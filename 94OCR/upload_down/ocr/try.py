# !/usr/bin/python
# -*- coding: utf-8 -*-
import re

import pandas as pd
import redis
import time

from utils_mysql import select_db_recode, insert_db_recode


# r = redis.Redis('192.168.224.72', port=6379, db=15, password='123456', decode_responses=True)
#
#
# r.sadd('image_flag', '永利集团269663_历史对话_269663' + '_image_flag')

df = pd.DataFrame({'a': [1,2,3],
                   'b': [4,5,6]})


if not df.empty:
    print('asdada')