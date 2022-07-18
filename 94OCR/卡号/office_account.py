# !/usr/bin/python
# -*- coding: utf-8 -*-
import re

import pandas as pd
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

engine = create_engine('mysql://root:12345678@192.168.224.49:33060/spider')
conn = engine.connect()

df1 = pd.read_sql_table('澳门永利娱乐城_chat_info_01', conn)
print(df1)

df = df1[pd.isna(df1['发送人IP'])]
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

df = df[pd.notna(df['卡号'])]

# 防止将 url 存储为超链接（若为超链接，打开xlsx会报错）
writer = pd.ExcelWriter('平台/金沙彩票_银行卡号_平台.xlsx', engine='xlsxwriter',  engine_kwargs={'options': {'strings_to_urls': False}})
df.to_excel(writer, index=False)
writer.close()