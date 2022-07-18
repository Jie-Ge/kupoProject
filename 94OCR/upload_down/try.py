# !/usr/bin/python
# -*- coding: utf-8 -*-
import os

import pandas as pd
import numpy as np
import redis
import requests
import re

from sqlalchemy import create_engine



r = redis.Redis('192.168.224.72', port=6379, db=15, password='123456', decode_responses=True)

# r.sadd('image_url', 'asdad')
# r.sadd('image_url', '2343244')

image_progress_total = r.get('image_progress_total')
print(type(image_progress_total))

url_set = r.scard('image_url')
print(type(url_set))

print(int(image_progress_total) - url_set)
