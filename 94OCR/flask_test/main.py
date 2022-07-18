import json
import time
from multiprocessing import Pool

from flask_cors import CORS
from tqdm import tqdm
from flask import Flask, make_response, jsonify

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 跨域问题：前端和后端都要配置允许跨域

@app.route('/run/')
def run():
    """执行任务"""
    print('qqqqqqqqqq')
    msg = {'msg': '数据库中无原数据，请先提交入库！', 'num': None}
    return json.dumps(msg, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True)