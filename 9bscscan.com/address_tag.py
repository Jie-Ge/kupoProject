# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    :  2022/5/31 14:27
@Version :  1.0
@Python  :  Python3.7
@Desc    :  网站：https://bscscan.com/labelcloud
            此网站限速严重，得睡久一点
            每个月跑一次，累加；
            跑之前更换cookie；
            跑之前先清空redis；
            对于量大的（上百万），访问比较慢，请求超时，会放在redis中的error表中，需要拿出来在 address_tag_error.py 中单独跑
"""

from fake_useragent import UserAgent
import requests
from lxml import etree
from utils_mysql import insert_db_recode, select_db_recode
import random
import time
import redis

tag_sql = 'SELECT MAX(id) FROM address_tag_bscscan'
tag_id = select_db_recode(tag_sql)[0][0]
if not tag_id:
    tag_id = 1
else:
    tag_id += 1
print(tag_id)

token_sql = 'SELECT MAX(id) FROM address_token_bscscan'
token_id = select_db_recode(token_sql)[0][0]
if not token_id:
    token_id = 1
else:
    token_id += 1
print(token_id)

total_num = 0

class AddrTag(object):
    def __init__(self, session1):
        self.session = session1
        self.ua = UserAgent()
        self.domain = 'https://bscscan.com'
        self.labelcloud_url = 'https://bscscan.com/labelcloud'
        self.accounts_url = 'https://bscscan.com/accounts/'
        self.cookie = 'ASP.NET_SessionId=vwa0hfpldb0c4yji2xfp5fkl; bscscan_cookieconsent=True; cf_clearance=r9f7wCqbwaAebNodfDYExQdhZfZK.2dwTTG_dmYwt70-1653470573-0-150; _gid=GA1.2.677907469.1653879543; __stripe_mid=dd98c17c-f75e-43d9-8dbc-b78bcc2c41cdea8ffc; bscscan_userid=jay777777; bscscan_autologin=True; bscscan_pwd=4792:Qdxb:v8uWlkEPwPKo8fiFQkwSfA==; __cflb=02DiuJNoxEYARvg2sN6cLGJRqRcE6ZmC7m9dPutvYuPXr; __cf_bm=98zS5djXKiflD9wvIC._iQ6y.oXjm4yLPmBbJL.eyz4-1654061007-0-AQzH1NEOXhkP752AzW6j4a64SxNX1zvaKafURdlo2AEbp1q1DFtjcUTqeXzH8q4TBoipxt+R6MG6n4rKCjuzqA/nPos7wxEL/lAM6Vdma/DzShLDSqxVJZ79GntoCqxxxg==; _ga_PQY6J2Q8EP=GS1.1.1654059818.58.1.1654061237.0; _ga=GA1.2.1197962558.1649324659'
        self.r = redis.Redis('192.168.224.72', port=6379, db=1, password='123456', decode_responses=True)

    def run(self):
        headers = {
            'user-agent': self.ua.random,
            'cookie': self.cookie
        }
        res = self.session.get(self.labelcloud_url, headers=headers, timeout=20)
        if res.status_code == 200:
            self.parse_detail_url(res)

    def parse_detail_url(self, res):
        success_accounts_addr = list(self.r.smembers('success_accounts_addr'))
        success_token_addr = list(self.r.smembers('success_token_addr'))

        page = etree.HTML(res.text)
        divs = page.xpath('//div[@class="row mb-3"]/div')
        for div in divs:
            category = ''
            acc_url = ''
            token_url = ''

            category_list = div.xpath('.//button/span/text()')
            if category_list:
                category = category_list[0]

            href_list = div.xpath('.//div[contains(@class, "dropdown-menu")]/a/@href')
            print('href_list: ', href_list)
            if href_list:
                for href in href_list:
                    if href.startswith('/accounts'):
                        acc_url = href
                    elif href.startswith('/tokens'):
                        token_url = href

            if acc_url not in success_accounts_addr:
                if self.req_accounts_url(acc_url, category):
                    self.r.sadd('success_accounts_addr', acc_url)  # 记录请求成功
            if token_url not in success_token_addr:
                if self.req_token_url(token_url, category):
                    self.r.sadd('success_token_addr', token_url)

            time.sleep(random.randint(5, 7) + random.random())

    def req_accounts_url(self, detail_url, category, page_num=1):
        if not detail_url:
            return None

        headers = {
            'user-agent': self.ua.random,
            'cookie': self.cookie
        }

        while True:
            try:
                url = self.domain + detail_url + f'/{page_num}?ps=100'
                print(url)
                res = self.session.get(url, headers=headers, timeout=20)
            except:
                print('accounts失败。。。。: ', detail_url, page_num)
                self.r.sadd('error_accounts_addr', detail_url)
                return False
            else:
                if res.status_code == 200:
                    is_finish = self.parse_accounts_data(res, category)
                    # 最大只能拿到一万条记录，达到最大后再翻页，会跳转到下面的链接
                    if is_finish or res.url == 'https://bscscan.com/accounts':
                        return True
                else:
                    print('accounts status_code != 200。。。。: ', res.url)
                    self.r.sadd('error_accounts_addr', detail_url)
                    return False
            time.sleep(random.randint(5, 7) + random.random())
            page_num += 1

    def req_token_url(self, detail_url, category, start=0):
        if not detail_url:
            return None

        headers = {
            'user-agent': self.ua.random,
            'cookie': self.cookie
        }

        size = 100
        while True:
            params = {
                'subcatid': 'undefined',
                'size': 100,
                'start': start,
                'col': 3,
                'order': 'desc'
            }

            try:
                url = self.domain + detail_url
                res = self.session.get(url, headers=headers, params=params, timeout=20)
            except:
                print('token失败。。。。: ', detail_url, start)
                self.r.sadd('error_token_addr', detail_url)
                return False
            else:
                if res.status_code == 200:
                    is_finish = self.parse_token_data(res, category)
                    if is_finish:
                        return True
                else:
                    print('token status_code != 200。。。。: ', res.url)
                    self.r.sadd('error_token_addr', detail_url)
                    return False

            time.sleep(random.randint(5, 7) + random.random())
            start += size

    def parse_accounts_data(self, res, category):
        global tag_id
        global total_num
        page = etree.HTML(res.text)
        trs = page.xpath('//div[@id="ContentPlaceHolder1_divTable"]//tbody[1]/tr')
        if trs:
            for tr in trs:
                total_num += 1
                print('total_num: ', total_num)
                address = ''
                name_tag = ''
                address_tag = tr.xpath('.//a/text()')
                if address_tag:
                    address = address_tag[0]

                name_tag_tag = tr.xpath('./td[2]/text()')
                if name_tag_tag:
                    name_tag = name_tag_tag[0]

                if address and name_tag:
                    sql = f"insert into address_tag_bscscan(address, category, name_tag, id, href) values('{address}', '{category}', '{name_tag}', '{tag_id}', 'https://bscscan.com/labelcloud');"
                    if insert_db_recode(sql):
                        print('accounts: ', address, name_tag, category, tag_id)
                        tag_id += 1
        else:
            print('accounts页面数据为空。。。。: ', res.url)
            self.r.sadd('error_accounts_addr', res.url)

        # 判断每页有没有100条记录，来判断是否是最后一页
        if len(trs) < 100:
            return True

    def parse_token_data(self, res, category):
        global token_id
        global total_num
        page = etree.HTML(res.text)
        trs = page.xpath('//div[@class="tab-content"]//table/tbody/tr')
        if trs:
            for tr in trs:
                total_num += 1
                print('total_num: ', total_num)
                address = ''
                token_name = ''
                address_tag = tr.xpath('.//div[@class="d-block"]/a/text()')
                if address_tag:
                    address = address_tag[0]

                token_name_tag = tr.xpath('.//div[contains(@class, "media-body")]/a/text()')
                if token_name_tag:
                    token_name = token_name_tag[0]

                if address and token_name:
                    sql = f"insert into address_token_bscscan(address, category, token_name, id, href) values('{address}', '{category}', '{token_name}', '{token_id}', 'https://bscscan.com/labelcloud');"
                    if insert_db_recode(sql):
                        print('token: ', address, token_name, category, token_id)
                        token_id += 1
        else:
            print('token页面数据为空。。。。: ', res.url)
            self.r.sadd('error_token_addr', res.url)

        if len(trs) < 100:
            return True


if __name__ == '__main__':
    session = requests.session()
    AddrTag(session).run()
    print(total_num)