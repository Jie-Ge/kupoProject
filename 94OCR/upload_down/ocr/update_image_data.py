# !/usr/bin/python
# -*- coding: utf-8 -*-
import re
import threading

from utils_mysql import select_db_recode, insert_db_recode, up_data_recode
from card_adress_spider import get_card_address
from extract_image_info_all import extract_payer_info, extract_trade_time


def en_decode(str01):
    return str(str01).replace('\'', '').replace('\001', '').replace('\002', '') \
        .replace(r'\0xa0', '').replace('\n', ' ').replace('\r', ' ') \
        .encode("utf-8", 'ignore').decode("utf-8", "ignore")


def get_wallet_bank(content):
    '''匹配出钱包地址 和 银行卡号'''
    cmp1 = re.compile('bc1[0-9A-Za-z]{77}|(5|7)[0-9A-Za-z]{63}|erd1[0-9A-Za-z]{58}|(X|4)[0-9A-Za-z]{57}|G[0-9A-Za-z]{55}|'
                      '9[0-9A-Za-z]{50}|(4|2)[0-9A-Za-z]{43}|terra1[0-9A-Za-z]{38}(0x|xdc)[0-9A-Za-z]{40}|'
                      'SP2[0-9A-Za-z]{39}|tz1[0-9A-Za-z]{33}|(1|3|T|A)[0-9A-Za-z]{33}|0x[0-9A-Za-z]{32}')

    sear1 = cmp1.search(content)

    wallet_address = ''
    if sear1:
        wallet_address = sear1.group()

    return wallet_address



sql = "select * from `500彩票321387_历史对话_321387` where 钱包地址 != '';"
data = list(select_db_recode(sql))

def get_bank_addr():
    global data
    while data:
        print('剩余数量：', len(data))
        item = data.pop()
        s_id = item[0]
        content = item[1]

        wallet_address = get_wallet_bank(content)

        sql = f"UPDATE 永利集团269663_历史对话_269663 SET 钱包地址 = '{wallet_address}' " \
              f"where 对话id = '{s_id}' and 消息内容 = '{content}';"

        up_data_recode(sql)


def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=get_bank_addr)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()





