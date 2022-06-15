import os
from os import path
import pandas as pd


def scaner_file(url):
    file = os.listdir(url)
    for f in file:
        real_url = path.join(url, f)
        if path.isfile(real_url):
            # 如果是文件，则以绝度路径的方式输出
            abs_url = path.abspath(real_url)
            print(abs_url)
            df = pd.read_excel(abs_url)
            aa = df[df['消息内容'].str.startswith('http')]
            print(aa['消息内容'].tolist())
        elif path.isdir(real_url):
            # 如果是目录，则是递归调用自定义函数 scaner_file (url)进行多次
            scaner_file(real_url)
        else:
            print("其他情况")
            pass
        break


ll = ['C:/Users/Administrator/Desktop/情报数据《金沙彩票》',
      'C:/Users/Administrator/Desktop/情报数据《84棋牌》',
      'C:/Users/Administrator/Desktop/情报数据《668娱乐》']
for p in ll:
    scaner_file(p)
