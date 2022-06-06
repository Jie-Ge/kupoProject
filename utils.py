import pymysql
from loguru import logger
import time
from dbutils.pooled_db import PooledDB

config = {
    'host': '192.168.224.49',
    'port': 33060,
    'database': 'test',
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


def list_insert_recode(item):
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        logger.info(f"开始插入数据------{otherStyleTime}\n")
        cursor.execute(f"insert into bitcoinabuse_list_data(address_name, date, href) values('{item['address_name']}', '{item['date']}', '{item['href']}');")
        conn.commit()
        logger.info(f"insert into mysql success-------{otherStyleTime}\n")
    except:
        logger.info(f"insert into mysql fail------------{otherStyleTime}\n")
    finally:
        conn.close()


def select_db_recode():
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        logger.info(f"开始读取数据-----------{otherStyleTime}\n")
        cursor.execute(f"select address_name, date, href, page_num from bitcoinabuse_list_data;")
        result_list = cursor.fetchall()
        logger.info(f"读取数据成功-----------{otherStyleTime}\n")
        return result_list
    except:
        logger.info(f"查询失败--------{otherStyleTime}\n")
    finally:
        conn.close()


def del_db_recode(href):
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        logger.info(f"开始删除{href}--------{otherStyleTime}\n")
        cursor.execute(f"DELETE FROM bitcoinabuse_list_data where href = '{href}';")
        conn.commit()
        logger.info(f"删除'{href}'成功\n")
    except:
        logger.info(f"删除'{href}'失败\n")
    finally:
        conn.close()


def up_data_recode(href, page_num):
    conn = poolDB.connection()
    cursor = conn.cursor()
    logger.info(f"UPDATE bitcoinabuse_list_data SET page_num = {page_num} where href = '{href}';")
    cursor.execute(f"UPDATE bitcoinabuse_list_data SET page_num = {page_num} where href = '{href}';")
    conn.commit()
    conn.close()


def insert_details_recode(item):
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        logger.info(f"开始插入详情页数据-----------{otherStyleTime}\n")
        replace_str = "'"
        cursor.execute(f"insert into bitcoinabuse_details_information(address_name, comment_date, abuse_type, description, up_data_date, href) values('{item['address_name']}', '{item['comment_date']}', '{item['abuse_type']}', '{item['description'].replace(replace_str, '')}', '{item['up_data_date']}', '{item['href']}');")
        conn.commit()
        logger.info(f"详情页数据插入成功----------{otherStyleTime}\n")
    except:
        logger.info(f"详情页插入失败--------{otherStyleTime}\n")
    finally:
        conn.close()

