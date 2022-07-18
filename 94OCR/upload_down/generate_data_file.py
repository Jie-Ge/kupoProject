# !/usr/bin/python
# -*- coding: utf-8 -*-
import os
from datetime import date
import pandas as pd
from sqlalchemy import create_engine, types
import pymysql
from loguru import logger
from zipfile import ZipFile, ZIP_DEFLATED
import warnings
warnings.filterwarnings("ignore")

pymysql.install_as_MySQLdb()  # 必须
engine = create_engine("mysql://root:12345678@192.168.224.49:33060/spider", echo=True)
conn = engine.connect()


def get_image_info(table_name):
    '''获取图片识别出的信息'''
    df = pd.read_sql_table(table_name+'_image', conn)

    ## 平台（收款方）
    df['isdigit1'] = df['收款账号'].str.isdigit()
    data1 = df[(df['isdigit1'] == True) & (df['收款账号'].str.len() > 15)]
    data1.drop_duplicates('收款账号', inplace=True)

    df_pt = data1[['image_url', '收款人', '收款账号', '收款银行', '收款账号归属地']]  # 选取这些字段数据
    # df_pt.rename(columns={'image_url': 'sdsd'}, inplace=True)
    df_pt.columns = ['消息内容', '姓名', '银行卡号', '银行卡号开户行', '银行卡号归属地']  # 字段重命名
    df_pt['钱包地址'] = ''
    # df_pt = df_pt.drop(index=df_pt[df_pt['姓名'] == ''].index.tolist())
    # df_pt.dropna(subset=['姓名'],  # 指定列
    #              axis=0,
    #              how='all',  # how='all'表示若指定列的值都为空，就删掉该行
    #              inplace=True)
    df_pt = df_pt[df_pt['姓名'] != '']

    ## 赌客（付款方）
    df['isdigit2'] = df['付款账号'].str.isdigit()
    data2 = df[(df['isdigit2'] == True) & (df['付款账号'].str.len() > 15)]
    data2.drop_duplicates('付款账号', inplace=True)

    df_duke = data2[['image_url', '付款人', '付款账号', '付款银行', '付款账号归属地']]

    # data2.rename(columns={'image_url': 'sdsd'}, inplace=True)
    df_duke.columns = ['消息内容', '姓名', '银行卡号', '银行卡号开户行', '银行卡号归属地']
    df_duke['钱包地址'] = ''
    # data2 = data2.drop(index=data2[data2['姓名'] == ''].index.tolist())
    # df_duke.dropna(subset=['姓名'],  # 指定列
    #              axis=0,
    #              how='all',  # how='all'表示若指定列的值都为空，就删掉该行
    #              inplace=True)
    df_duke = df_duke[df_duke['姓名'] != '']

    df_duke.insert(1, '发送人IP', '')
    df_duke.insert(2, 'IP归属地', '')

    return df_pt, df_duke


def save_file(df, table_name, pingtai_or_duke):
    if not os.path.exists('data'):
        os.mkdir('data')

    # 防止将 url 存储为超链接（若为超链接，打开xlsx会报错）
    writer = pd.ExcelWriter(f'data/{table_name}_{pingtai_or_duke}.xlsx', engine='xlsxwriter',
                                    engine_kwargs={'options': {'strings_to_urls': False}})
    df.to_excel(writer, index=False)
    writer.close()


def get_date_file(table_name):
    try:
        sql = f"select * from `{table_name}` where (银行卡号 != '') or 钱包地址 != '';"

        df = pd.read_sql(sql, conn)

        pingtai_df = df[pd.isna(df['发送人IP'])]
        pingtai_df.drop(columns=['status', 'IP归属地'], axis=1, inplace=True)

        pingtai_df = pingtai_df[['消息内容', '钱包地址', '银行卡号', '银行卡号开户行', '银行卡号归属地']]
        pingtai_df = pingtai_df.drop_duplicates(['钱包地址', '银行卡号'])
        pingtai_df = pingtai_df.drop(index=pingtai_df[(pingtai_df['银行卡号归属地'] == '银行卡号错误') & (pingtai_df['钱包地址'] == '')].index.tolist())
        new_columns = ['消息内容', '银行卡号', '银行卡号开户行', '银行卡号归属地', '钱包地址']  # 调整列的顺序
        pingtai_df = pingtai_df.reindex(columns=new_columns)

        pingtai_df.insert(1, '姓名', '')

        df_image_pt, df_image_duke = get_image_info(table_name)

        pingtai_df = pingtai_df.append(df_image_pt)
        save_file(pingtai_df, table_name, '平台')


        duke_df = df[pd.notna(df['发送人IP'])]
        duke_df.drop(columns=['status'], axis=1, inplace=True)

        duke_df = duke_df[
            ['消息内容', '发送人IP', 'IP归属地', '钱包地址', '银行卡号', '银行卡号归属地', '银行卡号开户行']]
        duke_df = duke_df.drop_duplicates(['钱包地址', '银行卡号'])
        duke_df = duke_df.drop(
            index=duke_df[(duke_df['银行卡号归属地'] == '银行卡号错误') & (duke_df['钱包地址'] == '')].index.tolist())
        new_columns = ['消息内容', '发送人IP', 'IP归属地', '银行卡号', '银行卡号归属地', '银行卡号开户行', '钱包地址']
        duke_df = duke_df.reindex(columns=new_columns)

        duke_df.insert(3, '姓名', '')

        duke_df = duke_df.append(df_image_duke)
        save_file(duke_df, table_name, '赌客')

        return {'msg': '生成数据文件成功！', 'file_name': table_name}
    except Exception as e:
        logger.remove()
        logger.add('main_error_log.out')
        logger.error(e)
        print(e)
        return {'msg': e, 'file_name': table_name}


if __name__ == '__main__':
    # get_date_file('id299265-新葡京_历史对话_299265')
    get_date_file('id138323-太阳城_历史对话_138323')