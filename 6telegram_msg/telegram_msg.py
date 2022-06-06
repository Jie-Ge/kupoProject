from telethon import TelegramClient, events, sync
from datetime import datetime, timedelta, date
import time
from loguru import logger
import asyncio
from utils import insert_db_history, select_db_record
from choice_table import get_table_name, get_max_seq
from telethon.tl.types import PeerUser
from extract_telegram_info import ExtractTelegraminfo

# Use your own values from my.telegram.org
api_id = 11943814
api_hash = '04e4fcdecbce07f3aa1a5001a30c56e9'

client = TelegramClient('history_msg_session', api_id, api_hash).start()


def en_decode(str01):
    return str(str01).replace('\'', '').replace('\001', '').replace('\002', '') \
        .replace(r'\0xa0', '').replace('\n', ' ').replace('\r', ' ') \
        .encode("utf-8", 'ignore').decode("utf-8", "ignore")


async def get_msg(channel_link, is_history_msg=False, msg_id=None):

    # 获取当前时间之前的历史数据
    date1 = (date.today()).strftime('%Y-%m-%d %H:%M:%S')  # xxxx-xx-xx 00:00:00, type: str
    date2 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')  # xxxx-xx-xx 00:00:00, type: datetime
    utc_date = date2 + timedelta(hours=-8)

    if is_history_msg:
        # 可以根据群地址拿到群里面的信息
        # offset_date会自动将date增加8小时
        # reverse：翻转（默认消息是最新到最旧）
        # offset_date：此日期之前的消息，若reverse=True，则是此日期之后的消息（最旧到最新）
        messages = client.iter_messages(channel_link, offset_date=utc_date)
    else:
        # 前一天的增量数据
        utc_date = utc_date + timedelta(hours=-24)
        messages = client.iter_messages(channel_link, offset_date=utc_date, reverse=True)

    async for message in messages:
        item = {}
        item['msg_id'] = str(message.id)
        if is_history_msg and msg_id and item['msg_id'] > str(msg_id):
            print('大了大了大了！！！')
            continue
        # print(message)

        item['username'] = ''
        item['first_name'] = ''
        item['last_name'] = ''
        # 获取发言者信息
        try:
            result_msg = await client.get_entity(message.from_id)
            item['username'] = str(result_msg.username)
            item['first_name'] = en_decode(str(result_msg.first_name))
            item['last_name'] = en_decode(str(result_msg.last_name))
        except Exception as e:
            pass

        if message.text:
            # (message.date + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
            date_time1 = message.date + timedelta(hours=8)
            item['link'] = channel_link
            item['date_time'] = date_time1
            item['text_info'] = en_decode(message.text)

            print(item)
            # 增量要添加此字段，以及添加插入数据库时的字段
            # item['result'] = ExtractTelegraminfo().get_increase_result(item['text_info'])

            table_name = get_table_name()
            if table_name:
                insert_db_history(item, table_name)


def get_new_links():
    sql = f"select link, is_new_add from telegram01.tg_group_info;"
    link_list = select_db_record(sql)

    channel_links = []
    new_links = []
    for tuple_item in link_list:
        channel_links.append(tuple_item[0])
        if tuple_item[1]:
            new_links.append(tuple_item[0])

    print(new_links)
    return channel_links, new_links


def get_msg_id():
    '''
    获取每个群的当前爬取到的最小message ID（历史全量数据是从最新到最旧爬取）；防止程序中断后从头爬取
    :return: 字典，每个群对应的message ID
    '''
    max_seq = get_max_seq()

    sql = f"select link, min(msg_id) from telegram01.telegram_msg_{max_seq} " \
          f"group by link;"
    link_list = select_db_record(sql)

    links_msgID = {}
    for tuple_item in link_list:
        links_msgID[tuple_item[0]] = tuple_item[1]

    return links_msgID


def async_get_msg(channel_links: list, new_links: list):
    # # 增量数据
    # tasks = []
    # for link in channel_links:
    #     msg = get_msg(link)
    #     task = asyncio.ensure_future(msg)
    #     tasks.append(task)
    #
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.gather(*tasks))

    # 新添加的群，获取历史全量数据
    if len(new_links):

        links_msgID_dic = get_msg_id()
        links_keys = links_msgID_dic.keys()

        is_history_msg = True
        print('开始爬取历史全量数据, new links:', new_links)
        tasks = []
        for link in new_links:
            msg_id = None
            if link in links_keys:
                msg_id = links_msgID_dic[link]
            msg = get_msg(link, is_history_msg, msg_id)
            task = asyncio.ensure_future(msg)
            tasks.append(task)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(*tasks))


if __name__ == '__main__':
    start_time = time.time()
    # channel_links, new_links = get_new_links()
    new_links = ['https://t.me/tianyanshequ']
    async_get_msg([], new_links)
    logger.info(f'程序结束，共耗时: {time.time()-start_time}s !')