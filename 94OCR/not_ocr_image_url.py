# !/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import redis
import pymysql
import threading

conn = pymysql.connect(
    host='192.168.224.49',
    port=33060,
    user='root',
    password='12345678',
    database='spider'
)

cursor = conn.cursor()

sql = 'select image_url from jinsha_chat_image_info_01'
cursor.execute(sql)
result = cursor.fetchall()
have_image_url = []
for item in result:
    have_image_url.append(item[0])


r = redis.Redis(host='192.168.224.72', port=6379, password='123456', db=3, decode_responses=True)
all_image_url = r.smembers('all_image_url')

not_image_url = list(all_image_url.difference(have_image_url))
print(not_image_url)
print(len(not_image_url))


count = 0
def main():
    global count
    while not_image_url:
        url = not_image_url.pop()
        count += 1
        print(count)
        r.sadd('not_image_url', url)


if __name__ == '__main__':

    threads = []
    for i in range(20):
        t = threading.Thread(target=main)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
