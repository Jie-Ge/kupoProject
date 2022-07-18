

import redis

r = redis.Redis(host="192.168.224.72", port=6379, db=15, password='123456', decode_responses=True)

r.sadd('customer_login', 'support-sys-客服登录_321387_2022-01-01_2022-06-30_1656574371.xlsx')
r.sadd('customer_login', 'support-sys-客服登录_269663_2022-01-01_2022-06-30_1656574387.xlsx')
r.sadd('customer_login', 'support-sys-客服登录_299265_2021-10-01_2022-03-09_1646820454.xlsx')

r.sadd('mysql_table_name', '永利集团269663_历史对话_269663')
r.sadd('mysql_table_name', '500彩票321387_历史对话_321387')
r.sadd('mysql_table_name', 'ID299265-新葡京_历史对话_299265')