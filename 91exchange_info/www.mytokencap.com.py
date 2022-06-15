# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    :  2022/6/8 15:46
@Author  :  JayYoung
@Python  :  Python3.7
@Desc    :  https://www.mytokencap.com/exchange
"""

import requests
from lxml import etree
import json
import pandas as pd
from fake_useragent import UserAgent
import pymysql
import time
import random


db = pymysql.connect(host='192.168.224.49',
                     port=33060,
                     user='root',
                     password='12345678',
                     database='exchanges')


def req_detail(url):
    headers = {
        'user-agent': UserAgent().random
    }
    res = requests.get(url, headers=headers)
    page = etree.HTML(res.text)
    website_tag = page.xpath('//ul[contains(@class, "cmc-details-panel-links")]/li[1]/a/@href')
    if website_tag:
        if website_tag[0].startswith('http'):
            official_website = website_tag[0]
            return official_website
    return ''


def req_html():
    url = 'https://api.mytokenapi.com/exchange/listbyexchangevolume'
    headers = {
        'user-agent': UserAgent().random
    }
    page_num = 1
    while page_num <= 3:
        parmas = {
            'page': page_num,
            'size': 50,
            'need_pagination': 1,
            'timestamp': '1654674635045',
            'code': 'cead6884746e1fa18264adca346d2c36',
            'platform': 'web_pc',
            'v': '1.0.0',
            'language': 'zh_CN',
            'legal_currency': 'USD'
        }

        json_data = requests.get(url, headers=headers, params=parmas).json()
        data_list = json_data['data']['list']
        for item in data_list:
            name = item['alias'] if item['alias'] else item['name']
            create_date = ''
            rank = item['rank']
            crawl_address = 'https://www.mytokencap.com/exchange'
            official_website = item['website']
            create_region = item['country_name']

            sql = f"insert into all_name_website " \
                  f"values('{name}', '{official_website}', '{crawl_address}', '{create_date}', '{create_region}', '{rank}')"

            print(sql)

            cursor.execute(sql)
            db.commit()

        page_num += 1


if __name__ == '__main__':
    cursor = db.cursor()
    req_html()
    db.close()
