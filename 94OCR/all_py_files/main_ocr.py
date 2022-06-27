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
from extract_data import extract_info
import multiprocessing
import time
import requests


def ocr(gpu_id):
    '''
    收款人、收款户名、对方户名、收款人名称、收款方、收款人姓名

    收款账号、对方账户、对方账户名称、收款卡号、收款账户
    '6217 米米/米米米 8242'、6230521190061458671、6235**********5183、'对方账户:  余忠甫6228****2978'、
    '余忠甫 6228***2978'、6230 *****x  8671、6230**4170

    收款银行、开户行、收款银行开户、收款行、对方账户行别、收款开户行、收款行名
    中国农业银行、黑龙江农村信用社、'收款银行开户 中国农业银行'、中国邮政储蓄银行
    '''


    if not os.path.exists('image_info2.csv'):
        f1 = open('image_info2.csv', 'a', encoding='utf-8-sig', newline='')
        info_f11 = csv.writer(f1)
        print('xiebiaotou!!!')
        info_f11.writerow(
            ['image_url', 'content', '收款人', '收款账号', '收款银行'])
        f1.close()

    f2 = open('image_info2.csv', 'a', encoding='utf-8-sig', newline='')
    info_f = csv.writer(f2)

    r = redis.Redis('192.168.224.72', port=6379, db=3, password='123456')

    reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)  # 没有cpu的话需要加上gpu=False
    while r.scard('image_url'):
        url = r.spop('image_url').decode(encoding='utf-8')
        # url = 'https://legacy-pics.meiqiausercontent.com/images/347754/hvx3/bFsidZlPiCgSvbJ81rYN.png'

        print('url: ', url)

        result = reader.readtext(url)

        content = ''
        for item in result:
            content += '_' + item[1]

        payee, payment_account, payment_bank = extract_info(content)

        # urls.append(url)
        # contents.append(content)
        #
        # dict_obj = {'image_url': urls,
        #             'content': contents,
        #             '收款人': [payee],
        #             '收款账号': [payment_account],
        #             '收款银行': [payment_bank]}
        # df_obj = pd.DataFrame(dict_obj)

        # if os.path.exists('./image_info2.xlsx'):
        #     df = pd.read_excel('./image_info2.xlsx')
        #     df_obj = df.append(df_obj)
        # df_obj.to_excel('./image_info2.xlsx', index=False)

        info_f.writerow([url, content, payee, payment_account, payment_bank])
        print([url, payee, payment_account, payment_bank])


count = 0
def get_image_url(abs_path, folder_name):
    df = pd.read_excel(abs_path)
    image_df = df[df['消息内容'].str.startswith('http') & df['消息内容'].str.match('.*\\.(jpg|png)')]
    image_list = image_df['消息内容'].tolist()

    pool = ProcessPoolExecutor(3)
    all_task = [pool.submit(ocr, url) for url in image_list]
    wait(all_task, return_when=ALL_COMPLETED)

    # wait(pool, return_when=ALL_COMPLETED)

    # ocr(image_list)
    print('ocr 处理完毕！！！')
    global count
    count += len(image_list)


    # print('处理ip归属地......')
    # # 处理ip归属地
    # df['归属地'] = df[['发送人IP']].apply(lambda x: get_asn(x.发送人IP), axis=1)
    # if not os.path.exists(f'./{folder_name}'):
    #     os.mkdir(f'./{folder_name}')
    #
    # save_path = "./{0}/{1}".format(folder_name, abs_path.split('\\\\')[-1])
    # df.to_excel(save_path, index=False)


def scaner_file(url, folder_name):
    '''
    遍历文件夹中的文件
    '''
    file = os.listdir(url)
    for f in file:
        real_url = path.join(url, f)
        if path.isfile(real_url):
            # 如果是文件，则以绝度路径的方式输出
            abs_path = path.abspath(real_url)
            # if 'support-sys-历史对话_347754_2022-03-20_2022-04-01' in abs_path and
            if abs_path == 'C:\\Users\\Administrator\\Desktop\\情报数据《金沙彩票》\\support-sys-历史对话_347754_2022-03-20_2022-04-01_1654676851\\support-sys-历史对话347754_2022-03-20_2022-04-01_1654676926_9000.xlsx':
                print('abs_path: ', abs_path)
                get_image_url(abs_path, folder_name)
        elif path.isdir(real_url):
            # 如果是目录，则是递归调用自定义函数 scaner_file (url)进行多次
            scaner_file(real_url, folder_name)
        else:
            print("其他情况")
            pass


def main(os_context):
    # ll = ['C:/Users/Administrator/Desktop/情报数据《金沙彩票》',
    #       # 'C:/Users/Administrator/Desktop/情报数据《84棋牌》',
    #       # 'C:/Users/Administrator/Desktop/情报数据《668娱乐》'
    # ]
    # for p in ll:
    #     scaner_file(p, p.split('/')[-1])

    # print('count', count)

    pp = []
    for i in range(3):
        p = os_context.Process(target=ocr, args=(0,))
        p.start()
        pp.append(p)

    for p in pp:
        p.join()


if __name__ == '__main__':
    s = time.time()
    # 输出CPU个数和GPU个数
    print('The machine has %d CPUs.' % os.cpu_count())
    print('The machine has %d GPUs.' % torch.cuda.device_count())
    # 获取操作系统上下文
    context = multiprocessing.get_context('spawn')
    # 运行主函数
    main(context)
    print('time: ', time.time()-s)