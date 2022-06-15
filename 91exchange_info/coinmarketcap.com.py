# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    :  2022/6/8 14:42
@Author  :  JayYoung
@Python  :  Python3.7
@Desc    :  https://coinmarketcap.com/rankings/exchanges/
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
    url = 'https://coinmarketcap.com/rankings/exchanges/'
    headers = {
        'user-agent': UserAgent().random
    }

    res = requests.get(url, headers=headers)
    page = etree.HTML(res.text)
    json_string = page.xpath('//script[@id="__NEXT_DATA__"]/text()')[0]

    json_data = json.loads(json_string)

    exchanges_list = json_data['props']['pageProps']['exchange']

    for item in exchanges_list:
        name = item['name']
        slug = item['slug']
        create_date = item['dateLaunched']
        rank = item['rank']

        crawl_address = f'https://coinmarketcap.com/exchanges/{slug}/'
        official_website = req_detail(crawl_address)
        create_region = ''

        sql = f"insert into all_name_website " \
              f"values('{name}', '{official_website}', '{crawl_address}', '{create_date}', '{create_region}', '{rank}')"

        print(sql)
        cursor.execute(sql)
        db.commit()

        time.sleep(0.5 + random.random())


if __name__ == '__main__':
    cursor = db.cursor()
    req_html()
    db.close()
