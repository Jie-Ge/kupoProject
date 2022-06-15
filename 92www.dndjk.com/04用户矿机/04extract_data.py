# !/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import etree
import csv

num = 1
data = []
keys_list = []
while num <= 10:
    print('num ', num)
    with open(f'./04file/04page{num}.html', 'r', encoding='utf-8') as f:
        html = f.read()

    page = etree.HTML(html)
    trs = page.xpath('//div[@class="card"]//tbody/tr')

    count = 0
    for tr in trs:
        count += 1
        print('count ', count)
        item = {}
        item['用户'] = tr.xpath('./td[1]/div[1]/text()')[0]
        item['账号'] = tr.xpath('./td[1]/div[2]/text()')[0]
        item['矿机编号'] = tr.xpath('./td[2]/div[1]/text()')[0]
        item['矿机名称'] = tr.xpath('./td[2]/div[2]/text()')[0]
        item['时产量'] = tr.xpath('./td[3]/div[1]/text()')[0]
        item['周期收益'] = tr.xpath('./td[4]/div[1]/text()')[0]
        item['价格'] = tr.xpath('./td[5]/text()')[0]
        item['累计收益'] = tr.xpath('./td[6]/text()')[0]
        item['收矿次数'] = tr.xpath('./td[7]/div[1]/text()')[0]
        item['购买时间'] = tr.xpath('./td[8]//text()')[1]
        item['截止时间'] = tr.xpath('./td[8]//text()')[3]

        with open(f"./04file/{item['矿机编号']}.html", 'r', encoding='utf-8') as f:
            hh = f.read()

        page1 = etree.HTML(hh)
        item['矿机等级'] = page1.xpath('//option[@selected="true"]/text()')[0]
        item['矿机状态'] = page1.xpath('//select[@name="status"]/option[@value="1"]/text()')[0]
        item['运行周期'] = page1.xpath('//input[@name="cycle"]/@value')[0]
        item['预计收入'] = page1.xpath('//input[@name="income"]/@value')[0]
        item['算力hash/h'] = page1.xpath('//input[@name="power"]/@value')[0]
        item['矿机价格'] = page1.xpath('//input[@name="price"]/@value')[0]
        item['上次收矿时间'] = page1.xpath('//input[@name="profit_at"]/@value')[0]

        keys_list = list(item.keys())
        print(item)
        data.append(item)
    num += 1

with open('./用户矿机.csv', 'a', encoding='utf-8-sig', newline='') as f:
    csv_f = csv.DictWriter(f, keys_list)
    csv_f.writeheader()
    csv_f.writerows(data)
