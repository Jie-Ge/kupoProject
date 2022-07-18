
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

url_num = 0  # url计数，用于显示进度
req_fail_url = []
error_url = []  # 无此链接：https://bscscan.com/token/XXXXXX
threadLock = threading.Lock()
count = 0
total_url_count = 0
page_queue = Queue()
proxy_ips_list = []

r = redis.Redis('192.168.224.72', port=6379, db=1, password='123456')

print('地址总数：', r.scard('address_all'))

def run111():
    logger.add('error_log.out', level='ERROR')

    global proxy_ips_list
    proxy_ips_list = get_proxy_ip()
    while r.scard('address_all'):
        try:
            contract = r.spop('address_all').decode(encoding='utf-8')
            if not contract:
                return None

            global url_num
            url_num += 1
            # if url_num > 10:
            #     return None
            print(f'正在请求第 {url_num} 个url：', threading.active_count())

            url_address = f'https://bscscan.com/address/{contract}'
            # while not len(proxy_ips_list):
            # proxy_ips_list = get_proxy_ip()

            proxies = {'https': f'http://STHB9U24:62E81DC42692@{proxy_ips_list[0]}'}
            request_page(url_address, proxies)
            time.sleep(random.randint(2, 4) + random.random())
        except Exception as e:
            logger.error(e)


def get_proxy_ip():
    logger.error('更换IP')
    ip_api = 'https://proxy.qg.net/allocate?Key=STHB9U24&Num=1&AreaId=&DataFormat=json&DataSeparator=&Detail=0'
    try:
        res = requests.get(ip_api).json()
        if res['Code'] == 0:
            item = res['Data'][0]
            ip = item['host']
            return [ip]
        else:
            logger.info('请求IP的状态码为：', res['Code'])
            return get_proxy_ip()
    except Exception as e:
        logger.info(e)
        return get_proxy_ip()


def request_page(url, proxy_ip=None):
    global proxy_ips_list
    retry_count = 3
    while True:
        headers = {
            'user-agent': UserAgent().random
        }
        try:
            response = requests.get(url, headers=headers, proxies=proxy_ip, timeout=5, verify=False, stream=True)
            # print(response.raw._connection.sock.getpeername())
        except:
            if retry_count < 1:
                # print('3次请求失败，更换代理！！！')
                proxy_ips_list = get_proxy_ip()

                proxies = {'https': f'http://STHB9U24:62E81DC42692@{proxy_ips_list[0]}'}
                request_page(url, proxies)
                # r.sadd('fail_contract', url.split('/')[-1])
                return None
            else:
                # print('请求失败，重试！等待1秒')
                retry_count -= 1
                proxy_ip = {'https': f'http://STHB9U24:62E81DC42692@{proxy_ips_list[0]}'}
                time.sleep(1)
                continue

        else:
            if ('/busy' in response.url) or (response.status_code == 403):
                # proxy_ips_list = get_proxy_ip()
                #
                # proxies = {'https': f'http://STHB9U24:62E81DC42692@{proxy_ips_list[0]}'}
                request_page(url, proxy_ip)
                # r.sadd('fail_contract', url.split('/')[-1])
                return None
            elif '/error' in response.url:
                r.sadd('error_contract', url.split('/')[-1])
            elif response.status_code == 200:
                print('请求的链接：', response.url)
                parse_data(response)

            else:
                print('detail page请求失败，状态码：', response.status_code)
                r.sadd('fail_contract', url.split('/')[-1])
        break


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


def run():
    with ThreadPoolExecutor(max_workers=3) as pool:
        pool.submit(run111)


def main():

    ppp = []
    for i in range(40):
        p = multiprocessing.Process(target=run)
        p.start()
        ppp.append(p)

    for p in ppp:
        if p.is_alive():
            p.join()


if __name__ == '__main__':
    '''
    15:13   26,183
    15:20   28,147  7466个
    15:29   31,624  7466个
    15:40   38,446  7321个
    15:50   45,453  7113个
    16:02   53,740  6878个
    16:22   66,356  6384个
    16:32   72,833  
    '''
    s = time.time()
    main()
    print('耗时：', time.time()-s)