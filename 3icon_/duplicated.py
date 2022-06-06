# !/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_excel('./icon2_data/token_detail1.xlsx', sheet_name='sheet1')
data = df.drop_duplicates(['Contract'], keep='first').reset_index(drop=True)
print(data)

# 防止将 url 存储为超链接（若为超链接，代开xlsx会报错）
writer = pd.ExcelWriter(r'./icon2_data/token_detail.xlsx', engine='xlsxwriter', options={'strings_to_urls':False})

data.to_excel(writer, index=False)

writer.close()