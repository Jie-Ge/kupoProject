import requests
from fake_useragent import UserAgent
import random

ua = UserAgent()
useragent = random.choice(ua.data_browsers['chrome'])
headers = {
    'user-agent': useragent,
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'autonotice': 'true',
    'content-length': '49',
    'content-type': 'application/json;charset=UTF-8',
    'diff_time': '-4082',
    'jwt_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MzMiLCJleHAiOjE2NDgyNDAzMTksImlhdCI6MTY0ODExMDcxOX0.O16zXefnz7ZfI9EJnA5aCE_P_bGv28ZCmyNarTgfCCw',
    'nonotice': 'false',
    'origin': 'https://aml.zklatech.com',
    'referer': 'https://aml.zklatech.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'x_token': '159fade6b71e23d54a0bc250b8092509'
    }
data = {
    'pageIndex': 1,
    'pageSize': 12,
    'title': "",
    'type': 1
}
print(useragent)
url = 'https://aml.zklatech.com/api/cms/case_law/list'
req = requests.get(url, headers=headers, data=data)
cnt = req.json()
print(cnt)