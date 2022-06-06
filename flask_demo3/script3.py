from flask import Flask, request
from flask_cors import *
import json
import requests
from lxml import etree

'''
使用request接收前端post请求
直接使用return发送后端处理好的数据给前端
'''

# flask服务启动，进行初始化
app = Flask(__name__)
CORS(app, supports_credentials=True)  # 跨域问题：后端和服务器都要配置允许跨域


# 通过python装饰器的方法定义一个路由地址，如http://127.0.0.1/test就是接口的url
@app.route('/api/', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        args_dic = json.loads(request.form.get('data'))
        print(args_dic)
        result = request_page(args_dic)
        # result = json.dumps(result, ensure_ascii=False)  # 转化为字符串格式
        # data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        # result = json.dumps(data)
        print(result)
        return result  # return会直接把处理好的数据返回给前端
    else:
        return " it's not a POST request! "


def request_page(data_dic):
    url = data_dic['url']
    res = requests.get(url)
    res.encoding = "utf-8"
    page = etree.HTML(res.text)
    title = page.xpath('//title/text()')[0]
    return title

## 还得增加日志功能（flask自带日志功能），异常检测

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)  # 可以设置为本机IP，或者127.0.0.1