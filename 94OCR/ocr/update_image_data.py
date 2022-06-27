# !/usr/bin/python
# -*- coding: utf-8 -*-
import threading

from utils_mysql import select_db_recode, insert_db_recode, up_data_recode
from card_adress_spider import get_card_address
from extract_image_info_all import extract_payer_info, extract_trade_time


def en_decode(str01):
    return str(str01).replace('\'', '').replace('\001', '').replace('\002', '') \
        .replace(r'\0xa0', '').replace('\n', ' ').replace('\r', ' ') \
        .encode("utf-8", 'ignore').decode("utf-8", "ignore")


sql = 'select * from jinsha_chat_image_info_01'
data = list(select_db_recode(sql))


def get_bank_addr():
    global data
    while data:
        print('剩余数量：', len(data))
        item = data.pop()
        image_url = item[0]
        content = item[1]

        payer, payer_account, payer_bank = extract_payer_info(content)

        trade_time = extract_trade_time(content)

        sql = f"UPDATE jinsha_chat_image_info_01 SET 付款人 = '{payer}', 付款账号 = '{payer_account}', 付款银行 = '{payer_bank}', 交易时间 = '{trade_time}' " \
              f"where image_url = '{image_url}';"

        up_data_recode(sql)


def main():
    threads = []
    for i in range(50):
        t = threading.Thread(target=get_bank_addr)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()





