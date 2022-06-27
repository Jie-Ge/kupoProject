# !/usr/bin/python
# -*- coding: utf-8 -*-
from functools import reduce

import pandas as pd
from pyparsing import col
import re

df = pd.read_csv('C:/Users/Administrator/Desktop/bbbb.csv')
print(df)


def account(content):
    cmp = re.compile('([0-9]{16,19})')
    sear = cmp.search(content)
    if sear:
        return sear.group(1)
    else:
        return ''


def replace_info(content):
    cmp = re.compile('\(.*?\)|（.*?）|《.*?》|（每次.*?谢谢|（每次.*?不负责')
    new_content = cmp.sub('', content)
    return new_content


df['卡号'] = df[['消息内容']].apply(lambda x: account(x.消息内容), axis=1)
df['消息内容'] = df[['消息内容']].apply(lambda x: replace_info(x.消息内容), axis=1)

df = df.drop_duplicates(['卡号'])

df.to_excel('cccccc.xlsx', index=False, encoding='utf-8')