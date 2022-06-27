

import time
from multiprocessing import Pool
from tqdm import tqdm
from flask import Flask, make_response, jsonify


total = 10  # 总任务数
tasks = range(total)
pbar = tqdm(total=len(tasks))

pbar.update(1)
print(pbar.n)
pbar.reset(total)
print(pbar.n)