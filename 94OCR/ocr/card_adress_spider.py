import requests
import json

def get_card_address(card_id):
    url = f"https://api.kazhiguo.com/api/bankcard/apikey=ef93e0ba04c6662ffe75f03d00d3acc1&bankcard={card_id}"
    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    while True:
        try:
            response = requests.get(url=url, headers=headers, timeout=10)
            break
        except:
            pass
    item = {}
    json_data = response.json()
    item['卡号'] = card_id
    item['归属地'] = json_data['result']['address']
    item['银行名称'] = json_data['result']['bank_name']
    item['银行卡名称'] = json_data['result']['card_name']
    item['银行卡类型'] = json_data['result']['card_type']

    return item['归属地']

if __name__ == '__main__':
    get_card_address('aaa')