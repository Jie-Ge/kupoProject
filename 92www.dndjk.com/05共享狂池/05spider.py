# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
共享狂池
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

num = 1
while num <= 1:
    print(num)
    url = f'http://www.dndjk.com/admin/event/pool.html'
    res = requests.get(url, headers=headers)

    with open(f'./05pool.html', 'w', encoding='utf-8') as f:
        f.write(res.text)

    num += 1
    time.sleep(1)
