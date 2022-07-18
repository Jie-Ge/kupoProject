import os
from os import path
import pandas as pd
import redis


r = redis.Redis('192.168.224.72', port=6379, db=15, password='123456')

count = 0
def open_file(abs_url):
    global count
    df = pd.read_excel(abs_url)
    image_urls = df['消息内容'].tolist()

    for image_url in image_urls:
        if image_url.startswith('http') and (image_url.endswith('.jpg') or image_url.endswith('.png')):
            count += 1
            print(image_url, count)
            r.sadd('all_image_url', image_url)


def scaner_file(url):
    file = os.listdir(url)
    for f in file:
        real_url = path.join(url, f)
        if path.isfile(real_url):
            # 如果是文件，则以绝度路径的方式输出
            abs_url = path.abspath(real_url)
            print(abs_url)
            open_file(abs_url)
        elif path.isdir(real_url):
            # 如果是目录，则是递归调用自定义函数 scaner_file (url)进行多次
            scaner_file(real_url)
        else:
            print("其他情况")
            pass


ll = [
    'C:/Users/Administrator/Desktop/情报数据《金沙彩票》',
      'C:/Users/Administrator/Desktop/情报数据《84棋牌》',
      'C:/Users/Administrator/Desktop/情报数据《668娱乐》'
]
for p in ll:
    scaner_file(p)

# open_file('C:/Users/Administrator/Desktop/情报数据《金沙彩票》/support-sys-历史对话_347754_2022-03-20_2022-04-01_1654676851/support-sys-历史对话347754_2022-03-20_2022-04-01_1654676866_1000.xlsx')
