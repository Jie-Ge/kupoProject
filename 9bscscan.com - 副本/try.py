# !/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('./contract_all.csv', header=None)
aa = df[0].tolist()  # all url
print(aa)
print(len(aa))

if '0x10ed43c718714eb63d5aa57b78b54704e256024e' in aa:
    print('qweqweqe')
