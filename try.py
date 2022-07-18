import requests
from fake_useragent import UserAgent
from lxml import etree
import pymysql
import pandas as pd
import urllib3
urllib3.disable_warnings()

#特例： 12.209.254.157  美国IP
add = []
class finder:
    def __init__(self):
        self.headers = {
            'user-agent': UserAgent().random
        }
        self.file_url = 'C:/Users/Admin/Downloads/情报数据《84棋牌》/情报数据《84棋牌》/support-sys-历史对话_311473_2022-01-01_2022-02-01_1654678949/support-sys-历史对话311473_2022-01-01_2022-02-01_1654678957_0.xlsx'
        self.count = 1
        self.address = 'https://ip.hao86.com/'
        self.get_detailed_Address_url = 'https://restapi.amap.com/v3/geocode/regeo?output=json&key=c09287250b128f19dfa38a1399607878&radius=1000&extensions=all&location={},{}'

    def get_ip_address(self, ip=None):
        url = f"https://www.ip38.com/ip.php?ip={ip}"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
        }
        while True:
            try:
                print(url)
                response = requests.get(url=url, headers=headers, verify=False, timeout=10)
                break
            except:
                pass
        item = {}
        html = etree.HTML(response.text)
        address = html.xpath('//*[@id="c"]/font/font[1]/text()')[0]
        item['ip'] = ip
        item['address'] = address
        print(item)
        return item

    def get_addr(self, x):
        if x['address'].split(' ')[0] == '湖南省':
            item = self.get_ip_address(x['ip'])
            return item['address']
        else:
            return x['address']

    def get_DILI_location(self):
        df = pd.read_csv('ip_address_hunan.csv')
        print(df)
        df['address1'] = df[['ip', 'address']].apply(lambda x: self.get_addr(x), axis=1)

        # print(df)
        df.to_excel('ip_address_hunan1.xlsx', index=False)


if __name__ == '__main__':
    finder = finder()
    finder.get_DILI_location()
