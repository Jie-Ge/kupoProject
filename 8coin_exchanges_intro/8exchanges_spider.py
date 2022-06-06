# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
爬取：https://www.mifengcha.com/ 的币种简介

'''

import threading
import time
import requests
from fake_useragent import UserAgent
import random
from lxml import etree
import re
import json
from queue import Queue

ua = UserAgent()

page_num = 0
url_num = 0  # url计数，用于显示进度
total_page = 457  # 102
fail_page_url = []
fail_list_page = []
threadLock = threading.Lock()
coin_info = []
count = 0
detail_info = []

page_queue = Queue(600)


class Icon2Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while not page_queue.empty():
            item = page_queue.get(block=False)

            global url_num
            url_num += 1
            # if url_num > 10:
            #     return None
            print(f'正在请求第 {url_num}/504 个url：', threading.active_count())

            url = f'https://www.mifengcha.com/exchange/{item["name"]}'
            count = 3  # 重试次数
            while count > 0:
                headers = {
                    'referer': 'https://www.mifengcha.com/',
                    'user-agent': random.choice(ua.data_browsers['chrome'])
                }
                try:
                    res = requests.get(url, headers=headers, timeout=10)
                except Exception as e:

                    if count == 1:
                        print('3次请求均失败！！！')
                        fail_page_url.append(url)  # 请求3次，均失败，则加入失败队列
                        # 同：traceback.print_exc(e)
                        print(e)
                    else:
                        print('请求失败，等待一会儿，再重试！！！')
                        time.sleep(5.5)

                else:
                    if '/busy' in res.url:
                        print('请求过快，等待5秒...')
                        time.sleep(5)
                        count -= 1
                        continue

                    if res.status_code == 200:
                        self.parse_data(res, item['name'])
                        break

                    else:
                        print('detail page请求失败，状态码：', res.status_code)
                        return None
                count -= 1

            time.sleep(2.4)

    def parse_data(self, response, name):
        desc = ''

        page = etree.HTML(response.text)
        div = page.xpath('//div[@class="exchange-info"]')
        if not len(div):
            print('请求到的不是正常的detail page')
            fail_page_url.append(response.url)
            return None

        cmp = re.compile('<div class="description".*?(<p.*?</p>)', re.S)

        have_search = cmp.search(response.text)
        if have_search:
            desc = have_search.group(1)
        else:
            print('请求到的不是正常的detail page')
            fail_page_url.append(response.url)
            return None

        # 替换 a 标签
        text_list = re.findall('<a.*?>(.*?)</a>', desc, re.S)
        a_tags = re.findall('<a.*?>.*?</a>', desc, re.S)

        if len(text_list) and len(text_list) == len(a_tags):
            for (a_tag, text) in zip(a_tags, text_list):
                desc = desc.replace(a_tag, text)

        desc = desc.replace('&#x27;', "'")

        print({'name': name, 'url': response.url})

        coin_info.append({'name': name, 'url': response.url, 'desc': desc})
        global count
        count += 1
        print('保存到的数据条数：', count)


def main():
    url = 'https://www.mifengcha.com/api/v1/quick_search/exchange'
    headers = {
        'user-agent': random.choice(ua.data_browsers['chrome']),
        'referer': 'https://www.mifengcha.com/'
    }
    params = {
        't': '79bcbabec04fa4c313fc65fd8ff0407f',
        'lan': 'zh'
    }
    print(f'正在请求列表页...')
    res = requests.get(url, headers=headers, params=params, timeout=10)
    if res.status_code == 200:
        data_json = res.json()
        for item in data_json['data']:
            page_queue.put({'name': item['name']})

    else:
        print('list page请求失败，状态码：', res.status_code)
        return None

    print(f'共 {page_queue.qsize()} 个detail url')

    threads2 = []
    for i in range(5):
        t = Icon2Thread()
        t.start()
        threads2.append(t)

    for t in threads2:
        t.join()

    with open('exchanges_desc1.json', 'w', encoding="utf-8") as file_object:
        json.dump(coin_info, file_object, ensure_ascii=False)

    print(f'{len(fail_list_page)}个list url请求失败：', fail_list_page)
    print(f'{len(fail_page_url)}个page url请求失败：', fail_page_url)


if __name__ == '__main__':

    s = time.time()
    main()
    print('耗时：', time.time()-s)