
import easyocr
import requests


reader = easyocr.Reader(['ch_sim', 'en'])     # 没有cpu的话需要加上gpu=False
result = reader.readtext('https://legacy-pics.meiqiausercontent.com/images/347754/hvx3/bFsidZlPiCgSvbJ81rYN.png')
print(result)

for item in result:
    print(item[1])