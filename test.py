import csv
import os

import redis
import threading

# r = redis.Redis('192.168.224.72', port=6379, db=15, password='123456')
import requests
import vthread


f1 = open('ip_address_hunan.csv', 'a', encoding='utf-8-sig', newline='')
info_f = csv.writer(f1)
info_f.writerow(['ip', 'address'])


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
def get_ip_address(ip):
    item = {}
    if ':' in ip:
        item['address'] = ''
    else:
        url = f"https://sp1.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query={ip}&resource_id=5809"
        response = rewrite_request(url=url)
        json_data = response.json()['data'][0]
        item['address'] = json_data['location']
    item['ip'] = ip
    save(item=item)


def save(item):
    print([item['ip'], item['address']])
    if '湖南' in item['address']:
        info_f.writerow([item['ip'], item['address']])


def main():
    with open('./ip_list.txt', 'r') as f:
        ips = f.read()
        ip_list = ips.split('\n')

    count = 0
    tt = len(ip_list)
    for g_ip in ip_list:
        count += 1
        print(f'{count}/{tt}')
        get_ip_address(g_ip)

    vthread.pool.waitall()


if __name__ == '__main__':
    main()
