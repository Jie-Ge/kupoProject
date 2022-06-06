
import json

data = []
for i in range(1, 6):
    with open(f'./coin_desc{i}.json', 'r', encoding='utf-8') as f:
        d1 = json.load(f)
        data += d1

with open('./coin_desc.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)

# 查看数据条数
with open(f'./coin_desc.json', 'r', encoding='utf-8') as f:
    d1 = json.load(f)
    print(len(d1))