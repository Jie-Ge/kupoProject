from loguru import logger
import re
import time
from datetime import date, datetime
from utils import insert_db_group_info, del_db_group_info, up_db_group_info, select_db_record

from telethon import TelegramClient
from telethon.tl import functions
import asyncio
from telethon.tl.types import PeerUser, PeerChat, PeerChannel, UpdateNewChannelMessage
from telethon.tl.types import ChannelParticipantsAdmins
from telegram_msg import async_get_msg

api_id = 11943814
api_hash = '04e4fcdecbce07f3aa1a5001a30c56e9'

client = TelegramClient('new_msg_session', api_id, api_hash).start()


async def tg_get_group_part(channel_id):
    '''
    获取群成员
    note: 成员名有隐藏的，并且 telegram api 也会限制获取成员数量（5k-6k），所以获取到的成员不全
    :return:
    '''

    # ord_members_username = []  # 普通成员名
    # admin_username = []  # 管理员名
    members_username = []  # 所有成员

    # ===============获取admin========
    try:
        for user in await client.get_participants(
                await client.get_entity(PeerChannel(int('{channel_id}'.format(channel_id=channel_id)))),
                filter=ChannelParticipantsAdmins, aggressive=True):

            if user.username:
                members_username.append(user.username)
    except Exception as e:
        logger.error(e)

    print('===== 获取群管理员结束，总共{}个管理员 ===='.format(len(members_username)))

    # ===============获取群成员信息========
    channel = await client.get_entity(PeerChannel(int('{channel_id}'.format(channel_id=channel_id))))  # 根据群组id获取群组对

    try:
        async for ip in client.iter_participants(channel):
            # part_num += 1
            # if part_num % 100 == 0:
            #     print('获取了【{}】个用户'.format(part_num), 'channel_id', channel_id)

            if ip.username:
                members_username.append(ip.username)

    except Exception as e:
        logger.error(e)

    print('==== 获取所有群成员结束，总共{}个群成员 ===='.format(len(members_username)))

    return '{' + ','.join(members_username) + '}'  # postgresql保存为数组必须是大括号


async def tg_get_group_info(channel_link):
    '''
    获取群基本信息
    :return:
    '''
    result_group_info = []
    dict_temp = {}
    dict_temp['link'] = channel_link
    dict_temp['crawl_date'] = (date.today()).strftime('%Y-%m-%d')
    dict_temp['is_new_add'] = 0

    try:
        Chat_Full_Info = await client(
            functions.channels.GetFullChannelRequest(channel=channel_link)
        )
    except Exception as e:
        logger.error("Chat_Full_Info", e)
        return None
    try:
        # 群
        if Chat_Full_Info.chats[0].broadcast == False:
            dict_temp['name'] = Chat_Full_Info.chats[0].title
            dict_temp['group_id'] = str(Chat_Full_Info.chats[0].id)
            dict_temp['group_or_channel'] = 'group'
            try:
                dict_temp['introduction'] = Chat_Full_Info.full_chat.about
            except:
                dict_temp['introduction'] = " "
            try:
                dict_temp['members_amount'] = Chat_Full_Info.full_chat.participants_count
            except:
                dict_temp['members_amount'] = " "

            dict_temp['members_username'] = await tg_get_group_part(dict_temp['group_id'])

            result_group_info.append(dict_temp)

        # 频道
        elif Chat_Full_Info.chats[0].broadcast == True:
            dict_temp['name'] = Chat_Full_Info.chats[0].title
            dict_temp['channel_id'] = str(Chat_Full_Info.chats[0].id)
            dict_temp['group_or_channel'] = 'channel'
            try:
                dict_temp['introduction'] = Chat_Full_Info.full_chat.about
            except:
                dict_temp['introduction'] = " "

            try:
                dict_temp['members_amount'] = Chat_Full_Info.full_chat.participants_count
            except:
                dict_temp['members_amount'] = " "

            dict_temp['members_username'] = '{}'

            result_group_info.append(dict_temp)
        else:
            print("个人：......")
    except Exception as e:
        logger.error(e.args)

    # print('result......: ', result_group_info)

    sql = f"select * from telegram01.tg_group_info where link='{dict_temp['link']}';"

    if len(select_db_record(sql)):
        up_db_group_info(result_group_info)


def get_links():
    sql = f"select link, is_new_add from telegram01.tg_group_info;"
    link_list = select_db_record(sql)

    channel_links = []
    new_links = []
    for tuple_item in link_list:
        channel_links.append(tuple_item[0])
        if tuple_item[1]:
            new_links.append(tuple_item[0])

    return channel_links, new_links


def main():
    channel_links, new_links = get_links()

    # 获取聊天消息（增量数据 + 历史数据）
    async_get_msg([], new_links)

    # 更新群信息
    tasks = []
    for channel_link in channel_links:
        msg = tg_get_group_info(channel_link)
        task = asyncio.ensure_future(msg)
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))


if __name__ == '__main__':
    start_time = time.time()
    main()
    logger.info(f'程序结束，共耗时: {time.time()-start_time}s !')