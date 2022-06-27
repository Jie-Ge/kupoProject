# !/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import redis
import torch
import os
from os import path
import pandas as pd
import easyocr
from concurrent.futures import ProcessPoolExecutor, wait, ALL_COMPLETED
from extract_image_info_all import extract_payee_info, extract_payer_info, extract_trade_time
import multiprocessing
from utils_mysql import insert_db_recode

# if not os.path.exists('../image_info7.csv'):
#     f1 = open('../image_info7.csv', 'a', encoding='utf-8-sig', newline='')
#     info_f11 = csv.writer(f1)
#     print('xiebiaotou!!!')
#     info_f11.writerow(
#         ['image_url', 'content', '收款人', '收款账号', '收款银行', '付款人', '付款账号', '付款银行', '交易时间'])
#     f1.close()
#
# f2 = open('../image_info7.csv', 'a', encoding='utf-8-sig', newline='')
# info_f = csv.writer(f2)

r = redis.Redis('192.168.224.72', port=6379, db=3, password='123456')


def ocr(process_name):
    '''
    收款人、收款户名、对方户名、收款人名称、收款方、收款人姓名

    收款账号、对方账户、对方账户名称、收款卡号、收款账户
    '6217 米米/米米米 8242'、6230521190061458671、6235**********5183、'对方账户:  余忠甫6228****2978'、
    '余忠甫 6228***2978'、6230 *****x  8671、6230**4170

    收款银行、开户行、收款银行开户、收款行、对方账户行别、收款开户行、收款行名
    中国农业银行、黑龙江农村信用社、'收款银行开户 中国农业银行'、中国邮政储蓄银行
    '''

    if process_name % 2 == 0:  # 指定使用哪张显卡
        os.environ["CUDA_VISIBLE_DEVICES"] = "1"
    else:
        os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    reader = easyocr.Reader(['ch_sim', 'en'])  # 没有cpu的话需要加上gpu=False
    while r.scard('not_image_url'):
        try:
            url = r.spop('not_image_url').decode(encoding='utf-8')
            # url = 'https://legacy-pics.meiqiausercontent.com/images/311473/BxFI/Y3FLVdxDkxK0PpUN7rl1.jpg'

            print('url: ', url)

            try:
                result = reader.readtext(url)
            except:
                continue

            content = ''
            for item in result:
                content += '_' + item[1]

            payee, payment_account, payment_bank = extract_payee_info(content)
            payer, payer_account, payer_bank = extract_payer_info(content)
            trade_time = extract_trade_time(content)

            sql = f"insert into jinsha_chat_image_info_01 " \
                  f"values('{url}', '{content}', '{payee}', '{payment_account}', '{payment_bank}', '{payer}', '{payer_account}', '{payer_bank}', '{trade_time}');"

            insert_db_recode(sql)
            print([url, payee, payment_account, payment_bank, payer, payer_account, payer_bank, trade_time])
        except:
            pass


def main(os_context):
    pp = []
    for i in range(4):
        p = os_context.Process(target=ocr, args=(i,))
        p.start()
        pp.append(p)

    for p in pp:
        p.join()


if __name__ == '__main__':
    # 输出CPU个数和GPU个数
    print('The machine has %d CPUs.' % os.cpu_count())
    print('The machine has %d GPUs.' % torch.cuda.device_count())
    # 获取操作系统上下文
    context = multiprocessing.get_context('spawn')
    # 运行主函数
    main(context)

