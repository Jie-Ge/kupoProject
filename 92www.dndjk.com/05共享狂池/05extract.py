# !/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import etree
import csv


data = []
keys_list = []
with open(f'./05pool.html', 'r', encoding='utf-8') as f:
    html = f.read()

page = etree.HTML(html)
trs = page.xpath('//div[@class="card"]//tbody/tr')

for tr in trs:
    item = {}
    item['用户'] = tr.xpath('./td[1]/text()')[0].replace('\t', '').replace('\n', '')
    item['操作'] = tr.xpath('./td[2]/text()')[0].replace('\t', '').replace('\n', '')
    item['当前算力'] = tr.xpath('./td[3]/text()')[0].replace('\t', '').replace('\n', '')
    item['消费货币'] = tr.xpath('./td[4]/text()')[0].replace('\t', '').replace('\n', '')
    item['道具名称'] = tr.xpath('./td[5]//text()')[0].replace('\t', '').replace('\n', '')
    item['奖励算力'] = tr.xpath('./td[6]//text()')[0].replace('\t', '').replace('\n', '')
    item['奖励货币'] = tr.xpath('./td[7]/text()')[0].replace('\t', '').replace('\n', '')
    item['时间'] = tr.xpath('./td[8]/text()')[0].replace('\t', '').replace('\n', '')

    keys_list = list(item.keys())
    print(item)
    data.append(item)

with open('./共享矿池.csv', 'a', encoding='utf-8-sig', newline='') as f:
    csv_f = csv.DictWriter(f, keys_list)
    csv_f.writeheader()
    csv_f.writerows(data)
