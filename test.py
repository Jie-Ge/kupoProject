import requests
from lxml import etree
import pandas as pd
import threading

import pandas as pd
import random
import time
# from utils import insert_db_record
from datetime import date, datetime
import pandas as pd
from fake_useragent import UserAgent
ua = UserAgent()

aaa = {'code': 200, 'data': [{'ip': '183.151.151.96', 'port': 31421}, {'ip': '123.134.158.53', 'port': 49153}]}

# ip_api = 'http://api.shenlongip.com/ip?key=hzqnpugb&pattern=json&count=1&need=1000&protocol=1'
# res = requests.get(ip_api)
# data1 = res.json()

# print(res)
# ip = data1['data'][0]['ip'] + ':' + str(data1['data'][0]['port'])
# proxy_ip = {'http': f'http://{ip}'}
proxy_ip = {'https': 'http://112.74.170.183:8888'}
print(proxy_ip)

aa = 1


def main():
    global aa
    url = 'https://bscscan.com/token/0x186b6eb42163701e2c25e5c4bed461ecc90a0044'
    headers = {
        'user-agent': random.choice(ua.data_browsers['chrome']),
        # 'accept' :'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'accept-encoding' :'gzip, deflate, br',
        # 'accept-language' :'zh-CN,zh;q=0.9',
        # 'cache-control' :'no-cache',
        # 'pragma' :'no-cache',
        # # 'Connection': 'close',
        # 'keep-live':'false',
        # 'referer': 'https://www.baidu.com/',
        # 'sec-ch-ua' :'" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        # 'sec-ch-ua-mobile' :'?0',
        # 'sec-ch-ua-platform' :'"Windows"',
        # 'sec-fetch-dest' :'document',
        # 'sec-fetch-mode' :'navigate',
        # 'sec-fetch-site' :'none',
        # 'sec-fetch-user' :'?1',
        # 'upgrade-insecure-requests' :'1',

    }
    res = requests.get(url=url, headers=headers, verify=False, proxies=proxy_ip, stream=True, timeout=(10, 10))
    print(res.text)
    print(res.status_code)



if __name__ == '__main__':
    # s = time.time()
    # tt = []
    # for i in range(5):
    #     t = threading.Thread(target=main)
    #     t.start()
    #     tt.append(t)
    #
    # for t in tt:
    #     t.join()
    main()
    # print('耗时：', time.time()-s)