# !/usr/bin/python
# -*- coding: utf-8 -*-
import os
import uuid

from flask import Flask, request, send_from_directory
from flask import render_template
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder="templates")

# 设置文件上传保存路径
app.config['UPLOAD_FOLDER'] = 'upload/'
# MAX_CONTENT_LENGTH设置上传文件的大小，单位字节
# app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        # file为上传表单的name属性值
        f = request.files['file']
        print('f: ', f)
        print('f.filename: ', f.filename)
        # fname = secure_filename(f.filename)
        # print('fname: ', fname)
        # ext = fname.rsplit('.')[-1]
        # # 生成一个uuid作为文件名
        # fileName = str(uuid.uuid4()) + "." + ext
        # os.path.join拼接地址，上传地址，f.filename获取文件名
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return 'ok'


# 图片下载
@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    if request.method == "GET":
        path = os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if path:
            return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, port=8080)  # debug: flask服务器会在修改代码之后自动重启，并且当应用出错时还会提供一个 有用的调试器