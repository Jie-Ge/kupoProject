import re
import time
import shutil
from zipfile import ZipFile
import os
import pandas as pd
from sqlalchemy import create_engine, types
import pymysql
from loguru import logger
import redis

r = redis.Redis(host="192.168.224.72", port=6379, db=15, password='123456', decode_responses=True)
pd.set_option('display.max_columns', None)


def read_table(path_name):
    df = pd.read_excel(path_name)
    timeArray = time.localtime(int(time.time()))
    checkpoint = time.strftime("%Y-%m-%d", timeArray)
    df['入库时间'] = checkpoint
    df["status"] = 0
    return df


def support_gbk(zip_file):
    try:
        name_to_info = zip_file.NameToInfo
        for name, info in name_to_info.copy().items():
            real_name = name.encode('cp437').decode('gbk')
            if real_name != name:
                info.filename = real_name
                del name_to_info[name]
                name_to_info[real_name] = info
        return zip_file
    except:
        return zip_file


def decompression(zip_project, target_project):
    with support_gbk(zip_project) as zfp:
        zfp.extractall(f'{target_project}')


def read_folder(target_project):
    file_name_list = os.listdir(target_project)
    return file_name_list


def get_file_type(file_name):
    file_type = os.path.splitext(file_name)[1].replace(".", "")
    return file_type


def finish_handle(zip_file_name, conn):
    '''删除数据文件'''
    shutil.rmtree(zip_file_name)
    shutil.rmtree('./历史会话')
    os.remove(zip_file_name + '.zip')
    conn.close()
    r.close()


def get_wallet_bank(content):
    '''匹配出钱包地址 和 银行卡号'''
    cmp1 = re.compile('bc1[0-9A-Za-z]{77}|(5|7)[0-9A-Za-z]{63}|erd1[0-9A-Za-z]{58}|(X|4)[0-9A-Za-z]{57}|G[0-9A-Za-z]{55}|'
                      '9[0-9A-Za-z]{50}|(4|2)[0-9A-Za-z]{43}|terra1[0-9A-Za-z]{38}(0x|xdc)[0-9A-Za-z]{40}|'
                      'SP2[0-9A-Za-z]{39}|tz1[0-9A-Za-z]{33}|(1|3|T|A)[0-9A-Za-z]{33}|0x[0-9A-Za-z]{32}')

    sear1 = cmp1.search(str(content))

    cmp2 = re.compile('([0-9]{16,19})')
    sear2 = cmp2.search(str(content))

    wallet_address = ''
    bank_account = ''
    if sear1:
        wallet_address = sear1.group()
    if sear2:
        bank_account = sear2.group(1)

    return wallet_address, bank_account


def get_wallet_address(df):
    '''获取钱包地址'''
    df['IP归属地'] = None
    df[['钱包地址', '银行卡号']] = df[['消息内容']].apply(lambda x: get_wallet_bank(x.消息内容), axis=1, result_type="expand")
    df['银行卡号归属地'] = None
    df['银行卡号开户行'] = None
    df['status'] = 0
    return df


def put_mysql(zip_file_name):
    pymysql.install_as_MySQLdb()  # 必须
    engine = create_engine("mysql://root:12345678@192.168.224.49:33060/spider", echo=False)
    conn = engine.connect()
    decompression(ZipFile(fr"{zip_file_name}.zip"), zip_file_name)
    file1 = read_folder(fr"{zip_file_name}")[0]
    file_name_list = read_folder(f'{zip_file_name}/' + file1)
    # print(file_name_list)
    # return
    prefix_name = zip_file_name.replace("情报数据《", "").replace("》", "")
    # print(file_name_list)

    if not os.path.exists('历史会话'):
        os.mkdir('历史会话')

    total_df1 = pd.DataFrame()
    table_name1 = ''
    for file_name in file_name_list:
        if "客服登录" in file_name:
            mem = r.smembers('customer_login')
            if file_name in mem:
                msg = '数据已经存在，请不要重复提交！'
                logger.error(msg)
                finish_handle(zip_file_name, conn)
                return {'num': 0, 'msg': msg}
            else:
                r.sadd('customer_login', file_name)

            path_name = os.path.abspath(f"{zip_file_name}") + f"/{file1}/" + file_name
            table_recode = read_table(path_name)
            table_name1 = prefix_name + "_" + file_name.replace("support-sys-", "").split("_")[0] + "_" + file_name.replace("support-sys-", "").split("_")[1]
            total_df1 = total_df1.append(table_recode)
            logger.remove()
            logger.add('main_ocr_log.out')
            logger.info(f'入库文件：{file_name}')

    if table_name1:
        try:
            total_df1.to_sql(table_name1, con=conn, if_exists='append', index=False)
        except Exception as e:
            logger.remove()
            logger.add('mysql_error_log.out', level='ERROR')
            logger.error(e)
            finish_handle(zip_file_name, conn)
            return {'num': 0, 'msg': e}

    history_conversation_list = []
    path_x = ''
    print(file_name_list)
    for file_name in file_name_list:
        file_type = get_file_type(file_name)
        if file_type == "zip":
            decompression(ZipFile(os.path.abspath(f"{zip_file_name}") + f"/{file1}/" + file_name), './历史会话')
            path_x = file_name.replace("support-sys-", "").split("_")[0] + "_" + \
                     file_name.replace("support-sys-", "").split("_")[1]

    history_conversation_list += read_folder('./历史会话')
    table_name2 = ''
    total_df2 = pd.DataFrame()

    # return
    r.set('file_progress_total', len(history_conversation_list))
    file_order = 0
    for conversation in history_conversation_list:
        file_order += 1
        r.set('file_progress_n', file_order)
        time.sleep(3)
        path_name = os.path.abspath("./历史会话") + "/" + conversation
        table_recode = read_table(path_name)
        table_name2 = prefix_name + "_" + path_x
        total_df2 = total_df2.append(table_recode)
        logger.remove()
        logger.add('main_ocr_log.out')
        logger.info(f'入库文件：{conversation}')
        print(f'入库文件：{conversation}')

    if table_name2:
        total_df2 = get_wallet_address(total_df2)
        try:
            dtype = {
                '发送人IP': types.VARCHAR(100),
                '银行卡号': types.VARCHAR(100),
                '入库时间': types.VARCHAR(100)
            }
            total_df2.to_sql(table_name2, con=conn, if_exists='append', index=False, dtype=dtype)

            # 给 `发送人IP` 字段建立索引
            sql = f"CREATE INDEX 发送人IP_index USING BTREE ON `{table_name2}` (`发送人IP`);"
            conn.execute(sql)

            # # 给 `银行卡号`, `入库时间` 字段建立索引
            sql = f"CREATE INDEX 银行卡号_入库时间_index USING BTREE ON `{table_name2}` (`银行卡号`, `入库时间`);"
            conn.execute(sql)

            r.sadd('mysql_table_name', table_name2)
        except Exception as e:
            logger.remove()
            logger.add('mysql_error_log.out', level='ERROR')
            logger.error(e)
            finish_handle(zip_file_name, conn)
            return {'num': 0, 'msg': e}

    r.sadd('image_flag', table_name2 + '_image_flag')
    finish_handle(zip_file_name, conn)

    return {'num': 1, 'msg': '入库并解析成功'}


if __name__ == '__main__':
    put_mysql("ok钱包2")
