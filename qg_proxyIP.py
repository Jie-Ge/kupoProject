import requests

url = 'https://proxy.qg.net/allocate?Key=1A9FD05A&Num=1&AreaId=&Isp=&DataFormat=json&DataSeparator=&Detail=0&Distinct=0'

res = requests.get(url).json()

print(res)

