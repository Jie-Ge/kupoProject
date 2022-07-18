# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
名字的全称和简称分开存，若没有简称则用全称替代，将英文,替换为中文，
为空的用 ’NAN‘ 占位
换行符、空格、制表符
"""
import requests
from lxml import etree
from fake_useragent import UserAgent

headers = {
    'user-agent': UserAgent().random
}
import pandas as pd
pd.read_csv(r'D:\Downloads\bsc_address.csv', header=None)
def parse_html():
    address = 'NAN'
    full_title = 'NAN'
    short_title = 'NAN'
    divSummary1 = 'NAN'
    divSummary2 = 'NAN'


    url = 'https://bscscan.com/address/0x569297f97110d0ec06606bb16fbb7d1d25298120'
    res = requests.get(url, headers=headers)
    page = etree.HTML(res.text)
    address_tag = page.xpath('//span[@id="mainaddress"]/text()')
    if address_tag:
        address = address_tag[0]

    tokeninfo_tag = page.xpath('//div[@id="ContentPlaceHolder1_tr_tokeninfo"]//a/text()')
    if tokeninfo_tag:
        tokeninfo = tokeninfo_tag[0].replace(',', '，').split(' ')
        full_title = tokeninfo[0]
        if len(tokeninfo) == 2:
            short_title = tokeninfo[1].replace('(', '').replace(')', '')
        else:
            short_title = full_title

    divSummary1_tag = page.xpath('//div[@id="ContentPlaceHolder1_divSummary"]/div[@class="row mb-4"]')
    if divSummary1_tag:
        divSummary1 = etree.tostring(divSummary1_tag[0], encoding='utf-8').decode()

    divSummary2_tag = page.xpath('//div[@id="ContentPlaceHolder1_divSummary"]/div[@class="card"]')
    if divSummary2_tag:
        divSummary2 = etree.tostring(divSummary2_tag[0], encoding='utf-8').decode()

    print(address)
    print(full_title)
    print(short_title)
    print(divSummary1)
    print('divSummary2: ', divSummary2)

parse_html()



'''
Contract
Title
Tag
Icon_href
Decimals
Official_Site
Social_Profiles
token_html

'''