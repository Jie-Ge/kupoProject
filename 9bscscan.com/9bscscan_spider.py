
# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
爬取：https://www.mifengcha.com/ 的币种简介

'''

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
from utils import insert_db_record
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
proxy_ips_list = []

r = redis.Redis('192.168.224.72', port=6379, db=1, password='123456')

print('地址总数：', r.scard('contract'))

if not os.path.exists('get_contract_info.csv'):
    f1 = open('get_contract_info.csv', 'a', encoding='utf-8', newline='')
    info_f = csv.writer(f1)
    info_f.writerow(
        ['Contract', 'Title', 'Tag', 'Icon_href', 'Decimals', 'Official_Site', 'Social_Profiles', 'token_html'])
else:
    f1 = open('get_contract_info.csv', 'a', encoding='utf-8', newline='')
    info_f = csv.writer(f1)


def run111():
    global proxy_ips_list
    proxy_ips_list = get_proxy_ip()
    while r.scard('contract'):
        contract = r.spop('contract').decode(encoding='utf-8')
        if not contract:
            return None

        global url_num
        url_num += 1
        # if url_num > 10:
        #     return None
        print(f'正在请求第 {url_num} 个url：', threading.active_count())

        url_address = f'https://bscscan.com/token/{contract}'
        # while not len(proxy_ips_list):
        # proxy_ips_list = get_proxy_ip()

        proxies = {'https': f'http://{proxy_ips_list[0]}'}
        request_page(url_address, proxies)
        time.sleep(random.randint(2, 4) + random.random())


def get_proxy_ip():
    ip_api = 'http://api.shenlongip.com/ip?key=lggx7gkw&pattern=json&count=1&need=1000&protocol=1'
    try:
        res = requests.get(ip_api)
    except:
        return []

    ips = []
    for item in res.json()['data']:
        ips.append(item['ip'] + ':' + str(item['port']))

    return ips


def request_page(url, proxy_ip=None):
    global proxy_ips_list
    retry_count = 3
    while True:
        headers = {
            'user-agent': random.choice(ua.data_browsers['chrome'])
        }
        try:
            # requests版本原因，代理用http，proxies = {'http': f'http://{proxy_ips_list.pop()}'}
            res = requests.get(url, headers=headers, proxies=proxy_ip, timeout=5, verify=False)
        except:
            if retry_count < 1:
                print('请求失败，更换代理！！！')
                proxy_ips_list = get_proxy_ip()

                proxies = {'https': f'http://{proxy_ips_list[0]}'}
                request_page(url, proxies)
                # r.sadd('fail_contract', url.split('/')[-1])
                return None
            else:
                print('请求失败，重试！等待5秒')
                retry_count -= 1
                time.sleep(5)
                continue

        else:
            if ('/busy' in res.url) or (res.status_code == 403):
                proxy_ips_list = get_proxy_ip()

                proxies = {'https': f'http://{proxy_ips_list[0]}'}
                request_page(url, proxies)
                # r.sadd('fail_contract', url.split('/')[-1])
                return None
            elif '/error' in res.url:
                r.sadd('error_contract', url.split('/')[-1])
            elif res.status_code == 200:
                print('请求的链接：', res.url)
                parse_data(res)

            else:
                print('detail page请求失败，状态码：', res.status_code)
                r.sadd('fail_contract', url.split('/')[-1])
        break

def en_decode(str01):
    return str(str01).replace('\'', '').replace('\001', '').replace('\002', '') \
        .replace(r'\0xa0', '').replace('\n', ' ').replace('\r', ' ') \
        .encode("utf-8", 'ignore').decode("utf-8", "ignore")

def parse_data(response):
    Contract = ''
    Title = ''
    Tag = ''
    Icon_href = ''
    Decimals = ''
    Official_Site = ''

    Social_Profiles = {}

    try:
        page = etree.HTML(response.text)

        if '/token' in response.url:
            Contract_tag = page.xpath('//div[@class="d-flex clipboard-hover"]/a[1]/text()')
            if len(Contract_tag):
                Contract = Contract_tag[0]

            title_tag = page.xpath('//h1//span[@class="text-secondary small"]/text()')
            if len(title_tag):
                Title = title_tag[0]

            tag_tag = page.xpath("//a[contains(@class, 'u-label')]/text()")
            if len(tag_tag):
                Tag = ','.join(tag_tag)

            Icon_tag = page.xpath('//h1/img/@src')
            if len(Icon_tag):
                Icon_href = Icon_tag[0]

            Decimals_label = page.xpath('//div[@id="ContentPlaceHolder1_trDecimals"]//div[@class="col-md-8"]/text()')
            if len(Decimals_label):
                Decimals = Decimals_label[0].replace('\n', '')

            Official_Site_tag = page.xpath(
                '//div[@id="ContentPlaceHolder1_tr_officialsite_1"]//div[@class="col-md-8"]/a/text()')
            if len(Official_Site_tag):
                Official_Site = Official_Site_tag[0]

            Social_Profiles_tags = page.xpath("//ul[@class='list-inline mb-0']/li")
            if len(Social_Profiles_tags):
                for li in Social_Profiles_tags:
                    original_title = li.xpath('./a/@data-original-title')
                    href_tag = li.xpath('./a/@href')
                    if len(original_title) and len(href_tag):
                        k = original_title[0].split(':')[0]
                        v = href_tag[0]
                        Social_Profiles[k] = v
        else:
            print('请求到的不是正常的address page')
            req_fail_url.append(response.url.split('/')[-1])
            return None
    except Exception as e:
        logger.error('parse data出错，链接：', response.url, e)
        req_fail_url.append(response.url.split('/')[-1])
        return None

    title = ''
    summary = ''
    title_tag = page.xpath('//div[@class="mb-3 mb-lg-0"]')
    if len(title_tag):
        title = etree.tostring(title_tag[0], encoding='utf-8').decode()

    summary_tag = page.xpath('//div[@id="ContentPlaceHolder1_divSummary"]/div[@class="row mb-4"]')
    if len(summary_tag):
        summary = etree.tostring(summary_tag[0], encoding='utf-8').decode()

    token_html = title + summary
    token_html = en_decode(token_html)

    data_list = []
    data_list.append(Contract)
    data_list.append(Title)
    data_list.append(Tag)
    data_list.append(Icon_href)
    data_list.append(Decimals)
    data_list.append(Official_Site)
    data_list.append(Social_Profiles)
    data_list.append(token_html)

    save_detail(data_list)

def save_detail(data_list):
    threadLock.acquire()
    info_f.writerow(data_list)
    threadLock.release()

    global count
    count += 1
    print('保存到的数据条数：', count)


def run():
    with ThreadPoolExecutor(max_workers=3) as pool:
        pool.submit(run111)


def main():

    ppp = []
    for i in range(20):
        p = multiprocessing.Process(target=run)
        p.start()
        ppp.append(p)

    for p in ppp:
        if p.is_alive():
            p.join()


if __name__ == '__main__':

    s = time.time()
    main()
    print('耗时：', time.time()-s)