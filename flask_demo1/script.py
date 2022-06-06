#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="templates")

"""
这是一个展示Flask如何读取服务器本地图片, 并返回图片流给前端显示的例子
"""


def return_img_stream(img_local_path):
    """
    工具函数:
    获取本地图片流
    :param img_local_path:文件单张图片的本地绝对路径
    :return: 图片流
    """
    import base64
    img_stream = ''
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode()
    return img_stream


@app.route('/')
def hello_world():
    img_path = './dog.jpg'
    img_stream = return_img_stream(img_path)
    return render_template('index.html',  # 要放在一个 templates 文件夹中
                           img_stream1=img_stream)  # img_stream1 为 html 文件中的参数名


if __name__ == '__main__':
    app.run(debug=True, port=8080)  # debug: flask服务器会在修改代码之后自动重启，并且当应用出错时还会提供一个 有用的调试器
