### 1aml.zklatech.com
- selenium

### 3icon_
- xlsx、xlsx去重（防止将 url 存储为超链接（若为超链接，代开xlsx会报错））、文件夹下文件个数

### 4icon_2
- 创建文件、xlsx表格

### 6telegram_msg
- 电报telegram相关数据、程序自动分表存储（按记录条数分表）

### 7coin_introduce
- 保存数据到json文件、合并json文件


### 9bscscan.com
- 网站：https://bscscan.com/token/0x3ee2200efb3400fabb9aacf31297cbdd1d435d47
- 技术：重新启动程序，爬虫接着运行（而不是从头开始）、代理的使用、大量请求、csv、进程与线程配合、请求失败重试
- 难点：此网站限速严重。多线程共享内存变量，减少线程数会大大减少爬取速度。
  - 解决方法：开启多进程，再在每个进程中开启多线程，每个进程使用不同的代理IP，这样可以降低每个代理IP的请求速度；每个多进程的线程开少一点，只要内存够，进程可以无限开

### 93www.mytokencap.com
- 参数加密、webpack

### 94OCR
- 图像文字识别、接口API、遍历文件夹中文件、pandas合并文件、pandas保存数据到数据库、ip归属地、vthread多线程
- flask、日志