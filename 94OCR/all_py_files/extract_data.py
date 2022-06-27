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


def extract_info(content):
    # print(content)

    if pd.isna(content):
        return None

    payee_list = ['收款人', '收款人：', '收款人:', '收款户名', '对方户名', '收款人名称', '收款方', '收款人姓名']
    payment_account_list = ['收款账号', '对方账户', '对方账户名称', '收款卡号', '收款账户']
    payment_bank_list = ['收款银行', '收款银行开户', '收款行', '对方账户行别', '收款开户行', '收款行名']
    content_list = content.split('_')

    # 提取收款人
    payee = ''
    for index, value in enumerate(content_list):
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
                if ('米米' in temp2 or '**' in temp2) and digit_length(temp1) >= 4:
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


if __name__ == '__main__':
    # df = pd.read_excel('./image_info.xlsx')
    # df[['收款人', '收款账号', '收款银行']] = df[['content']].apply(lambda x: extract_info(x.content), axis=1, result_type="expand")
    #
    # print(df.to_excel('image_info1.xlsx', index=False))

    import easyocr

    reader = easyocr.Reader(['ch_sim', 'en'], gpu=True)     # 没有cpu的话需要加上gpu=False
    result = reader.readtext('https://legacy-pics.meiqiausercontent.com/images/347754/zDTS/KcyCQpWe1Py63WzirEmw.png')
    print(result)

    content = ''
    for item in result:
        content += '_' + item[1]
    print(extract_info(content))