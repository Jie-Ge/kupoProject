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


def insert_db_recode(sql):
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        # logger.info(f"开始插入数据------{otherStyleTime}\n")
        cursor.execute(sql)
        conn.commit()
        logger.info(f"insert into mysql success-------{otherStyleTime}\n")
        return True
    except Exception as e:
        logger.info(f"insert into mysql fail------------{otherStyleTime}\n")
        print(e)
        return False
    finally:
        conn.close()


def select_db_recode(sql):
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        cursor.execute(sql)
        logger.info(f"select mysql success-------{otherStyleTime}\n")
        return cursor.fetchall()
    except Exception as e:
        logger.info(f"select mysql fail------------{otherStyleTime}\n")
        print(e)
        return False
    finally:
        conn.close()


def up_data_recode(sql):
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        cursor.execute(sql)
        conn.commit()
        logger.info(f"update mysql success-------{otherStyleTime}\n")
        return cursor.fetchall()
    except Exception as e:
        logger.info(f"update mysql fail------------{otherStyleTime}\n")
        print(e)
        return False
    finally:
        conn.close()