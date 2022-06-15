# !/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import etree
import csv

num = 1
data = []
keys_list = []
while num <= 18:
    print('num ', num)
    with open(f'./03file/03page{num}.html', 'r', encoding='utf-8') as f:
        html = f.read()

    page = etree.HTML(html)
    trs = page.xpath('//div[@class="card"]//tbody/tr')

    for tr in trs:
        item = {}
        item['用户'] = tr.xpath('./td[2]/div[1]/text()')[0]
        item['账号'] = tr.xpath('./td[2]/div[2]/text()')[0]
        item['总算力'] = tr.xpath('./td[3]/text()')[0]
        item['团队算力'] = tr.xpath('./td[4]/text()')[0]
        item['矿机算力'] = tr.xpath('./td[5]//text()')[0]
        item['团队人数'] = tr.xpath('./td[6]//text()')[0]
        item['矿机数量'] = tr.xpath('./td[7]/text()')[0]
        item['过期矿机'] = tr.xpath('./td[8]/text()')[0]

        keys_list = list(item.keys())
        print(item)
        data.append(item)
    num += 1

with open('./仪表盘.csv', 'a', encoding='utf-8-sig', newline='') as f:
    csv_f = csv.DictWriter(f, keys_list)
    csv_f.writeheader()
    csv_f.writerows(data)
