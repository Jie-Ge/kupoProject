# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
爬取：https://coinmarketcap.com/

此网站大概可以开启8线程（加了速度限制）
开启10线程，大概2000个请求就被封
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

page_num = 80
url_num = 0  # url计数，用于显示进度
total_page = 102  # 102
fail_page_url = []
fail_list_page = []
threadLock = threading.Lock()
coin_info = []
count = 0

page_queue = Queue(10300)


class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)  # 在自写的类中的init中需要先初始化Thread
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
        }

    def run(self):
        url = 'https://coinmarketcap.com/'
        global page_num
        while page_num < total_page:
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'user-agent': random.choice(ua.data_browsers['chrome']),
                'referer': 'https: //coinmarketcap.com/',
                'sec-ch-ua-platform': '"Windows"'
            }
            page_num += 1
            params = {
                'page': page_num
            }
            print(f'正在请求第 {page_num} 个列表页...')
            try:
                res = requests.get(url, headers=headers, params=params, timeout=10)
            except Exception as e:
                print('列表页请求失败，页码为：', page_num)
                fail_list_page.append(page_num)
                print(e)
            else:
                if '/busy' in res.url:
                    print('列表页请求失败，页码为：', page_num)
                    fail_list_page.append(page_num)
                    continue
                if res.status_code == 200:
                    self.parse_page_url(res)
                else:
                    print('list page请求失败，状态码：', res.status_code)
                    return None

            time.sleep(1.3)

    def parse_page_url(self, response):
        page = etree.HTML(response.text)
        tr_tags = page.xpath("//table[contains(@class, 'cmc-table')]/tbody/tr")

        if len(tr_tags):
            for h3_tag in tr_tags:
                href = h3_tag.xpath('./td[3]//a[@class="cmc-link"]/@href')
                if len(href):
                    page_href = href[0]
                    page_queue.put(page_href)
        else:
            print('列表页请求失败，页码为：', page_num)
            fail_list_page.append(page_num)


class Icon2Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global url_num
        while not page_queue.empty():
            url_num += 1
            # if url_num == 20:
            #     raise
            print(f'正在请求第 {url_num}/10200 个url：', threading.active_count())

            url = page_queue.get(block=False)
            url = 'https://coinmarketcap.com' + url
            count = 3  # 重试次数
            while count > 0:
                headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'referer': 'https: //coinmarketcap.com/',
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
                        self.parse_data(res)
                        break

                    else:
                        print('detail page请求失败，状态码：', res.status_code)
                        return None
                count -= 1

            time.sleep(2.4)


    def parse_data(self, response):
        desc = ''
        name = ''

        page = etree.HTML(response.text)
        h2 = page.xpath('//h2[@class="sc-1q9q90x-0 jCInrl h1"]/text()')
        if len(h2):
            name = h2[0]
        else:
            print('请求到的不是正常的detail page')
            fail_page_url.append(response.url)
            return None

        cmp = re.compile('<div class="sc-16r8icm-0 kjciSH contentClosed hasShadow.*?(<div class="sc-2qtjgt-0 eApVPN">.*?)</div><div class="sc-101ku0o-2 exKUGw">', re.S)

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
    threads1 = []
    for i in range(5):
        t = Producer()
        t.start()
        threads1.append(t)

    for t in threads1:
        t.join()

    print('detail page 数量：', page_queue.qsize())

    threads2 = []
    for i in range(5):
        t = Icon2Thread()
        t.start()
        threads2.append(t)

    for t in threads2:
        t.join()

    with open('coin_desc1.json', 'a', encoding="utf8") as file_object:
        json.dump(coin_info, file_object)

    print(f'{len(fail_list_page)}个list url请求失败：', fail_list_page)
    print(f'{len(fail_page_url)}个page url请求失败：', fail_page_url)


if __name__ == '__main__':

    s = time.time()
    main()
    print('耗时：', time.time()-s)