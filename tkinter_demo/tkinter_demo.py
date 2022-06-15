#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
改变控件状态: https://blog.csdn.net/qq_21238607/article/details/108824662

'''


# Python2.x 导入方法
import tkinter as tk  # 导入 Tkinter 库
from tkinter.messagebox import showinfo, showwarning, showerror
from tkinter import *

# Python3.x 导入方法

window = tk.Tk()  # 创建窗口对象的背景色
window.title('my tkinter')
# 窗口设置长宽以及窗口在屏幕的位置
window.geometry("580x350+630+80")  # 长x宽+x*y

var = tk.StringVar()  # 定义一个字符串变量


def req_html():
    var = e.get()
    if not var.startswith('http://') and not var.startswith('https://'):
        tk.messagebox.showwarning(title='警告', message='请输入正确的网址！')

    else:
        # 颜色: https://www.cnblogs.com/wilson-wu/p/8343470.html
        btn.configure(state=DISABLED, bg='#DCDCDC')

        t.insert('insert', f'开始下载网站{var}......\n')
        insert_point()

id_ = ''
count = 0
def insert_point():
    global count, id_
    # var = e.get()
    # t.delete(1.0, tk.END)  # 清空文本框，有些系统或版本只能识别 1.0
    # t.insert('insert', var)

    btn1.configure(state=NORMAL)
    btn2.configure(state=DISABLED)

    count += 1
    ss = f'正在下载第{count}个url\n'
    t.insert('end', ss)  # 插入到文本框的末尾（'end' 同 tk.END）
    t.see("end")  # 实现显示超出文本框的内容
    id_ = window.after(1000, insert_point)  # 每隔1s调用函数 insert_point 自身


def pause():
    global id_
    btn1.configure(state=DISABLED)
    btn2.configure(state=NORMAL)

    t.insert(tk.END, '程序已暂停！\n')
    window.after_cancel(id_)


def insert_end():
    global count
    # window.withdraw()  # ****实现主窗口隐藏(即隐藏带tk标题的空白窗口)
    # window.update()  # *********需要update一下
    r = tk.messagebox.askyesno(title='询问', message='确定要结束下载？')
    if r:
        count = 0
        t.insert(tk.END, '下载结束！\n')
        window.after_cancel(id_)

        btn.configure(state=NORMAL)
        btn1.configure(state=DISABLED)
        btn2.configure(state=DISABLED)


lb = tk.Label(window, text='请输入网址：')

url = tk.StringVar()
url.set('https://www.baidu.com')
e = tk.Entry(window, width=30, textvariable=url)

btn = tk.Button(window,
                text='开始下载',
                # width=15, height=2,
                command=req_html)

btn1 = tk.Button(window,
                 text='暂停',
                 command=pause,
                 state=DISABLED,
                 bg='#DCDCDC')

btn2 = tk.Button(window,
                 text='继续',
                 command=insert_point,
                 state=DISABLED,
                 bg='#DCDCDC')

btn3 = tk.Button(window,
                 text='结束下载',
                 command=insert_end)

t = tk.Text(window, height=20, width=75)

# 创建滚动条
scroll = tk.Scrollbar(orient="vertical")
# 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
scroll.config(command=t.yview)
# 将滚动条关联到文本框
t.config(yscrollcommand=scroll.set)


lb.grid(row=1, column=1, pady=20, padx=10)
# padx: x轴外边距； ipady：y轴内边距
e.grid(row=1, column=2, padx=5)
btn.grid(row=1, column=3, padx=5)
btn1.grid(row=1, column=4, padx=5)
btn2.grid(row=1, column=5, padx=5)
btn3.grid(row=1, column=6, padx=5)
t.grid(row=2, column=1, columnspan=6, padx=10)
# t.grid(x=20, y=80)  # 布局，显示的起始位置

'''
sticky=N+S 拉高组件，让组件上下填充到表格框的顶端和底端。
sticky=N+S+E 拉高组件，让组件上下填充到表格框的顶端和底端，同时，让组件靠右对齐。
sticky=N+W+W+E 拉高并拉长组件，让组件填充满一个表格框。
'''
scroll.grid(row=2, column=6, sticky=N+S+E)


def customized_function():
    r = tk.messagebox.askyesno(title='询问', message='确定要关闭窗口？')
    if r:
        window.destroy()


window.protocol('WM_DELETE_WINDOW', customized_function)
window.mainloop()  # 进入消息循环（显示窗口）
