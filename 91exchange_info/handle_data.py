# !/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

# df = pd.read_sql_table('all_name_website', "mysql://root:12345678@192.168.224.49:33060/exchanges")

engine = create_engine("mysql://root:12345678@192.168.224.49:33060/exchanges", echo=True)
conn = engine.connect()
table_name = 'all_name_website'
df = pd.read_sql_table(table_name, conn)
print(df)


def handle(website):
    if website.startswith('http'):
        return website.split('/')[2]
    else:
        return website


# print(type(df[['official_website']]))  # DataFrame
# print(type(df['official_website']))  # Series

# df['handled_website'] = [x.split('/')[2] if x.startswith('http') else x for x in df['official_website']]
df['handled_website'] = df[['official_website']].apply(lambda x: handle(x.official_website), axis=1)
print(df)

df.drop_duplicates('handled_website', inplace=True)
df.drop_duplicates('name', inplace=True)

print(df)