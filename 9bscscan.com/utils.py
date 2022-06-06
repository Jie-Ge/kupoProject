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
    maxconnections=10,
    # 初始化时,连接池至少创建的空闲连接,0表示不创建
    mincached=2,
    # 连接池中空闲的最多连接数,0和None表示没有限制
    maxcached=10,
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


def insert_db_record(item):
    conn = poolDB.connection()
    cursor = conn.cursor()
    try:
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        logger.info(f"开始插入数据------{otherStyleTime}\n")
        cursor.execute(f"insert into xunibi.contract_info(contract_address, href, tag, summary_html, contract_code, token_tracker_html, creator_hash_html, crawl_date) "
                       f"values('{item['contract_address']}', '{item['href']}', '{item['tag']}', '{item['summary_html']}', '{item['contract_code']}', '{item['token_tracker_html']}', '{item['creator_hash_html']}', '{item['crawl_date']}');")
        conn.commit()
        logger.info(f"insert into xunibi.contract_info success-------{otherStyleTime}\n")
    except Exception as e:
        logger.error(f"insert into xunibi.contract_info fail------------{otherStyleTime}\n")
        print(e)

    finally:
        conn.close()

