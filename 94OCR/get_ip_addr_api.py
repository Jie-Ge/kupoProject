'''
调用收费网站api识别IP归属地
网站：https://www.apispace.com/eolink/api/ipguishu/api/
'''


import csv
import pandas as pd
import requests
import os
from os import path
import threading
import redis
import json


r = redis.Redis('192.168.224.72', port=6379, db=3, password='123456')

def get_asn():
    '''
    获取 ip 归属地
    '''
    # global ip_asn, ips, have_ips

    while r.scard('ip_fail'):
        ip = r.spop('ip_fail').decode(encoding='utf-8')

        querystring = {"ip": f"{ip}", "coordsys": "WGS84"}

        url = "https://eolink.o.apispace.com/ipguishu/ip/geo/v1/district"
        payload = ""
        headers = {
            'X-APISpace-Token': 'h1u6yitkhwl9df38wic40zh5yzsyvcau',
            'Authorization-Type': 'apikey'
        }

        try:
            res = requests.request("GET", url, data=payload, headers=headers, params=querystring)
            myjson = json.loads(res.text)
            addr = myjson['data']['country'] + ' ' + myjson['data']['prov'] + ' ' + myjson['data']['city'] + ' ' + myjson['data']['district']

        except Exception as e:
            print('ip获取失败：', ip)
            r.sadd('ip_fail', ip)
            raise e

        ip_ = res.url.split('/')[-1].split('.html')[0]
        print([ip, addr])
        info_f.writerow([ip, addr])


if not os.path.exists('ip_addr.csv'):
    f1 = open('ip_addr.csv', 'a', encoding='utf-8-sig', newline='')
    info_f = csv.writer(f1)
    info_f.writerow(['ip', 'addr'])
else:
    f1 = open('ip_addr.csv', 'a', encoding='utf-8-sig', newline='')
    info_f = csv.writer(f1)


threads = []
for i in range(10):
    t = threading.Thread(target=get_asn)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

