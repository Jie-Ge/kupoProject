# !/usr/bin/python
# -*- coding: utf-8 -*-
import threading

from utils_mysql import select_db_recode, insert_db_recode
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
        receipt = item[2] if item[2] else ''
        receipt_account = item[3] if item[3] else ''
        receipt_bank = item[4] if item[4] else ''

        receipt_account_addr = ''
        if receipt_account and receipt_account.isdigit():
            try:
                receipt_account_addr = get_card_address(receipt_account)
            except:
                pass

        payer, payer_account, payer_bank = extract_payer_info(content)
        payer_account_addr = ''
        if payer_account and payer_account.isdigit():
            try:
                payer_account_addr = get_card_address(payer_account)
            except:
                pass

        trade_time = extract_trade_time(content)

        sql = f"insert into jinsha_chat_image_info_01_new " \
              f"values ('{image_url}', '{en_decode(content)}', '{receipt}', '{receipt_account}', '{receipt_bank}', '{payer}', '{payer_account}', '{payer_bank}', '{receipt_account_addr}', '{payer_account_addr}', '{trade_time}')"

        insert_db_recode(sql)


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





