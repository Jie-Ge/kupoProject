
import easyocr
import requests
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import os
import torch


def train(gpu_id):
    # 设置模型训练所在GPU
    torch.cuda.set_device(gpu_id)
    torch.cuda.is_available()
    print('being train on gpu[%d]' % (torch.cuda.current_device()))

    reader = easyocr.Reader(['ch_sim', 'en'], gpu=True)     # 没有cpu的话需要加上gpu=False
    # device = reader.device(gpu_id)

    while True:
        result = reader.readtext('https://legacy-pics.meiqiausercontent.com/images/347754/hvx3/bFsidZlPiCgSvbJ81rYN.png')
        print(result)


def main(os_context):
    # 创建多个子进程

    pp = []
    for i in range(5):
        p = os_context.Process(target=train, args=(0,))
        p.start()
        pp.append(p)

    for p in pp:
        p.join()


# 程序入口
if __name__ == '__main__':
    print('1111111')
    # 输出CPU个数和GPU个数
    print('The machine has %d CPUs.' % os.cpu_count())
    print('The machine has %d GPUs.' % torch.cuda.device_count())
    # 获取操作系统上下文
    context = multiprocessing.get_context('spawn')
    print('context: ', context)
    # 运行主函数
    main(context)

