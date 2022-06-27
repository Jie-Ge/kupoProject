# !/usr/bin/python
# -*- coding: utf-8 -*-
import random
import time
import pandas as pd
import requests
from lxml import etree
from fake_useragent import UserAgent
import os
from os import path
import threading
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED
import numpy as np
import redis


ip_asn = []
ips = []
have_ips = []

r = redis.Redis('192.168.224.72', port=6379, db=3, password='123456')


def req_ip(ip):
    url = f'https://www.ip.cn/ip/{ip}.html'

    headers = {
        'user-agent': UserAgent().random,
        'referer': 'https://www.ip.cn/',
        'cookie': '__51cke__=; __51uvsct__1vGn5KEyNxI88WjH=1; __51vcke__1vGn5KEyNxI88WjH=c6ef841d-c3cd-57cb-a772-34895049ea45; __51vuft__1vGn5KEyNxI88WjH=1655787916333; INIT_IP_INFO=%E7%BE%8E%E5%9B%BD++%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9A++; __tins__20765349=%7B%22sid%22%3A%201655787916319%2C%20%22vd%22%3A%204%2C%20%22expires%22%3A%201655789909498%7D; __51laig__=4; __vtins__1vGn5KEyNxI88WjH=%7B%22sid%22%3A%20%2213075f01-8d1c-5365-ae3f-eeac07c96e99%22%2C%20%22vd%22%3A%204%2C%20%22stt%22%3A%20193179%2C%20%22dr%22%3A%20171340%2C%20%22expires%22%3A%201655789909509%2C%20%22ct%22%3A%201655788109509%7D'
    }

    try:
        print('正在请求。。。')
        res = requests.get(url, headers=headers, timeout=10)
    except:
        print('请求失败！！！')
        return ''

    res.encoding = 'utf-8'
    page = etree.HTML(res.text)
    addr_tag = page.xpath('//div[@id="tab0_address"]/text()')
    if addr_tag:
        addr = addr_tag[0]
        print(addr)
    else:
        print('ip获取失败：', ip)
        addr = ''
    return addr

def get_asn(ip):
    '''
    获取 ip 归属地
    '''
    # global ip_asn, ips, have_ips

    if pd.isna(ip):
        return ''

    df_addr = pd.read_csv('ip_addr.csv')
    addr_ = df_addr[df_addr['ip'] == ip]['addr'].tolist()
    if addr_:
        addr = addr_[0]
    else:
        addr = req_ip(ip)
    return addr


def func(a, b):
    if a != b:
        return a
    else:
        return np.nan


def get_image_url(abs_path):
    print(abs_path)
    df = pd.read_excel(abs_path)

    print('处理ip归属地......')
    # 处理ip归属地
    df['归属地'] = df[['发送人IP']].apply(lambda x: get_asn(x.发送人IP), axis=1)

    if not os.path.exists(f'./情报数据《金沙彩票》'):
        os.mkdir(f'./情报数据《金沙彩票》')

    save_path = "./情报数据《金沙彩票》/{}".format(abs_path.split('/')[-1])
    df.to_excel(save_path, index=False)


def scaner_file(url):
    file = os.listdir(url)
    for f in file:
        real_url = path.join(url, f)
        if path.isfile(real_url):
            # 如果是文件，则以绝度路径的方式输出
            abs_url = path.abspath(real_url)
            if '2022-03-20_2022-04-01_1654676858_0.xlsx' in abs_url:
                continue
            get_image_url(abs_url)
        elif path.isdir(real_url):
            # 如果是目录，则是递归调用自定义函数 scaner_file (url)进行多次
            scaner_file(real_url)
        else:
            print("其他情况")
            pass


ll = [
    # 'C:/Users/Administrator/Desktop/情报数据《84棋牌》/test.xlsx',
    'C:/Users/Administrator/Desktop/情报数据《金沙彩票》'
      ]
for p in ll:
    scaner_file(p)



# while True:
#
#     get_asn('220.196.60.17')
#     # time.sleep(random.random())
#     # break