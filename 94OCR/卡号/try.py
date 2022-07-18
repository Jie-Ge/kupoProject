# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  try.py
@Time    :  2022/6/27 17:45
@Author  :  JayYoung
@Version :  1.0
@Python  :  Python3.7
@License :  (C)Copyright 2019-2020
@Desc    :  None
"""

import pandas as pd
df = pd.read_excel('赌客/澳门永利娱乐城赌客银行卡号(去重).xlsx')
print(df)
df = df[pd.notna(df['卡号'])]
print(df)
df.to_excel('aaaa.xlsx', index=False, encoding='utf-8')