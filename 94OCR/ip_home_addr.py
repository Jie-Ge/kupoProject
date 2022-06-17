# !/usr/bin/python
# -*- coding: utf-8 -*-
import random
import time
import pandas as pd
import requests


def get_asn(ip):
    '''
    获取 ip 归属地
    '''

    if pd.isna(ip):
        return ''

    # params_ip = {
    #     'ip': ip,
    #     'action': 2
    # }
    #
    # headers = {
    #     'User-Agent': UserAgent().random
    # }
    #
    # url_ip = 'https://www.ip138.com/iplookup.asp'
    #
    # res = requests.get(url_ip, params=params_ip, headers=headers)
    # res.encoding = 'gbk'
    # print(res.text)
    # print(res.status_code)
    # print(ip)
    # cmp = re.compile('var ip_result = (.*?);')
    # string = cmp.search(res.text).group(1)
    # # print(type(string))
    #
    # json_data = json.loads(string)
    # asn = json_data['ip_c_list'][0]['ct'] + ' ' + json_data['ip_c_list'][0]['prov']

    url = 'https://tool.lu/ip/ajax.html'

    data = {
        'ip': ip
    }

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'cookie': 'Hm_lvt_0fba23df1ee7ec49af558fb29456f532=1655349947; uuid=26da444d-dead-4c1a-b071-37f8035e3b8a; _session={"slim.flash":[]}; Hm_lpvt_0fba23df1ee7ec49af558fb29456f532=1655357134; _access=46a906a492c4354b4740fd994f56a256ecdbfae61ed97dc231c311668153712d',
        'origin': 'https://tool.lu',
        'referer': 'https://tool.lu/ip/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9'
    }

    res = requests.post(url, data=data, headers=headers).json()
    print(res)
    asn = res['text']['chunzhen']


    time.sleep(random.random())
    return asn