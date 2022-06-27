# !/usr/bin/python
# -*- coding: utf-8 -*-


import os
from os import path
import pandas as pd
import redis
from sqlalchemy import create_engine, VARCHAR
import pymysql
pymysql.install_as_MySQLdb()

engine = create_engine("mysql://root:12345678@192.168.224.49:33060/spider", echo=True)
conn = engine.connect()


total_df = pd.DataFrame()
def open_file(abs_url):
    global total_df
    df = pd.read_excel(abs_url)
    total_df = total_df.append(df)


def scaner_file(url):
    file = os.listdir(url)
    for f in file:
        real_url = path.join(url, f)
        if path.isfile(real_url):
            # 如果是文件，则以绝度路径的方式输出
            abs_url = path.abspath(real_url)
            print(abs_url)
            open_file(abs_url)
        elif path.isdir(real_url):
            # 如果是目录，则是递归调用自定义函数 scaner_file (url)进行多次
            scaner_file(real_url)
        else:
            print("其他情况")
            pass


ll = [
    'C:/Users/Administrator/Desktop/ok钱包/eid=44249fe129595d3c369acf0f9abcd746/support-sys-历史对话_224377_2022-03-01_2022-04-01_1655291377'
]
for p in ll:
    scaner_file(p)


total_df.to_sql(name="ok钱包_chat_info_01", if_exists='append', con=conn, index=False)