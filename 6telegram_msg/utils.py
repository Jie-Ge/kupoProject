import psycopg2
from loguru import logger
import time
from dbutils.pooled_db import PooledDB

config = {
    'host': '192.168.224.80',
    'port': 5432,
    'database': 'yuqing',
    'user': 'mxadmin',
    'password': '1qaz2wsx'
}
poolDB = PooledDB(
    # 指定数据库连接驱动
    creator=psycopg2,
    # 连接池允许的最大连接数,0和None表示没有限制
    maxconnections=5,
    # 初始化时,连接池至少创建的空闲连接,0表示不创建
    mincached=2,
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


def insert_db_history(item, table_name):
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        logger.info(f"开始插入数据------{otherStyleTime}\n")
        cursor.execute(f"insert into telegram01.{table_name}(link, date_time, text_info, username, first_name, last_name, msg_id) "
                       f"values('{item['link']}', '{item['date_time']}', '{item['text_info']}', '{item['username']}', '{item['first_name']}', '{item['last_name']}', '{item['msg_id']}');")
        conn.commit()
        logger.info(f"insert into telegram01.{table_name} success-------{otherStyleTime}\n")
    except Exception as e:
        logger.error(f"insert into telegram01.{table_name} fail------------{otherStyleTime}\n")
        print('fail...: ', item)
        print(e)
    finally:
        conn.close()


def select_db_count(seq):
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        logger.info(f"开始计算 telegram_msg_{seq} 数据量-----------{otherStyleTime}\n")
        cursor.execute(f"select count(*) from telegram01.telegram_msg_{seq};")
        result_list = cursor.fetchall()
        logger.info(f"计算 telegram_msg_{seq} 数据成功-----------{otherStyleTime}\n")
        return result_list
    except:
        logger.info(f"查询失败--------{otherStyleTime}\n")
    finally:
        conn.close()


def select_db_record(sql):
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        logger.info(f"开始读取数据-----------{otherStyleTime}\n")
        cursor.execute(sql)
        result_list = cursor.fetchall()
        logger.info(f"读取数据成功-----------{otherStyleTime}\n")
        return result_list
    except:
        logger.info(f"查询失败--------{otherStyleTime}\n")
    finally:
        conn.close()


def show_tables():
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        logger.info(f"开始查询表名------{otherStyleTime}\n")
        cursor.execute("select tablename from pg_tables where schemaname='telegram01';")
        result_list = cursor.fetchall()
        logger.info(f"查询表名成功-------{otherStyleTime}\n")
        return result_list
    except Exception as e:
        logger.info(f"查询表名失败------------{otherStyleTime}\n")
    finally:
        conn.close()


def create_msg_table(table_name):
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        logger.info(f"开始创建新表 {table_name}------{otherStyleTime}\n")

        create_cmd = f'''
            create table telegram01.{table_name}(
                link        varchar(255)    NOT NULL,
                date_time   timestamp,
                text_info   text,
                username    varchar(255),
                first_name  varchar(255),
                last_name   varchar(255),
                msg_id      int4,
                result      jsonb,
                PRIMARY KEY(link, msg_id)
            );
        '''

        cursor.execute(create_cmd)
        conn.commit()
        logger.info(f"创建新表 {table_name} 成功-------{otherStyleTime}\n")
    except Exception as e:
        logger.info(f"创建新表 {table_name} 失败------------{otherStyleTime}\n")
        print(e)
    finally:
        conn.close()


def insert_db_group_info(data: list):
    conn = poolDB.connection()
    cursor = conn.cursor()
    for item in data:
        try:
            now = int(time.time())
            # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
            timeArray = time.localtime(now)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            logger.info(f"开始插入数据------{otherStyleTime}\n")
            cursor.execute(f"insert into telegram01.tg_group_info(name,link,group_or_channel,members_amount,introduction,members_username,crawl_date) "
                           f"values('{item['name']}', '{item['link']}', '{item['group_or_channel']}', '{item['members_amount']}', '{item['introduction']}', '{item['members_username']}', '{item['crawl_date']}');")
            conn.commit()
            logger.info(f"insert into telegram01.tg_group_info success-------{otherStyleTime}\n")
        except Exception as e:
            logger.info(f"insert into telegram01.tg_group_info fail------------{otherStyleTime}\n")
            print('insert error: ', e)

    conn.close()


def up_db_group_info(data: list):
    conn = poolDB.connection()
    cursor = conn.cursor()
    for item in data:
        try:
            now = int(time.time())
            # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
            timeArray = time.localtime(now)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            logger.info(f"开始UPDATE数据------{otherStyleTime}\n")
            cursor.execute(f"UPDATE telegram01.tg_group_info SET name='{item['name']}', members_amount='{item['members_amount']}', introduction='{item['introduction']}', "
                           f"members_username='{item['members_username']}', crawl_date='{item['crawl_date']}', is_new_add='{item['is_new_add']}' "
                           f"where link='{item['link']}'")
            conn.commit()
            logger.info(f"UPDATE xnbyq.tg_group_info success-------{otherStyleTime}\n")
        except Exception as e:
            logger.info(f"UPDATE xnbyq.tg_group_info fail------------{otherStyleTime}\n")
            print('UPDATE error: ', e)

    conn.close()


def del_db_group_info():
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        logger.info(f"开始删除--------{otherStyleTime}\n")
        cursor.execute(f"DELETE FROM telegram01.tg_group_info;")
        conn.commit()
        logger.info(f"删除成功\n")
    except:
        logger.info(f"删除失败\n")
    finally:
        conn.close()


