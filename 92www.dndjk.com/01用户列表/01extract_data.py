# !/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import etree
import csv

num = 1
data = []
keys_list = []
while num <= 18:
    print('num ', num)
    with open(f'./01file/page{num}.html', 'r', encoding='utf-8') as f:
        html = f.read()

    page = etree.HTML(html)
    trs = page.xpath('//div[@class="card"]//tbody/tr')

    count = 0
    for tr in trs:
        count += 1
        print('count ', count)
        item = {}
        item['用户'] = tr.xpath('./td[2]/div[1]/text()')[0]
        item['用户日期'] = tr.xpath('./td[2]/div[2]/text()')[0]
        item['账号'] = tr.xpath('./td[3]/div[1]/text()')[0]
        item['推荐人'] = tr.xpath('./td[3]/div[2]/text()')[0]
        item['类型'] = tr.xpath('./td[4]/text()')[0]
        item['状态'] = tr.xpath('./td[5]//text()')[1].replace('\n', '').replace('\t', '').replace(' ', '')
        item['实名'] = tr.xpath('./td[6]//text()')[1].replace('\n', '').replace('\t', '').replace(' ', '')
        item['可用CRH'] = tr.xpath('./td[7]/text()')[0]
        item['冻结CRH'] = tr.xpath('./td[8]/text()')[0]
        item['可用STD'] = tr.xpath('./td[9]/text()')[0]
        item['冻结STD'] = tr.xpath('./td[10]/text()')[0]

        with open(f"./01file/{item['账号']}.html", 'r', encoding='utf-8') as f:
            hh = f.read()

        page1 = etree.HTML(hh)
        item['个性昵称'] = page1.xpath('//input[@name="nickname"]/@value')[0]
        item['qq号码'] = page1.xpath('//input[@name="qq"]/@value')[0]
        item['微信账号'] = page1.xpath('//input[@name="wechat"]/@value')[0]
        item['支付宝账号'] = page1.xpath('//input[@name="alipay"]/@value')[0]
        item['银行名称'] = page1.xpath('//input[@name="bankname"]/@value')[0]
        item['银行卡号'] = page1.xpath('//input[@name="bankcard"]/@value')[0]
        item['分行地址'] = page1.xpath('//input[@name="bankaddress"]/@value')[0]

        keys_list = list(item.keys())
        print(item)
        data.append(item)
    num += 1

with open('./用户列表.csv', 'a', encoding='utf-8-sig', newline='') as f:
    csv_f = csv.DictWriter(f, keys_list)
    csv_f.writeheader()
    csv_f.writerows(data)
