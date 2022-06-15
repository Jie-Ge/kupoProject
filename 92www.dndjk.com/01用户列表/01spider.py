# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
用户列表
'''

import requests
from fake_useragent import UserAgent
from lxml import etree
import time

headers = {
    'Cookie': 'PHPSESSID=a0t7l16nh2tmlujggcjgh326m5',
    'Host': 'www.dndjk.com',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.dndjk.com/admin.html',
    'User-Agent': UserAgent().random
}

def get_detail(user_account):
    detail_url = f'http://www.dndjk.com/admin/account/edit.html?username={user_account}'
    res1 = requests.get(detail_url, headers=headers)
    with open(f'./{user_account}.html', 'w', encoding='utf-8') as ff:
        ff.write(res1.text)

num = 1
while num <= 18:
    print(num)
    url = f'http://www.dndjk.com/admin/account.html?page={num}'
    res = requests.get(url, headers=headers)

    page = etree.HTML(res.text)
    trs = page.xpath('//div[@class="card"]//tbody/tr')

    with open(f'./page{num}.html', 'w', encoding='utf-8') as f:
        f.write(res.text)

    for tr in trs:
        user_account_tag = tr.xpath('./td[3]/div[1]/text()')
        if user_account_tag:
            user_account = user_account_tag[0]

            get_detail(user_account)

    num += 1
    time.sleep(1)


