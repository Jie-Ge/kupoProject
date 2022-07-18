import requests
from lxml import etree
import vthread
import re
import json

import ssl
import pyWebBrowser


browser = pyWebBrowser.Browser()
browser.Create(width=0, height=0)


@ vthread.pool(1)
def get_params():
    url = 'https://cn.etherscan.com/token/0x28324828ace2ce9b37bf999851560eac74338d76'
    try:
        browser.Open(url=url)
        browser.WaitByElement('//*[@id="content"]/div[1]/div/div[1]/h1/img/@src')
        htmlElement = browser.Html()
        print(htmlElement.xpath('//*[@id="content"]/div[1]/div/div[1]/h1/img/@src'))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    for i in range(1000000):
        get_params()
    # get_params()
    vthread.pool.waitall()
# PnAfOlYMNSQX-13-723ba2472ae68385

