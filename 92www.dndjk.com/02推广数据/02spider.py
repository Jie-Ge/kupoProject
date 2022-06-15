# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
推广数据
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
    url = f'http://www.dndjk.com/admin/account/promotion.html?page={num}'
    res = requests.get(url, headers=headers)

    page = etree.HTML(res.text)
    trs = page.xpath('//div[@class="card"]//tbody/tr')

    with open(f'./02file/02page{num}.html', 'w', encoding='utf-8') as f:
        f.write(res.text)

    num += 1
    time.sleep(1)



