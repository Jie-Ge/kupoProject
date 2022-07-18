# !/usr/bin/python
# -*- coding: utf-8 -*-
import re

import pandas as pd
import redis
import time

from utils_mysql import select_db_recode, insert_db_recode



df['t3'] = df['付款账号'].str.isdigit()
data3 = df[(df['t3'] == True) & (df['付款账号'].str.len() > 10)]
data3.drop_duplicates('付款账号', inplace=True)

data4 = data3[['image_url', '付款人', '付款账号', '付款银行', '付款账号归属地']]

# data2.rename(columns={'image_url': 'sdsd'}, inplace=True)
data4.columns = ['消息内容', '姓名', '银行卡号', '银行卡号开户行', '银行卡号归属地']
data4['钱包地址'] = ''
# data2 = data2.drop(index=data2[data2['姓名'] == ''].index.tolist())
data4.dropna(subset=['姓名'],  # 指定列
			  axis=0,
			  how='all', # how='all'表示若指定列的值都为空，就删掉该行
			  inplace=True)


data4.insert(1, '发送人IP', '')
data4.insert(2, 'IP归属地', '')

# 防止将 url 存储为超链接（若为超链接，打开xlsx会报错）
duke_writer = pd.ExcelWriter(f'C:/Users/Administrator/Desktop/ok钱包_历史对话_224377_image_赌客.xlsx', engine='xlsxwriter',
                                engine_kwargs={'options': {'strings_to_urls': False}})
data4.to_excel(duke_writer, index=False)
duke_writer.close()