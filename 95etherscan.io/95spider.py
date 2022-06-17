# !/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import multiprocessing
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import threading

from loguru import logger
import requests
from fake_useragent import UserAgent
from lxml import etree
import time
import random
import redis


def req_html():
    global block_height
    while r.scard('block_height'):
        transactions = ''
        contract_internal = ''

        block_height = r.spop('block_height').decode(encoding='utf-8')
        url = f'https://etherscan.io/block/{block_height}'

        headers = {
            'user-agent': UserAgent().random
        }
        try:
            res = requests.get(url, headers=headers, timeout=10)
            print(res.url)
            if 'busy' in res.url:
                r.sadd('block_height', block_height)
                time.sleep(10)
                continue
        except Exception as e:
            logger.error(e)
            r.sadd('block_height', block_height)
            continue

        page = etree.HTML(res.text)
        transactions_tag = page.xpath('//div[@id="ContentPlaceHolder1_div_tx_fieldvalue"]/a[1]/text()')
        if transactions_tag:
            transactions = transactions_tag[0].split(' ')[0]

        contract_internal_tag = page.xpath('//div[@id="ContentPlaceHolder1_div_tx_fieldvalue"]/a[2]/text()')
        if contract_internal_tag:
            contract_internal = contract_internal_tag[0].split(' ')[0]


        f1 = open('transactions_info.csv', 'a', encoding='utf=8', newline='')
        info_f = csv.writer(f1)


        print([res.url.split('/')[-1], transactions, contract_internal])
        info_f.writerow([res.url.split('/')[-1], transactions, contract_internal])

        time.sleep(random.randint(1, 3) + random.random())


r = redis.Redis('192.168.224.72', port=6379, db=3, password='123456')
total = 14900000
index = 0
def push_to_redis():
    global index, total
    while index <= total:
        r.sadd('block_height', index)
        index += 1


def main():
    if not os.path.exists('transactions_info.csv'):
        f1 = open('transactions_info.csv', 'a', encoding='utf=8', newline='')
        info_f = csv.writer(f1)
        info_f.writerow(['block_height', 'transactions', 'contract_internal_transactions'])


    # with ThreadPoolExecutor(max_workers=10) as pool:
    #     pool.submit(req_html)


    # tt = []
    # for i in range(5):
    #     t = threading.Thread(target=req_html, args=(info_f,))
    #     t.start()
    #     tt.append(t)
    # for t in tt:
    #     t.join()

    for i in range(5):
        t = threading.Thread(target=push_to_redis)
        t.start()

    ppp = []
    for i in range(5):
        p = multiprocessing.Process(target=req_html)
        p.start()
        ppp.append(p)

    for p in ppp:
        if p.is_alive():
            p.join()


if __name__ == '__main__':
    main()