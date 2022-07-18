import redis
import requests
from loguru import logger
import vthread
import redis
r = redis.Redis(host="192.168.224.72", port=6379, db=15, password='123456', decode_responses=True)

def rewrite_request(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    while True:
        try:
            print('url:', url)
            response = requests.get(url=url, headers=headers, timeout=10)
            if response.json()['Result']:
                break
        except:
            pass
    return response


@vthread.pool(50)
def get_ip_address(table_name, ip):
    item = {}
    if ':' in ip:
        item['address'] = ''
    else:
        url = f"https://sp1.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query={ip}&resource_id=5809"
        response = rewrite_request(url=url)
        json_data = response.json()['data'][0]
        item['address'] = json_data['location']
    item['ip'] = ip
    save(table_name=table_name, item=item)


def save(table_name, item):
    sql = f"UPDATE `{table_name}` SET `IP归属地` = '{item['address']}' where `发送人IP` = '{item['ip']}';"
    up_data_recode(sql)
    sql = f"select distinct `发送人IP` from `{table_name}` where (`发送人IP` is not null)  and (`IP归属地` is not null);"
    result = select_db_recode(sql)
    r.set('ip_progress_n', len(result))


def get_ip_addr(table_name):
    sql = f"select distinct `发送人IP` from `{table_name}` where (`发送人IP` is not null)  and (`IP归属地` is null);"

    result = select_db_recode(sql)
    ip_list = [ip[0] for ip in result]

    r.set('ip_progress_total', len(ip_list))
    for g_ip in ip_list:
        get_ip_address(table_name, g_ip)

    vthread.pool.waitall()

    logger.remove()
    logger.add('ip_address_log.out')
    logger.info(f'{table_name}---ip归属地已完成！')
    return 'ip归属地已完成！'


if __name__ == '__main__':
    # get_ip_addr('ok钱包2_历史对话_224377')
    rewrite_request('https://sp1.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=2409::8928:70b6:374c:b089:c0f:4e11:1e71&resource_id=5809')