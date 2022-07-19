import pymysql
from loguru import logger
import time
from dbutils.pooled_db import PooledDB

config = {
    'host': '192.168.224.49',
    'port': 33060,
    'database': 'spider',
    'user': 'root',
    'password': '12345678',
    'charset': 'utf8'
}
poolDB = PooledDB(
    # 指定数据库连接驱动
    creator=pymysql,
    # 连接池允许的最大连接数,0和None表示没有限制
    maxconnections=20,
    # 初始化时,连接池至少创建的空闲连接,0表示不创建
    mincached=10,
    # 连接池中空闲的最多连接数,0和None表示没有限制
    maxcached=5,
    # 连接池中最多共享的连接数量,0和None表示全部共享(其实没什么卵用)
    maxshared=0,
    # 连接池中如果没有可用共享连接后,是否阻塞等待,True表示等等,
    # False表示不等待然后报错
    blocking=True,
    # 开始会话前执行的命令列表
    setsession=[],
    # ping Mysql服务器检查服务是否可用
    ping=0,
    **config
)


def insert_db_recode(sql):
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        logger.remove()
        logger.add('mysql_error_out.log', level='ERROR')
        logger.error(f"insert into mysql fail-----Exception: {e}, sql: {sql}\n")
    finally:
        conn.close()


def select_db_recode(sql):
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        logger.remove()
        logger.add('mysql_error_out.log', level='ERROR')
        logger.error(f"select mysql fail-----Exception: {e}, sql: {sql}\n")
    finally:
        conn.close()


def up_data_recode(sql):
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        logger.add('mysql_error_out.log', level='ERROR')
        logger.error(f"update mysql fail-----Exception: {e}, sql: {sql}\n")
    finally:
        conn.close()


def create_table(table_name):
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        create_cmd = f'''
            create table `{table_name}`(
                image_url        varchar(255)    NOT NULL,
                image_content     text,
                收款人     text,
                收款账号    text,
                收款银行    text,
                付款人      text,
                付款账号    text,
                付款银行    text,
                交易时间    text,
                收款账号归属地    text,
                付款账号归属地    text,
                PRIMARY KEY(image_url)
            );
        '''

        cursor.execute(create_cmd)
        conn.commit()
    except Exception as e:
        logger.remove()
        logger.add('mysql_error_out.log', level='ERROR')
        logger.error(f"create table fail-----{e}\n")
    finally:
        conn.close()