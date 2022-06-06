# !/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import threading
import requests
from fake_useragent import UserAgent
import random
from lxml import etree
import csv
import time
import queue
from retrying import retry

domain = 'https://etherscan.io/address/'

threadLock = threading.Lock()
ua = UserAgent()


class ThreadCrawl(threading.Thread):
    def __init__(self, threadID, addr_list, url_queue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.addr_list = addr_list
        self.url_queue = url_queue

    def run(self) -> None:
        while not self.url_queue.empty():
            num = self.url_queue.get()
            # num += 7435
            addr = self.addr_list[num]
            url = domain + addr
            self.get_html(url, num)
            time.sleep(2+random.random())

    @retry(stop_max_attempt_number=3)
    def get_html(self, url, num):
        ua_list = ua.data_browsers['chrome']
        useragent = random.choice(ua_list)
        headers = {
            'user-agent': useragent
        }
        res = requests.get(url, headers=headers, timeout=5)
        print(f'正在获取第 {num} 个url', res.status_code)
        if res.status_code == 200:
            self.parse(res)

    def parse(self, res):

        page = etree.HTML(res.text)
        span_tabs = page.xpath('(//div[contains(@class, "card-header")])[1]//span[@data-toggle="tooltip"]')
        label = ''
        if len(span_tabs):
            label = span_tabs[0].xpath('./text()')
            if len(label):
                label = label[0].split(':')[0]
                print(label)
        else:
            title = page.xpath('//title/text()')
            if len(title):
                label = title[0].split(' ')[0]
                label = label.replace('\r\n\t', '').replace(':', '')
                print(label)

        self.save(res.url, label)

    def save(self, url, label):
        if '/address/' in url:
            threadLock.acquire()
            with open('./label2.csv', 'a', encoding='utf=8', newline='') as f:
                csv_f = csv.writer(f)
                print([url, label])
                csv_f.writerow([url, label])
                print('save !!!! ')
            threadLock.release()


def read_file():
    df = pd.read_csv('C:/Users/Administrator/Desktop/eth_rqb_manual_labelled.csv')
    print(df)
    addr_list = df['address'].tolist()[:5]

    url_queue = queue.Queue(len(addr_list))
    print(len(addr_list))
    for i in range(len(addr_list)):
        url_queue.put(i)

    return addr_list, url_queue


def again_request():
    '''
    爬取请求失效的或者遗漏的url
    :return: 请求失效的或者遗漏的地址
    '''

    ## 对当前爬取结果进行去重
    df = pd.read_csv('label.csv')
    # print(df['address'].duplicated().tolist())  查看address是否有重复
    df_dup = df.drop_duplicates(subset=['address'], keep='first').reset_index(drop=True)
    # df_dup.to_csv('./filename.csv', index=False, encoding='utf-8')  # 保存数据，不保存索引
    print(df_dup['address'])
    addr = df_dup['address'].tolist()

    ## 对比原待爬取url，检查遗漏了哪些url
    source_df = pd.read_csv('C:/Users/Administrator/Desktop/eth_rqb_manual_labelled.csv')
    s_addr = source_df['address'].tolist()
    again_addr = [i for i in s_addr if domain+i not in addr]
    print('请求失效的或者遗漏的url数量：', len(again_addr))

    return again_addr


def main():

    addr_list, url_queue = read_file()

    threads = []
    for i in range(1):
        t = ThreadCrawl(i, addr_list, url_queue)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    # 爬取请求失效的或者遗漏的url
    # 这里注意，如果一直有未请求成功的url，就会一直循环下去
    again_addr = again_request()
    while len(again_addr):
        main()


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()

    print('程序结束, 用时：%s' % (end_time-start_time))

