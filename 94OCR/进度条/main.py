import time
from multiprocessing import Pool
from tqdm import tqdm
from flask import Flask, make_response, jsonify

app = Flask(__name__)

def do_work(x):
    time.sleep(1)
    return x

total = 10  # 总任务数
tasks = range(total)
pbar = tqdm(total=len(tasks))

@app.route('/run/')
def run():
    """执行任务"""
    global pbar
    results = []
    print('n: ', pbar.n)
    print('total: ', total)
    with Pool(processes=1) as pool:
        for _result in pool.imap_unordered(do_work, tasks):
            results.append(_result)
            if pbar.n >= total:
                pbar.n = 0  # 重置
            pbar.update(1)
    response = make_response(jsonify(dict(results=results)))
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response

@app.route('/progress/')
def progress():
    """查看进度"""
    global pbar
    print('1n: ', pbar.n)
    print('1total: ', pbar.total)
    response = make_response(jsonify(dict(n=pbar.n, total=pbar.total)))
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response


if __name__ == '__main__':
    app.run()