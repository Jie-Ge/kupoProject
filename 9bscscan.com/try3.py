import requests
from loguru import logger
from fake_useragent import UserAgent
from lxml import etree


# def get_proxy_ip():
#     ip_api = 'http://api.shenlongip.com/ip?key=lggx7gkw&pattern=json&count=1&need=1000&protocol=2'
#     try:
#         res = requests.get(ip_api)
#     except:
#         return []
#
#     ips = []
#     for item in res.json()['data']:
#         ips.append(item['ip'] + ':' + str(item['port']))
#
#     return ips

def get_proxy_ip():
    ip_api = 'https://proxy.qg.net/allocate?Key=STHB9U24&Num=1&AreaId=&DataFormat=json&DataSeparator=&Detail=0'
    try:
        res = requests.get(ip_api).json()
    except Exception as e:
        logger.info(e)
        return get_proxy_ip()

    if res['Code'] == 0:
        item = res['Data'][0]
        ip = item['host']
        return ip
    else:
        logger.info('请求IP的状态码为：', res['Code'])
        logger.error('等待30秒再请求IP')
        return get_proxy_ip()


# print(get_proxy_ip())

headers = {
    'user-agent': UserAgent().random
}
url = 'https://bscscan.com/address/0x431ba6ba45262043bdfd4081adae2cbeb18d8fe4'
# url = 'https://www.baidu.com/'
# requests版本原因，代理用http，proxies = {'http': f'http://{proxy_ips_list.pop()}'}

ip = '114.231.46.104:21504'
# proxies = {'http': f'http://{get_proxy_ip()[0]}'}
proxies = {'https': 'http://STHB9U24:62E81DC42692@36.6.140.218:18220'}
print(proxies)
response = requests.get(url, headers=headers, proxies=proxies, timeout=5, verify=False, stream=True)
print(response.raw._connection.sock.getpeername())
print(response.text)
# page = etree.HTML(res.text)
#
# tokeninfo_tag = page.xpath('//div[@id="ContentPlaceHolder1_tr_tokeninfo"]//a//text()')
# if tokeninfo_tag:
#     tokeninfo = ''.join(tokeninfo_tag).replace(',', '，').split(' (')
#     full_title = tokeninfo[0]
#     if len(tokeninfo) == 2:
#         short_title = tokeninfo[1].replace(')', '')
#     else:
#         short_title = full_title
#
# # print(tokeninfo)
# # print(full_title)
# # print(short_title)