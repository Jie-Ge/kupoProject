# !/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
import uuid
from io import BytesIO

from flask import Flask, request, send_from_directory, jsonify, send_file, make_response
from flask import render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
from read_files import put_mysql
from ip_adress import get_ip_addr
from ocr.main_ocr import parse_image_info
from ocr.card_adress_spider import get_card_address
from ocr import extract_image_info_all
from generate_data_file import get_date_file
import redis
import zipfile

app = Flask(__name__, template_folder="templates", static_folder='static')
CORS(app, supports_credentials=True)  # 跨域问题：前端和后端都要配置允许跨域

# 设置文件上传保存路径
app.config['UPLOAD_FOLDER'] = './'
# 设置文件下载路径
app.config['DOWN_FOLDER'] = 'data/'
# MAX_CONTENT_LENGTH设置上传文件的大小，单位字节
# app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config["JSON_AS_ASCII"] = False  # 支持中文


r = redis.Redis(host="192.168.224.72", port=6379, db=15, password='123456', decode_responses=True)
filename = None
# http://127.0.0.1:8080/upload
# http://192.168.224.80:8080/upload
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    global filename
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        # file为上传表单的name属性值
        f = request.files['file']

        filename = f.filename.rsplit('.')[0]

        if f.filename.rsplit('.')[-1] != 'zip':
            return jsonify({"num": 4, "msg": "上传失败，上传的不是zip文件"})

        # os.path.join拼接地址，上传地址，f.filename获取文件名
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        if os.path.exists(save_path):
            return jsonify({"num": 1, "msg": "上传失败，上传的文件已存在"})  # 当post请求时，需要用jsonify()

        f.save(save_path)
        msg_dic = put_mysql(filename)
        code = msg_dic['num']
        status_msg = msg_dic['msg']
        return jsonify({"num": 2, "msg": f"{status_msg}"})


@app.route('/ipaddress/', methods=['GET'])
def ipaddress():
    if request.method == "GET":
        table_set = r.smembers('mysql_table_name')

        msg = '数据库中无原数据，请先提交入库！'
        for table_name in table_set:
            if table_name.split('_')[0] == filename:
                msg = get_ip_addr(table_name)
        return msg


@app.route('/parseimage/', methods=['GET'])
def parseimage():
    if request.method == "GET":
        table_set = r.smembers('mysql_table_name')

        msg = '数据库中无原数据，请先提交入库！'
        for table_name in table_set:
            if table_name.split('_')[0] == filename:
                msg_dic = parse_image_info(table_name)
                code = msg_dic['num']
                msg = msg_dic['msg']
        return msg


@app.route('/bankaddress/', methods=['GET'])
def bankaddress():
    if request.method == "GET":
        table_set = r.smembers('mysql_table_name')

        msg = '数据库中无原数据，请先提交入库！'
        for table_name in table_set:
            if table_name.split('_')[0] == filename:
                msg = get_card_address(table_name)
        return msg


@app.route('/datafile/', methods=['GET'])
def datafile():
    if request.method == "GET":
        table_set = r.smembers('mysql_table_name')

        msg = '数据库中无原数据，请先提交入库！'
        zipfilename = 'default_name111'
        for table_name in table_set:
            if table_name.split('_')[0] == filename:
                msg_dic = get_date_file(table_name)
                msg = msg_dic['msg']
                zipfilename = msg_dic['file_name']
        return json.dumps({
                "msg": msg,
                "filename": zipfilename
            }, ensure_ascii=False)


# http://127.0.0.1:8080/download/
@app.route('/download/', methods=['GET'])
def download():
    if request.method == "GET":
        if not filename:
            return '请先选择文件，并提交！'

        is_exists_path = False
        table_set = r.smembers('mysql_table_name')
        for table_name in table_set:
            if table_name.split('_')[0] == filename:
                memory_file = BytesIO()
                with zipfile.ZipFile(memory_file, "w", zipfile.ZIP_DEFLATED) as zf:
                    for file_dir in [f'{table_name}_平台.xlsx', f'{table_name}_赌客.xlsx']:
                        data_dir = os.path.join(app.config['DOWN_FOLDER'], file_dir)
                        if os.path.exists(data_dir):
                            is_exists_path = True
                            zf.write(data_dir)
                memory_file.seek(0)
                if is_exists_path:
                    return send_file(memory_file, attachment_filename='zip.zip', as_attachment=True)

        if not is_exists_path:
            return json.dumps({
                "msg": "下载的文件不存在",
                "num": 3
            }, ensure_ascii=False)


@app.route('/progress_bar/', methods=['POST'])
def upload_progress():
    if request.method == "POST":
        args_dic = json.loads(request.form.get('data'))
        key_n = args_dic['key_n']
        key_total = args_dic['key_total']
        return json.dumps({
                key_n: r.get(key_n),
                key_total: r.get(key_total)
            }, ensure_ascii=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)  # debug: flask服务器会在修改代码之后自动重启，并且当应用出错时还会提供一个 有用的调试器