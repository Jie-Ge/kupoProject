# !/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from aliyun_ocr_sdk import Sample
import json

df = pd.read_excel(r'C:\Users\Administrator\Desktop\情报数据《金沙彩票》\support-sys-历史对话_347754_2022-03-20_2022-04-01_1654676851\support-sys-历史对话347754_2022-03-20_2022-04-01_1654676858_0.xlsx')

aa = df[df['消息内容'].str.startswith('http') & df['消息内容'].str.match('.*\.(jpg|png)')]
image_list = aa['消息内容'].tolist()

for url in image_list:
    print(url)
    response = Sample.main(url)
    # print(response)
    # print(type(response))

    requestId = response.body
    print(requestId)
    break
    # ('LTAI5tG4fVJNT4ctiBJTi8hT', 'o9UleXtBjhBC49AWCS4aVNXNjg4ilB')