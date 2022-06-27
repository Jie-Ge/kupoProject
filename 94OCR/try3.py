# !/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd

ips = ['112.83.0.201', '153.101.231.119', '58.241.114.36', '114.98.224.221']

df = pd.read_excel('all_files.xlsx')
# df = pd.read_excel('C:/Users/Administrator/Desktop/情报数据《金沙彩票》/support-sys-历史对话_347754_2022-03-20_2022-04-01_1654676851/support-sys-历史对话347754_2022-03-20_2022-04-01_1654676858_0.xlsx')
print(df)

df22 = pd.DataFrame()
for ip in ips:
    id_ = df[df['发送人IP'] == ip]['对话id'].tolist()
    if id_:
        df11 = df[df['对话id'] == id_[0]]
        df22 = df22.append(df11)

df22.to_excel('./asaasaa.xlsx', index=False)
