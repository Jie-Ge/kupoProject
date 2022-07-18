
# !/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import time
import requests
from fake_useragent import UserAgent
import random
from lxml import etree
from queue import Queue
import pandas as pd
import csv
from loguru import logger
import os
from datetime import date
from utils_mysql import insert_db_recode
import redis
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

import urllib3
urllib3.disable_warnings()

ua = UserAgent()

url_num = 0  # url计数，用于显示进度
req_fail_url = []
error_url = []  # 无此链接：https://bscscan.com/token/XXXXXX
threadLock = threading.Lock()
count = 0
total_url_count = 0
page_queue = Queue()
all_proxy_ip = {'https': f'http://1.25.147.249:50844'}

r = redis.Redis('192.168.224.72', port=6379, db=1, password='123456', decode_responses=True)

print('地址总数：', r.scard('address_all'))


def run111():
    while r.scard('address_all'):
        contract = r.spop('address_all')
        # contract = '0x569297f97110d0ec06606bb16fbb7d1d25298120'
        if not contract:
            return None

        global url_num
        url_num += 1
        # if url_num > 10:
        #     return None
        print(f'正在请求第 {url_num} 个url：', threading.active_count())

        url_address = f'https://bscscan.com/address/{contract}'

        request_page(url_address, all_proxy_ip)
        time.sleep(random.randint(2, 4) + random.random())
        # break


def get_proxy_ip():
    ip_api = 'https://proxy.qg.net/replace?Key=1AFA2ED5&Num=1&KeepAlive=&AreaId=&Isp=&DataFormat=json&DataSeparator=&Detail=0&Distinct=1'
    try:
        res = requests.get(ip_api).json()
    except Exception as e:
        logger.info(e)
        return get_proxy_ip()

    if res['Code'] == 0:
        item = res['Data'][0]
        ip = item['host']
        return ip
    else:
        logger.info('请求IP的状态码为：', res['Code'])
        logger.error('等待30秒再请求IP')
        time.sleep(31)
        return get_proxy_ip()


def request_page(url, proxy_ip):
    global all_proxy_ip
    headers = {
        'user-agent': random.choice(ua.data_browsers['chrome'])
    }
    try:
        # requests版本原因，代理用http，proxies = {'http': f'http://{proxy_ips_list.pop()}'}
        print('代理：', proxy_ip)
        res = requests.get(url, headers=headers, proxies=proxy_ip, timeout=5, verify=False)
    except:
        threadLock.acquire()
        if all_proxy_ip == proxy_ip:
            print('请求失败，更换代理！！！')
            all_proxy_ip = {'https': f'http://{get_proxy_ip()}'}
        threadLock.release()

        print('请求出错=======')
        request_page(url, all_proxy_ip)
        # r.sadd('fail_contract', url.split('/')[-1])
        # raise

    else:
        if '/busy' in res.url:
            logger.info('busy请求过快，等待4秒！')
            time.sleep(4)
            request_page(url, proxy_ip)
        elif '/error' in res.url:
            r.sadd('error_contract', url.split('/')[-1])
        elif res.status_code == 200:
            print('请求的链接：', res.url)
            parse_data(res)
        elif res.status_code == 403:
            proxy_ip = get_proxy_ip()
            proxies = {'https': f'http://{proxy_ip}'}
            request_page(url, proxies)

        else:
            print('detail page请求失败，状态码：', res.status_code)
            r.sadd('fail_contract', url.split('/')[-1])


def en_decode(str01):
    return str(str01).replace('\'', '').replace('\001', '').replace('\002', '') \
        .replace(r'\0xa0', '').replace('\n', ' ').replace('\r', ' ') \
        .encode("utf-8", 'ignore').decode("utf-8", "ignore")


def parse_data(response):
    page = etree.HTML(response.text)

    if '/address' in response.url:
        address = 'NAN'
        full_title = 'NAN'
        short_title = 'NAN'
        divSummary1 = 'NAN'
        divSummary2 = 'NAN'

        address_tag = page.xpath('//span[@id="mainaddress"]/text()')
        if address_tag:
            address = address_tag[0]

        tokeninfo_tag = page.xpath('//div[@id="ContentPlaceHolder1_tr_tokeninfo"]//a//text()')
        if tokeninfo_tag:
            tokeninfo = ''.join(tokeninfo_tag).replace(',', '，').split(' (')
            full_title = tokeninfo[0]
            if len(tokeninfo) == 2:
                short_title = tokeninfo[1].replace(')', '')
            else:
                short_title = full_title

        divSummary1_tag = page.xpath('//div[@id="ContentPlaceHolder1_divSummary"]/div[@class="row mb-4"]')
        if divSummary1_tag:
            divSummary1 = etree.tostring(divSummary1_tag[0], encoding='utf-8').decode()

        divSummary2_tag = page.xpath('//div[@id="ContentPlaceHolder1_divSummary"]/div[@class="card"]')
        if divSummary2_tag:
            divSummary2 = etree.tostring(divSummary2_tag[0], encoding='utf-8').decode()
    else:
        print('请求到的不是正常的address page')
        r.sadd('error_contract', response.url.split('/')[-1])
        return None

    if address == 'NAN':
        r.sadd('error_contract', response.url.split('/')[-1])
        return None

    address_html = divSummary1 + divSummary2
    address_html = en_decode(address_html)

    sql = f"insert into bsc_address_all values ('{address}', '{full_title}', '{short_title}', '{address_html}')"
    insert_db_recode(sql)
    global count
    count += 1
    print('保存到的数据条数：', count)


# def run():
#     with ThreadPoolExecutor(max_workers=3) as pool:
#         pool.submit(run111)


def main():

    # ppp = []
    # for i in range(20):
    #     p = multiprocessing.Process(target=run)
    #     p.start()
    #     ppp.append(p)
    #
    # for p in ppp:
    #     if p.is_alive():
    #         p.join()

    tt = []
    for i in range(10):
        t = threading.Thread(target=run111)
        t.start()
        tt.append(t)
    for t in tt:
        t.join()


if __name__ == '__main__':

    s = time.time()
    main()
    print('耗时：', time.time()-s)