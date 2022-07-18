# !/usr/bin/python
# -*- coding: utf-8 -*-
import threading

import redis
import pandas as pd
import time
from sqlalchemy import create_engine, types
import pymysql
pymysql.install_as_MySQLdb()  # 必须

r = redis.Redis('192.168.224.72', port=6379, db=15, password='123456')

image_urls = []
def put_image_url():
    global image_urls
    while image_urls:
        print('剩余待入库image_urls：', len(image_urls))
        url = image_urls.pop()
        r.sadd('image_url', url)


def image_url_thread(urls):
    global image_urls
    image_urls = urls
    threads = []
    for i in range(30):
        t = threading.Thread(target=put_image_url)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


def get_image_url(table_name):
    global image_urls
    engine = create_engine("mysql://root:12345678@192.168.224.49:33060/spider", echo=True)
    conn = engine.connect()

    sql = f"select `消息内容` from `{table_name}` where (`消息内容` regexp '^http.*?(jpg|png)$') and (`发送人IP` is not null)"
    results = conn.execute(sql)
    for result in results:
        image_urls.append(result[0])
    image_url_thread(image_urls)
    conn.close()


if __name__ == '__main__':
    s = time.time()
    get_image_url('668娱乐_chat_info_01')
    print(time.time()-s)