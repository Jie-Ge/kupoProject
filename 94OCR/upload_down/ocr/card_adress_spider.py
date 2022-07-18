import os
import re
import threading

import requests
import redis
from loguru import logger
from lxml import etree
import json

import sys
sys.path.append(os.path.abspath('./ocr'))
from utils_mysql import select_db_recode, up_data_recode

cookie_list = "bank_cookies_list"
r = redis.Redis(host="192.168.224.72", port=6379, db=3, password='123456')
card_list = []


def rewrite_request(url=None, cookies=None):
    '''调用API解析银行卡号'''
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    }
    if not cookies:
        cookies = {}
    while True:
        try:
            response = requests.get(url=url, cookies=cookies, headers=headers, timeout=10)
            break
        except Exception as e:
            pass
    return response


def get_api_card_address(card_id):
    url = f"https://api.kazhiguo.com/api/bankcard/apikey=ef93e0ba04c6662ffe75f03d00d3acc1&bankcard={card_id}"
    response = rewrite_request(url=url)
    json_data = response.json()['result']
    return json_data


def card_address(card_id):
    print('API获取银行卡号归属地：card_id=', card_id)
    json_data = get_api_card_address(card_id)
    if 'error' in json_data.keys():
        error_code = json_data['error']
        if error_code == 1:
            return '银行卡号API余额不足', 0
        if error_code == 2:
            return '银行卡号API有效期已过', 0
        if error_code == 3:
            return '银行卡号错误', ''
    address = json_data['address']
    bank_name = json_data['bank_name'] + '-' + json_data['card_type']

    return address, bank_name


def parse_card(table_name, date_time):
    global card_list
    while card_list:
        print('card_list:', len(card_list))
        card_id = card_list.pop()
        if card_id and card_id.isdigit():
            address, bank_name = card_address(card_id)
            if bank_name == 0:
                logger.remove()
                logger.add('main_error_log.out')
                logger.error(address)
                return address

        sql = f"UPDATE `{table_name}` SET `银行卡号归属地`='{address}', `银行卡号开户行`='{bank_name}' " \
              f"where (银行卡号='{card_id}') and (入库时间='{date_time}');"
        up_data_recode(sql)

        sql = f"select distinct `银行卡号` from `{table_name}` where (入库时间 = '{date_time}') and (银行卡号 != '') and (银行卡号归属地 is null);"
        result = select_db_recode(sql)
        r.set('card_progress_n', len(result))


def thread_get_card_address(table_name, date_time):
    threads = []
    for i in range(20):
        t = threading.Thread(target=parse_card, args=(table_name, date_time))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


def get_new_date(table_name):
    '''获取最新数据的入库时间'''
    sql = f'select max(入库时间) from `{table_name}`'
    result = select_db_recode(sql)

    if result:
        date_time = result[0][0]
        return date_time
    else:
        return None


def get_card_address(table_name):
    global card_list
    date_time = get_new_date(table_name)
    if not date_time:
        logger.remove()
        logger.add('mysql_error_log.out')
        logger.error('无法获取表中的 "入库时间" 字段')
        return '无法获取表中的 "入库时间" 字段'

    sql = f"select `银行卡号` from `{table_name}` where (入库时间 = '{date_time}') and (银行卡号 != '') and (银行卡号归属地 is null);"
    result = select_db_recode(sql)
    card_list = []
    for item in result:
        card_id = item[0]
        card_list.append(card_id)

    card_list = list(set(card_list))

    r.set('card_progress_total', len(card_list))
    thread_get_card_address(table_name, date_time)

    return '解析银行卡归属地已完成！'


if __name__ == '__main__':
    address, bank_name = card_address('6230522860022192176')
    print(address, bank_name)
