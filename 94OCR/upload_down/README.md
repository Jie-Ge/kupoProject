#### 此项目使用步骤

- 启动 flask_app.py
- 访问 http://ip:8080/upload
  - 若想远程访问当前计算机，需要修改 `./templates/upload.html` 文件中的 `ip_port` 变量为当前计算机的IP
  - 若只是本机访问，则将IP设成 `127.0.0.1`
- 每次打开上一步的页面，需要先选择文件并提交，才能点击执行后续功能

- 若想使用GPU识别图片，需要先安装 CUDA 驱动