
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


class Icon2Thread(threading.Thread):
    def __init__(self, info_f):
        threading.Thread.__init__(self)
        self.info_f = info_f

    def run(self):
        global proxy_ips_list
        proxy_ips_list = self.get_proxy_ip()
        while not page_queue.empty():
            contract = page_queue.get(block=False)

            global url_num
            url_num += 1
            # if url_num > 10:
            #     return None
            print(f'正在请求第 {url_num}/{total_url_count} 个url：', threading.active_count())

            url_address = f'https://bscscan.com/token/{contract}'
            # while not len(proxy_ips_list):
            #     proxy_ips_list += self.get_proxy_ip()
            #
            proxies = {'https': f'http://{proxy_ips_list[0]}'}
            self.request_page(url_address, proxies)
            time.sleep(random.randint(2, 4) + random.random())

    @staticmethod
    def get_proxy_ip():
        ip_api = 'https://proxy.qg.net/allocate?Key=835ACE84&Num=1&AreaId=&Isp=&DataFormat=json&DataSeparator=&Detail=0&Distinct=0'

        try:
            res = requests.get(ip_api)
        except:
            return []
        print(res.json())
        ips = []
        for item in res.json()['Data']:
            ips.append(item['host'])

        return ips

    def request_page(self, url, proxy_ip=None):
        global proxy_ips_list

        retry_count = 3
        while True:
            headers = {
                'user-agent': random.choice(ua.data_browsers['chrome'])
            }
            try:
                print(proxy_ip)
                res = requests.get(url, headers=headers, proxies=proxy_ip, timeout=10, verify=False)
            except:
                if retry_count < 1:
                    print('请求失败，更换代理！！！')
                    return None
                else:
                    print('请求失败，重试！')
                    time.sleep(2)
                    retry_count -= 1
                    continue

            else:
                if ('/busy' in res.url) or (res.status_code == 403):
                    print('/busy......')
                    time.sleep(2)
                    return None
                elif '/error' in res.url:
                    error_url.append(url.split('/')[-1])
                elif res.status_code == 200:
                    print('请求的链接：', res.url)

                else:
                    print('detail page请求失败，状态码：', res.status_code)
            break

def not_req_urls():
    '''
    获取未请求过的url
    '''
    df = pd.read_csv('./contract_all.csv', header=None)
    req_url = df[0].tolist()  # all url

    for url in req_url:
        page_queue.put(url)


def main():
    not_req_urls()

    global total_url_count
    total_url_count = page_queue.qsize()

    if not os.path.exists('get_contract_info1.csv'):
        f1 = open('get_contract_info1.csv', 'a', encoding='utf=8', newline='')
        info_f = csv.writer(f1)
        info_f.writerow(['Contract', 'Title', 'Tag', 'Icon_href', 'Decimals', 'Official_Site', 'Social_Profiles', 'token_html'])
    else:
        f1 = open('get_contract_info1.csv', 'a', encoding='utf=8', newline='')
        info_f = csv.writer(f1)

    threads2 = []
    for i in range(1):
        t = Icon2Thread(info_f)
        t.start()
        threads2.append(t)

    for t in threads2:
        t.join()

    f1.close()

    print(f'共 {total_url_count} 个page url')
    print('请求成功的page url数量：', count)
    print(f'{len(req_fail_url)}个page url请求失败：', req_fail_url)
    print(f'{len(error_url)}个error url')

    # if len(req_fail_url):
    #     with open('./req_fail_url.csv', 'a', encoding='utf=8', newline='') as f:
    #         writ_f = csv.writer(f)
    #         for url in req_fail_url:
    #             writ_f.writerow([url])
    #
    # if len(error_url):
    #     with open('./error_url.csv', 'a', encoding='utf=8', newline='') as f:
    #         writ_f = csv.writer(f)
    #         for url in error_url:
    #             writ_f.writerow([url])


if __name__ == '__main__':

    s = time.time()
    main()
    print('耗时：', time.time()-s)