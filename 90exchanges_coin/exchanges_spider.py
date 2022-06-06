# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    :  2022/6/6 10:49
@Author  :  JayYoung
@Python  :  Python3.7
@Desc    :  https://coinmarketcap.com/rankings/exchanges/
"""


import requests
from lxml import etree
import json
import pandas as pd


def save_img(content, name):
    try:
        with open(f'./exchanges_icon/{name}.png', 'wb') as f:
            f.write(content)
        return True
    except:
        print('img 保存失败！！！')


def req_img(id_, name):

    url = f'https://s2.coinmarketcap.com/static/img/exchanges/64x64/{id_}.png'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        print('img请求成功，url:', res.url)
        if save_img(res.content, name):
            return True
    else:
        print(f'{name} 请求失败：', res.url)


def req_detail(name):
    url = f'https://coinmarketcap.com/exchanges/{name.lower()}/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    page = etree.HTML(res.text)
    img_tag = page.xpath('//div[@class="sc-16r8icm-0 escjiH"]/img/@src')
    if img_tag:
        id_ = img_tag[0].split('/')[-1]
        id_ = id_.split('.')[0]
        print('id_: ', id_)
        return req_img(id_, name)


def req_html():
    url = 'https://coinmarketcap.com/rankings/exchanges/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    res = requests.get(url, headers=headers)
    page = etree.HTML(res.text)
    json_string = page.xpath('//script[@id="__NEXT_DATA__"]/text()')[0]

    json_data = json.loads(json_string)

    exchanges_list = json_data['props']['pageProps']['exchange']

    df = pd.read_csv('./LABEL_DICTIONARY_202206021630.csv')
    old_label_names = df['LABEL_NAME'].tolist()
    # old_label_names = list(map(lambda x: x.lower(), old_label_names))

    label_icon = []

    temp_dic = {}
    for item in exchanges_list:
        id_ = item['id']
        name = item['name'].lower()
        temp_dic[name] = id_

    print(temp_dic)
    print('temp_dic: ', len(temp_dic))

    count = 0
    for name in old_label_names:
        if name.lower() in temp_dic.keys():
            count += 1
            print('count: ', count)
            if req_img(temp_dic[name.lower()], name):
                label_icon.append(f'/labelicon/second/{name}.png')
            else:
                label_icon.append('')
        else:
            if req_detail(name):
                label_icon.append(f'/labelicon/second/{name}.png')
            else:
                label_icon.append('')

    df['LABEL_ICON'] = label_icon
    print(df)
    df.to_csv('./exchange_icon_info1.csv')


if __name__ == '__main__':
    req_html()


