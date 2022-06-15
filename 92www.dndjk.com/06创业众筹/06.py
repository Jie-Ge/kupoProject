# !/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import etree
import csv


data = []
keys_list = []
with open(f'./06funding.html', 'r', encoding='utf-8') as f:
    html = f.read()

page = etree.HTML(html)
trs = page.xpath('//div[@class="card mt-3"]//tbody/tr')

for tr in trs:
    item = {}
    item['名称'] = tr.xpath('./td[1]/text()')[0].replace('\t', '').replace('\n', '').replace(' ', '')
    item['类目'] = tr.xpath('./td[3]//text()')[0].replace('\t', '').replace('\n', '').replace(' ', '')
    item['状态'] = tr.xpath('./td[4]//text()')[1].replace('\t', '').replace('\n', '').replace(' ', '')
    item['发起人'] = tr.xpath('./td[5]/text()')[0].replace('\t', '').replace('\n', '').replace(' ', '')
    item['目标金额'] = tr.xpath('./td[6]//text()')[0].replace('\t', '').replace('\n', '').replace(' ', '')
    item['当前金额'] = tr.xpath('./td[7]//text()')[0].replace('\t', '').replace('\n', '').replace(' ', '')
    item['参与人数'] = tr.xpath('./td[8]/text()')[0].replace('\t', '').replace('\n', '').replace(' ', '')
    item['参与次数'] = tr.xpath('./td[9]/text()')[0].replace('\t', '').replace('\n', '').replace(' ', '')
    item['到期时间'] = tr.xpath('./td[10]/text()')[0].replace('\t', '').replace('\n', '').replace(' ', '')

    keys_list = list(item.keys())
    print(item)
    data.append(item)

with open('./创业众筹.csv', 'a', encoding='utf-8-sig', newline='') as f:
    csv_f = csv.DictWriter(f, keys_list)
    csv_f.writeheader()
    csv_f.writerows(data)
