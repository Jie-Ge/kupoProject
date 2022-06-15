# !/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from fake_useragent import UserAgent
import re
import json
from aliyun_ocr_sdk import Sample
import sys
import os
from os import path
import pandas as pd
import time


def get_asn():
    '''
    获取 ip 归属地
    '''
    params_ip = {
        'ip': '183.46.107.2',
        'action': 2
    }

    headers = {
        'User-Agent': UserAgent().random
    }

    url_ip = 'https://www.ip138.com/iplookup.asp'

    res = requests.get(url_ip, params=params_ip, headers=headers)
    res.encoding = 'gbk'

    cmp = re.compile('var ip_result = (.*?);')
    string = cmp.search(res.text).group(1)
    # print(type(string))

    json_data = json.loads(string)
    asn = json_data['ip_c_list'][0]['ct'] + ' ' + json_data['ip_c_list'][0]['prov']
    print(asn)


def ocr(image_list):
    '''
    收款方 、收款银行、收款卡号
    '收款方 请联系XXXX'
    :return:
    '''

    # url = 'https://legacy-pics.meiqiausercontent.com/images/347754/krnw/cnOcoHOkNT8jSQIW6dPx.jpg'
    # url = 'https://legacy-pics.meiqiausercontent.com/images/347754/85w5/aN9yz4eTVmj5r269p4eC.jpg'
    # url = 'https://legacy-pics.meiqiausercontent.com/images/347754/JnfU/knO6dBLZYhaaRGf4qZOw.jpg'
    for url in image_list:
        aa = Sample.main(url)
        print(aa)
        time.sleep(0.2)


def get_image_url(abs_path):
    df = pd.read_excel(abs_path)
    image_df = df[df['消息内容'].str.startswith('http') & df['消息内容'].str.match('.*\.(jpg|png)')]
    image_list = image_df['消息内容'].tolist()
    ocr(image_list)


def scaner_file(url):
    '''
    遍历文件夹中的文件
    '''
    file = os.listdir(url)
    for f in file:
        real_url = path.join(url, f)
        if path.isfile(real_url):
            # 如果是文件，则以绝度路径的方式输出
            abs_path = path.abspath(real_url)
            print(abs_path)
            get_image_url(abs_path)
        elif path.isdir(real_url):
            # 如果是目录，则是递归调用自定义函数 scaner_file (url)进行多次
            scaner_file(real_url)
        else:
            print("其他情况")
            pass


def main():
    ll = ['C:/Users/Administrator/Desktop/情报数据《金沙彩票》',
          'C:/Users/Administrator/Desktop/情报数据《84棋牌》',
          'C:/Users/Administrator/Desktop/情报数据《668娱乐》']
    for p in ll:
        scaner_file(p)


if __name__ == '__main__':
    main()


