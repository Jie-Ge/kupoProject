import os
import time
import torch
import torch.nn as nn
import multiprocessing as mp


# 控制模型选择的函数
def train(is_end, gpu_id, model_name):
    if model_name == 'TransE':
        transe_run(gpu_id, model_name)
        transe_run(gpu_id, model_name)
        with is_end.get_lock():
            is_end.value += 1
    elif model_name == 'TransH':
        transh_run(gpu_id, model_name)
        transh_run(gpu_id, model_name)
        transh_run(gpu_id, model_name)
        with is_end.get_lock():
            is_end.value += 1
    else:
        sacn_run(gpu_id, model_name)
        sacn_run(gpu_id, model_name)
        sacn_run(gpu_id, model_name)
        sacn_run(gpu_id, model_name)
        with is_end.get_lock():
            is_end.value += 1


# 父进程中的主函数
def main(os_context):
    # 设置一个共享变量，用来记录完成训练的子进程个数
    is_end = os_context.Value("i", 0)
    # 创建多个子进程
    transe_trainer = os_context.Process(target=train, args=(is_end, 0, 'TransE'))
    transh_trainer = os_context.Process(target=train, args=(is_end, 1, 'TransH'))
    sacn_trainer = os_context.Process(target=train, args=(is_end, 2, 'SACN'))
    # 启动子进程
    transe_trainer.start()
    transh_trainer.start()
    sacn_trainer.start()
    # 下面的代码使得共享变量能够同步更新
    transe_trainer.join()
    transh_trainer.join()
    sacn_trainer.join()
    # 输出完成训练的子进程个数
    print('finish count: %d' % is_end.value)


# 程序入口
if __name__ == '__main__':
    # 输出CPU个数和GPU个数
    print('The machine has %d CPUs.' % os.cpu_count())
    print('The machine has %d GPUs.' % torch.cuda.device_count())
    # 获取操作系统上下文
    context = mp.get_context('spawn')
    # 运行主函数
    main(context)


# 模拟TransE训练
def transe_run(gpu_id, model_name):
    # 设置模型训练所在GPU
    torch.cuda.set_device(gpu_id)
    torch.cuda.is_available()
    print('b train [%s] on gpu[%d]' % (model_name, torch.cuda.current_device()))
    # 模型的初始化
    entity_embedding = nn.Parameter(torch.zeros(2000, 50))
    nn.init.uniform_(tensor=entity_embedding, a=-20, b=20)
    relation_embedding = nn.Parameter(torch.zeros(16, 50))
    nn.init.uniform_(tensor=relation_embedding, a=-20, b=20)
    entity_embedding.cuda(gpu_id)
    relation_embedding.cuda(gpu_id)
    # 模拟模型的训练
    for i in range(100):
        entity_embedding = entity_embedding + torch.tensor([0.1])
        relation_embedding = relation_embedding + torch.tensor([-0.1])
        time.sleep(1.5)
    print('a train [%s] on gpu[%d]' % (model_name, torch.cuda.current_device()))


# 模拟TransH训练
def transh_run(gpu_id, model_name):
    # 设置模型训练所在GPU
    torch.cuda.set_device(gpu_id)
    torch.cuda.is_available()
    print('b train [%s] on gpu[%d]' % (model_name, torch.cuda.current_device()))
    # 模型的初始化
    entity_embedding = nn.Parameter(torch.zeros(2000, 100))
    nn.init.uniform_(tensor=entity_embedding, a=-20, b=20)
    relation_embedding = nn.Parameter(torch.zeros(16, 100))
    nn.init.uniform_(tensor=relation_embedding, a=-20, b=20)
    entity_embedding.cuda(gpu_id)
    relation_embedding.cuda(gpu_id)
    # 模拟模型的训练
    for i in range(100):
        entity_embedding = entity_embedding + torch.tensor([0.1])
        relation_embedding = relation_embedding + torch.tensor([-0.1])
        time.sleep(1.5)
    print('a train [%s] on gpu[%d]' % (model_name, torch.cuda.current_device()))


# 模拟SACN训练
def sacn_run(gpu_id, model_name):
    # 设置模型训练所在GPU
    torch.cuda.set_device(gpu_id)
    torch.cuda.is_available()
    print('b train [%s] on gpu[%d]' % (model_name, torch.cuda.current_device()))
    # 模型的初始化
    entity_embedding = nn.Parameter(torch.zeros(2000, 150))
    nn.init.uniform_(tensor=entity_embedding, a=-20, b=20)
    relation_embedding = nn.Parameter(torch.zeros(16, 150))
    nn.init.uniform_(tensor=relation_embedding, a=-20, b=20)
    entity_embedding.cuda(gpu_id)
    relation_embedding.cuda(gpu_id)
    # 模拟模型的训练
    for i in range(100):
        entity_embedding = entity_embedding + torch.tensor([0.1])
        relation_embedding = relation_embedding + torch.tensor([-0.1])
        time.sleep(1.5)
    print('a train [%s] on gpu[%d]' % (model_name, torch.cuda.current_device()))