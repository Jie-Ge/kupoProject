# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
爬用户表信息：http://192.168.224.91:16010/master-status
'''
import requests
from fake_useragent import UserAgent
import random
import threading
import xlsxwriter as xw
import os
import openpyxl as xl
from retrying import retry
import time
from lxml import etree

ua = UserAgent()

url = 'http://192.168.224.91:16010/master-status'
start = -20
threadLock = threading.Lock()
fail_url = []
fail_page_url = []
not_img_url_count = 0
duplicated_img_count = 0
save_img_error = []

totol = 0

row_count = 0
totol_count = 0

## 出错时保存 start ，下次启动接着执行
class IconThread(threading.Thread):
    def __init__(self, f):
        threading.Thread.__init__(self)
        self.f = f


    # @retry(stop_max_attempt_number=3)
    def run(self) -> None:
        global start
        global fail_url

        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            self.parse_data(res)

    def parse_data(self, response):
        page = etree.HTML(response.text)

        trs = page.xpath('//*[@id="userTables"]/tbody/tr')
        print('链接总个数：', len(trs))

        for tr in trs:
            href = tr.xpath('./td[2]/a/@href')[0]
            page_url = 'http://192.168.224.91:16010/' + href

            self.request_page(page_url)

    def request_page(self, page_url):
        global totol
        threadLock.acquire()
        totol += 1
        print('当前已爬取个数：', totol)
        threadLock.release()

        count = 3  # 重试次数
        while count > 0:
            headers = {
                'User-Agent': random.choice(ua.data_browsers['chrome'])
            }
            try:
                res = requests.get(page_url, headers=headers, timeout=5)  # 这里可能会报连接超时等错误
            except Exception as e:
                print('imgUrl请求失败！！！')
                if count == 1:
                    fail_page_url.append(page_url)  # 请求3次，均失败，则加入失败队列
                    # 同：traceback.print_exc(e)
                    print(e)

            else:
                if '/busy' in res.url:
                    print('请求过快，等待5秒...')
                    time.sleep(5)
                    continue

                if res.status_code == 200:
                    self.pase_data(res)
                    break
                else:
                    fail_page_url.append(page_url)
                    break
            count -= 1

    def pase_data(self, response):
        global duplicated_img_count
        global save_img_error
        global totol_count

        page = etree.HTML(response.text)

        trs = page.xpath('//*[@id="regionServerDetailsTable"]/tbody/tr')
        if len(trs):
            row_data = ''
            for tr in trs:
                storefile_size = tr.xpath('./td[5]/text()')
                if len(storefile_size):
                    storefile_size = storefile_size[0]
                    # print(storefile_size)
                    if storefile_size == '0 MB':
                        name = tr.xpath('./td[1]/text()')
                        print(name)
                        if len(name):
                            print('error: ', response.url)
                            name = name[0].split('.')[-2]
                            row_data = row_data + name + ' '

                            threadLock.acquire()
                            totol_count += 1
                            threadLock.release()

            if row_data:
                self.save_detail(row_data)

    def save_detail(self, row_data):
        global row_count
        threadLock.acquire()
        self.f.write(row_data)
        row_count += 1
        threadLock.release()



def main():

    f = open('./user_info.txt', 'w')

    threads = []
    for i in range(1):
        t = IconThread(f)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f'请求失败的fail_page_url个数：{len(fail_page_url)}\n', fail_page_url)
    print('总条数：', row_count)
    print('总个数：', totol_count)

    f.close()



if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print('程序结束！！！，用时: ', end_time-start_time)
