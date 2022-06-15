# !/usr/bin/python
# -*- coding: utf-8 -*-


# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
仪表盘
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
while num <= 18:
    print(num)
    url = f'http://www.dndjk.com/admin/account/dashboard.html?page={num}'
    res = requests.get(url, headers=headers)

    with open(f'./03file/03page{num}.html', 'w', encoding='utf-8') as f:
        f.write(res.text)

    num += 1
    time.sleep(1)

