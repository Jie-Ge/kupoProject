import os
from os import path
import pandas as pd
import redis

# aa = ['https://legacy-pics.meiqiausercontent.com/images/311745/3OmA/UuBAyyN7FTCKmSOKJFqe.jpg',
#       'https://legacy-pics.meiqiausercontent.com/images/311473/2t4P/aceoHdz0mhfhjdb0Wm17.jpg']
#
# r = redis.Redis('192.168.224.72', port=6379, db=3, password='123456')
#
# for url in aa:
#     print(url)
#     r.sadd('image_url', url)


# total_df = pd.read_excel('C:/Users/Administrator/Desktop/image_info1.xlsx')

# total_df = pd.DataFrame()
# def scaner_file(url):
#     global total_df
#     file = os.listdir(url)
#     for f in file:
#         real_url = path.join(url, f)
#         if path.isfile(real_url):
#
#             # 如果是文件，则以绝度路径的方式输出
#             abs_url = path.abspath(real_url)
#             print(abs_url)
#             df = pd.read_excel(abs_url)
#             total_df = total_df.append(df)
#
#         elif path.isdir(real_url):
#             # 如果是目录，则是递归调用自定义函数 scaner_file (url)进行多次
#             scaner_file(real_url)
#         else:
#             print("其他情况")
#             pass
#
#
# ll = [
#     # 'C:/Users/Administrator/Desktop/情报数据《84棋牌》/test.xlsx',
#     'C:/Users/Administrator/Desktop/情报数据《668娱乐》'
#       ]
# for p in ll:
#     scaner_file(p)
#
#
# total_df.to_excel('./all_files_668娱乐.xlsx', index=False)


import pandas as pd
from sqlalchemy import create_engine, VARCHAR
import pymysql
pymysql.install_as_MySQLdb()

host = '192.168.224.49'
db = 'spider'
user = 'root'
password = '12345678'

engine = create_engine("mysql://root:12345678@192.168.224.49:33060/spider", echo=True)
conn = engine.connect()


# total_df = pd.read_excel('C:/Users/Administrator/Desktop/image_info1.xlsx')
total_df = pd.DataFrame()
for i in range(2, 9):
    df = pd.read_csv(f'C:/Users/Administrator/Desktop/image_info{i}.csv')
    total_df = total_df.append(df)

# total_df.to_sql('jinsha_chat_info_01', con=conn, if_exists='replace', index=False)
# total_df.to_sql('jinsha_chat_image_info_01', con=conn,if_exists='append', index=False)


for i in range(len(total_df)):
    try:
        total_df.iloc[i:i+1].to_sql(name="jinsha_chat_image_info_01", if_exists='append', con=conn, index=False)
    except:
        print('asdadsaadaadasa!!!!')
        pass

