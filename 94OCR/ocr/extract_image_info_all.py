# !/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import easyocr


def digit_length(string: str):
    digit_count = 0
    for i in string:
        # 判断是否为数字
        if i.isdigit():
            digit_count += 1
    return digit_count


def extract_payee_info(content):
    '''
    收款人信息
    '''
    # print(content)

    if pd.isna(content):
        return None

    payee_list = ['收款人', '收款户名', '对方户名', '收款人名称', '收款方', '收款人姓名', '收款方户名']
    payment_account_list = ['收款账号', '对方账户', '对方账户名称', '收款卡号', '收款账户', '收款方账号']
    payment_bank_list = ['收款银行', '收款银行开户', '收款行', '对方账户行别', '收款开户行', '收款行名']

    try:
        content_list = content.split('_')
    except Exception as e:
        print('payee content_list is error: ', e)
        print(content)
        return '', '', ''

    # 提取收款人
    payee = ''
    for index, value in enumerate(content_list):
        value = value.split(':')[0].split('：')[0]
        if '转给' in value and len(value) <= 6:  # 转给XXX
            temp = value.split('转给')
            if len(temp) == 2:
                payee = temp[1]
                break
        else:
            for i in payee_list:
                if (i == value) and (index+1) < len(content_list):
                    temp = content_list[index+1]
                    if len(temp) <= 4:  # 名字长度
                        payee = temp
    if '复制' in payee:
        payee = ''

    # 提取收款账号
    payment_account = ''
    for index, value in enumerate(content_list):
        for i in payment_account_list:
            if digit_length(value) >= 4:
                temp = value.split(i)
                if len(temp) == 2:
                    payment_account = temp[1]

            elif (i in value) and (index + 3) < len(content_list):
                temp1 = content_list[index + 1]
                temp2 = content_list[index + 2]
                # 识别出来分段的情况
                if ('米米' in temp2 or '**' in temp2 or '米*' in temp2 or '*米' in temp2) and digit_length(temp1) >= 4:
                    payment_account = temp1 + '****' + content_list[index + 3]
                elif digit_length(temp1) >= 4:  # 收款账号数字个数
                    payment_account = temp1
                elif ('米米' in temp2 or '**' in temp2) and digit_length(temp2) >= 4:
                    payment_account = temp2

    # 提取收款银行
    payment_bank = ''
    for index, value in enumerate(content_list):
        for i in payment_bank_list:
            if (i in value) and (index+1) < len(content_list):
                temp = content_list[index + 1]
                if ('银行' in temp) or ('信用社' in temp):
                    payment_bank = temp

    return payee, payment_account, payment_bank


def extract_payer_info(content):
    '''
    付款户名、付款方、付款人:、付款账号名称:
    玉苏甫江:努尔艾合买提
    
    付款账号、付款卡号、付款账户、转出账号
    6228****8674、6230_米米_8723、6228_米*_7673、6214_米米*米_2018、徐迪飞 6217 ******9349、交通银行_借记卡(*1109)、6221 **x 9515、6229*******xxx*1953、
    新昌农商行澄潭支行(6163)
    
    付款银行、付款账号开户行:
    福建省农村信用社

    '''

    payer_list = ['付款人', '付款户名', '付款账号名称:', '付款账号名称', '付款方', '付款人姓名', '付款方户名']
    payer_account_list = ['付款账号', '付款账户', '付款账户名称', '付款卡号', '转出账号', '付款方账号']
    payer_bank_list = ['付款银行', '付款银行开户', '付款行', '付款开户行', '付款行名', '付款账号开户行']

    try:
        content_list = content.split('_')
    except Exception as e:
        print('payer content_list is error: ', e)
        print(content)
        return '', '', ''

    # 提取付款人
    payer = ''
    for index, value in enumerate(content_list):
        value = value.split(':')[0].split('：')[0]
        for i in payer_list:
            if (i == value) and (index+1) < len(content_list):
                temp = content_list[index+1]
                if len(temp) <= 4:  # 名字长度
                    payer = temp

    # 提取付款账号
    payer_account = ''
    for index, value in enumerate(content_list):
        for i in payer_account_list:
            if digit_length(value) >= 4:
                temp = value.split(i)
                if len(temp) == 2:
                    payer_account = temp[1]

            elif (i in value) and (index + 3) < len(content_list):
                temp1 = content_list[index + 1]
                temp2 = content_list[index + 2]
                # 识别出来分段的情况
                if ('米米' in temp2 or '**' in temp2 or '米*' in temp2 or '*米' in temp2) and digit_length(temp1) >= 4:
                    payer_account = temp1 + '****' + content_list[index + 3]
                elif digit_length(temp1) >= 4:  # 收款账号数字个数
                    payer_account = temp1
                elif ('米米' in temp2 or '**' in temp2) and digit_length(temp2) >= 4:
                    payer_account = temp2

    # 提取付款银行
    payer_bank = ''
    for index, value in enumerate(content_list):
        for i in payer_bank_list:
            if (i in value) and (index+1) < len(content_list):
                temp = content_list[index + 1]
                if ('银行' in temp) or ('信用社' in temp):
                    payer_bank = temp

    return payer, payer_account, payer_bank


def extract_trade_time(content):
    '''
    交易时间、创建时间、转账时间、交易日期
    2022-05-1720:40:12、2022-04-08_06:16:19、2022-03-1905.06、2022/02/20、2022-04-08 20:37:57、2022/02/0423.22、
    2022-01-25、2022-04-01_01:57:25
    '''
    trade_time_list = ['交易时间', '创建时间', '转账时间', '交易日期']

    try:
        content_list = content.split('_')
    except Exception as e:
        print('extract_trade_time is error: ', e)
        print(content)
        return ''

    trade_time = ''
    for index, value in enumerate(content_list):
        value = value.split(':')[0].split('：')[0]
        for i in trade_time_list:
            if (i == value) and (index + 1) < len(content_list):
                temp1 = content_list[index + 1]
                if (len(temp1) == 18) and (':' in temp1):
                    trade_time = temp1[:10] + ' ' + temp1[10:]
                elif (len(temp1) == 10) and ((index + 2) < len(content_list)):
                    temp2 = content_list[index + 2]
                    if ':' in temp2:
                        trade_time = temp1 + ' ' + temp2
                    else:
                        trade_time = temp1
                elif (len(temp1) == 15) and ('-' in temp1 or '/' in temp1):
                    trade_time = temp1[:10] + ' ' + temp1[10:]
                else:
                    trade_time = temp1

    trade_time = trade_time.replace('.', ':')
    return trade_time


if __name__ == '__main__':
    # df = pd.read_excel('./image_info.xlsx')
    # df[['收款人', '收款账号', '收款银行']] = df[['content']].apply(lambda x: extract_info(x.content), axis=1, result_type="expand")
    #
    # print(df.to_excel('image_info1.xlsx', index=False))

    import easyocr

    reader = easyocr.Reader(['ch_sim', 'en'], gpu=True)     # 没有cpu的话需要加上gpu=False
    result = reader.readtext('https://legacy-pics.meiqiausercontent.com/images/311745/F7wm/djE5K3XQX6VN4dBEcplw.jpg')
    print(result)

    content = ''
    for item in result:
        content += '_' + item[1]

    payer = extract_payer_info(content)
    trade_time = extract_trade_time(content)

    print(payer, trade_time)