'''
https://www.mytokencap.com/exchange  参数加密
'''

import execjs
import requests

with open('./code.js', 'r') as f:
    js = f.read()

jscode = execjs.compile(js)
code = jscode.call('get_code')

print(code)

url = 'https://api.mytokenapi.com/exchange/listbyexchangevolume'

params = {
    'page': 1,
    'size': 50,
    'need_pagination': 1,
    'timestamp': code['timestamp'],
    'code': code['code'],
    'platform': 'web_pc',
    'v': '1.0.0',
    'language': 'zh_CN',
    'legal_currency': 'USD'
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=headers, params=params)

print(res.text)