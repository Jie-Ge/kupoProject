import requests
from lxml import etree
import json
import re

coin_info = []
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

params = {
    't': '79bcbabec04fa4c313fc65fd8ff0407f',
    'lan': 'zh'
}

url = 'https://www.mifengcha.com/exchange/mercado-bitcoin'
response = requests.get(url, headers=headers, timeout=10)

cmp = re.compile('<div class="description".*?(<p.*?</p>)', re.S)

have_search = cmp.search(response.text)
if have_search:
    desc = have_search.group(1)
else:
    print('请求到的不是正常的detail page')
    # fail_page_url.append(response.url)
    # return None

# 替换 a 标签
text_list = re.findall('<a.*?>(.*?)</a>', desc, re.S)
a_tags = re.findall('<a.*?>.*?</a>', desc, re.S)

if len(text_list) and len(text_list) == len(a_tags):
    for (a_tag, text) in zip(a_tags, text_list):
        desc = desc.replace(a_tag, text)

desc = desc.replace('&#x27;', "'")

print(desc)


