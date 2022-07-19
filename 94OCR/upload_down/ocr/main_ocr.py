# !/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import time

import pymysql
import redis
import torch
import os
from os import path
import pandas as pd
import easyocr
from concurrent.futures import ProcessPoolExecutor, wait, ALL_COMPLETED

import sys
sys.path.append(os.path.abspath('./ocr'))  # 必须要添加路径，否则flask找不到 extract_image_info_all 这种自定义的py文件

from extract_image_info_all import extract_payee_info, extract_payer_info, extract_trade_time
import multiprocessing
from utils_mysql import insert_db_recode, create_table
from loguru import logger
from put_image_url import get_image_url, image_url_thread
from card_adress_spider import card_address


r = redis.Redis('192.168.224.72', port=6379, db=15, password='123456', decode_responses=True)

error_msg = ''
error_code = 1
def en_decode(str01):
    return str(str01).replace('\'', '').replace('\001', '').replace('\002', '') \
        .replace(r'\0xa0', '').replace('\n', ' ').replace('\r', ' ') \
        .encode("utf-8", 'ignore').decode("utf-8", "ignore")


def is_exist_table(table_name):
    '''
    判断数据库中是否已存在表
    '''
    conn1 = pymysql.connect(
        host='192.168.224.49',
        port=33060,
        user='root',
        password='12345678',
        database='spider'
    )

    cursor = conn1.cursor()

    sql = 'show tables'
    cursor.execute(sql)
    result = cursor.fetchall()

    conn1.close()

    tables = []
    for item in result:
        tables.append(item[0])

    if table_name in tables:
        return True
    else:
        return False


def ocr(process_name, image_table_name):
    '''
    收款人、收款户名、对方户名、收款人名称、收款方、收款人姓名

    收款账号、对方账户、对方账户名称、收款卡号、收款账户
    '6217 米米/米米米 8242'、6230521190061458671、6235**********5183、'对方账户:  余忠甫6228****2978'、
    '余忠甫 6228***2978'、6230 *****x  8671、6230**4170

    收款银行、开户行、收款银行开户、收款行、对方账户行别、收款开户行、收款行名
    中国农业银行、黑龙江农村信用社、'收款银行开户 中国农业银行'、中国邮政储蓄银行
    '''
    global error_msg, error_code

    if process_name % 2 == 0:  # 指定使用哪张显卡
        os.environ["CUDA_VISIBLE_DEVICES"] = "1"
    else:
        os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    reader = easyocr.Reader(['ch_sim', 'en'])  # 没有cpu的话需要加上gpu=False
    while r.scard('image_url'):
        try:
            url = r.spop('image_url')
            # url = 'https://legacy-pics.meiqiausercontent.com/images/311473/BxFI/Y3FLVdxDkxK0PpUN7rl1.jpg'

            result = reader.readtext(url)

            content = ''
            for item in result:
                content += '_' + item[1]
            content = en_decode(content)

            payee, payment_account, payment_bank = extract_payee_info(content)  # 收款
            payer, payer_account, payer_bank = extract_payer_info(content)  # 付款
            trade_time = extract_trade_time(content)

            receipt_account_addr = ''
            receipt_bank_name = ''
            if payment_account and payment_account.isdigit():
                receipt_account_addr, receipt_bank_name = card_address(payment_account)
                if receipt_bank_name == 0:
                    logger.remove()
                    logger.add('main_error_out.log')
                    logger.error(receipt_account_addr)
                    error_msg = receipt_account_addr
                    error_code = 0
                    return None

            payer_account_addr = ''
            payer_bank_name = ''
            if payer_account and payer_account.isdigit():
                payer_account_addr, payer_bank_name = card_address(payer_account)
                if payer_bank_name == 0:
                    logger.remove()
                    logger.add('main_error_out.log')
                    logger.error(payer_account_addr)
                    error_msg = payer_account_addr
                    error_code = 0
                    return None

            # 如果图片上没有开户行，就用API根据银行卡号识别出来的开户行
            if not payment_bank:
                payment_bank = receipt_bank_name
            if not payer_bank:
                payer_bank = payer_bank_name

        except Exception as e:
            r.sadd('fail_image_url', url)
            logger.remove()
            logger.add('main_error_out.log', level='ERROR')
            logger.error(f"func ocr() error-------，Exception: {e}，url: {url}\n")
        else:
            sql = f"insert into `{image_table_name}` " \
                  f"values('{url}', '{content}', '{payee}', '{payment_account}', '{payment_bank}', '{payer}', '{payer_account}', '{payer_bank}', '{trade_time}', '{receipt_account_addr}', '{payer_account_addr}');"
            print([url, payee, payment_account, payment_bank, payer, payer_account, payer_bank, receipt_account_addr, payer_account_addr])
            insert_db_recode(sql)
            image_progress_total = r.get('image_progress_total')
            r.set('image_progress_n', int(image_progress_total) - r.scard('image_url'))


def parse_image_info(table_name):
    global error_msg, error_code
    error_code = 1

    image_table_name = table_name + '_image'  # 存储图片信息的表名
    image_flag = table_name + '_image_flag'

    # 根据表名检查是否是第一次执行
    if not is_exist_table(image_table_name):
        create_table(image_table_name)

    image_flag_set = r.smembers('image_flag')
    if image_flag in image_flag_set:
        print('正在匹配图片地址.......')
        get_image_url(table_name)
        r.srem('image_flag', image_flag)
    else:
        print('正在入fail_image_url......')
        fail_url_set = r.smembers('fail_image_url')
        if fail_url_set:
            # 每次执行先将请求失败的url重新入队列
            image_url_thread(list(fail_url_set))
            r.delete('fail_image_url')

    url_set = r.smembers('image_url')
    if not url_set:
        logger.remove()
        logger.add('main_ocr_out.log')
        logger.info(f'{table_name}---解析图片已全部完成')
        return {'num': 0, 'msg': '解析图片已全部完成！'}

    r.set('image_progress_total', len(url_set))

    # 输出CPU个数和GPU个数
    print('The machine has %d CPUs.' % os.cpu_count())
    print('The machine has %d GPUs.' % torch.cuda.device_count())
    # 获取操作系统上下文
    context = multiprocessing.get_context('spawn')

    pp = []
    for i in range(2):
        p = context.Process(target=ocr, args=(i, image_table_name))
        p.start()
        pp.append(p)

    for p in pp:
        p.join()

    if error_code == 0:
        return {'num': 0, 'msg': error_msg}

    r.set('image_progress_n', 0)
    return {'num': 0, 'msg': '请再次点击解析图片按钮，检验是否已全部解析完成！'}


if __name__ == '__main__':
    parse_image_info('澳门威尼斯人_历史对话_347932')

