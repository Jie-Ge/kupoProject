# !/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import etree
import csv

num = 1
data = []
keys_list = []
while num <= 18:
    print('num ', num)
    with open(f'./02file/02page{num}.html', 'r', encoding='utf-8') as f:
        html = f.read()

    page = etree.HTML(html)
    trs = page.xpath('//div[@class="card"]//tbody/tr')

    for tr in trs:
        item = {}
        item['用户'] = tr.xpath('./td[2]/div[1]/text()')[0]
        item['账号'] = tr.xpath('./td[2]/div[2]/text()')[0]
        item['一代'] = tr.xpath('./td[3]/text()')[0]
        item['二代'] = tr.xpath('./td[4]/text()')[0]
        item['三代'] = tr.xpath('./td[5]//text()')[0]
        item['四代'] = tr.xpath('./td[6]//text()')[0]
        item['五代'] = tr.xpath('./td[7]/text()')[0]
        item['六代'] = tr.xpath('./td[8]/text()')[0]
        item['七代'] = tr.xpath('./td[9]/text()')[0]
        item['八代'] = tr.xpath('./td[10]/text()')[0]
        item['Lv0'] = tr.xpath('./td[11]/text()')[0]
        item['Lv1'] = tr.xpath('./td[12]/text()')[0]
        item['Lv2'] = tr.xpath('./td[13]/text()')[0]
        item['Lv3'] = tr.xpath('./td[14]/text()')[0]
        item['Lv4'] = tr.xpath('./td[15]/text()')[0]
        item['Lv5'] = tr.xpath('./td[16]/text()')[0]
        item['Lv6'] = tr.xpath('./td[17]/text()')[0]
        item['Lv7'] = tr.xpath('./td[18]/text()')[0]
        item['Lv8'] = tr.xpath('./td[19]/text()')[0]

        keys_list = list(item.keys())
        print(item)
        data.append(item)
    num += 1

with open('./推广数据.csv', 'a', encoding='utf-8-sig', newline='') as f:
    csv_f = csv.DictWriter(f, keys_list)
    csv_f.writeheader()
    csv_f.writerows(data)
