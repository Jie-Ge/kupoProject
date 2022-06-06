
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
            time.sleep(random.randint(4, 6) + random.random())

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
                # requests版本原因，代理用http，proxies = {'http': f'http://{proxy_ips_list.pop()}'}
                print(proxy_ip)
                res = requests.get(url, headers=headers, proxies=proxy_ip, timeout=10, verify=False)
            except:
                if retry_count < 1:
                    print('请求失败，更换代理！！！')
                    # while not len(proxy_ips_list):
                    #     proxy_ips_list += self.get_proxy_ip()
                    #
                    # proxies = {'https': f'http://{proxy_ips_list.pop()}'}
                    # self.request_page(url, proxies)
                    return None
                else:
                    print('请求失败，重试！')
                    time.sleep(4)
                    retry_count -= 1
                    continue

            else:
                if ('/busy' in res.url) or (res.status_code == 403):
                    # while not len(proxy_ips_list):
                    #     proxy_ips_list += self.get_proxy_ip()
                    #
                    # proxies = {'https': f'http://{proxy_ips_list.pop()}'}
                    # self.request_page(url, proxies)
                    print('/busy......')
                    time.sleep(4)
                    return None
                elif '/error' in res.url:
                    error_url.append(url.split('/')[-1])
                elif res.status_code == 200:
                    print('请求的链接：', res.url)
                    # self.parse_data(res)

                else:
                    print('detail page请求失败，状态码：', res.status_code)
                    # req_fail_url.append(url.split('/')[-1])
            break

    def en_decode(self, str01):
        return str(str01).replace('\'', '').replace('\001', '').replace('\002', '') \
            .replace(r'\0xa0', '').replace('\n', ' ').replace('\r', ' ') \
            .encode("utf-8", 'ignore').decode("utf-8", "ignore")

    def parse_data(self, response):
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
        token_html = self.en_decode(token_html)

        data_list = []
        data_list.append(Contract)
        data_list.append(Title)
        data_list.append(Tag)
        data_list.append(Icon_href)
        data_list.append(Decimals)
        data_list.append(Official_Site)
        data_list.append(Social_Profiles)
        data_list.append(token_html)

        self.save_detail(data_list)

    def save_detail(self, data_list):
        threadLock.acquire()
        self.info_f.writerow(data_list)
        threadLock.release()

        global count
        count += 1
        print('保存到的数据条数：', count)


def not_req_urls():
    '''
    获取未请求过的url
    '''
    df = pd.read_csv('./contract_all.csv', header=None)
    req_url = df[0].tolist()  # all url

    reqed_url = []
    # if os.path.exists('get_contract_info1.csv'):
    #     df = pd.read_csv('get_contract_info1.csv', header=None)
    #     reqed_url = df[0].tolist()[1:]  # 已爬取过的url

    have_fail_url = []
    # if os.path.exists('./req_fail_url.csv'):
    #     df = pd.read_csv('./req_fail_url.csv', header=None)
    #     have_fail_url = df[0].tolist()  # 已爬取过的, 并且请求失败的url

    have_error_url = []
    # if os.path.exists('./error_url.csv'):
    #     df = pd.read_csv('./error_url.csv', header=None)
    #     have_error_url = df[0].tolist()  # 无此链接：https://bscscan.com/token/XXXXXX

    urls = list(set(req_url).difference(reqed_url, have_fail_url, have_error_url))  # 取差集，效率高

    for url in urls:
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