import scrapy
from fake_useragent import UserAgent
import random
from scrapy import FormRequest, Request
import json
from icon_scrapy.items import IconScrapyItem

ua = UserAgent()


class IconSpiderSpider(scrapy.Spider):
    name = 'icon_spider'
    # allowed_domains = ['www.xx.coom']
    start_urls = ['https://apilist.tronscan.org/api/tokens/overview']
    url = 'https://apilist.tronscan.org/api/tokens/overview'

    user_agent = random.choice(ua.data_browsers['chrome'])
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'Host': 'apilist.tronscan.org',
            'Origin': 'https://tronscan.org',
            'Referer': 'https://tronscan.org/',
            'User-Agent': user_agent

        }
    }

    def start_requests(self):
        start = 0
        while start <= 78040:
            params = {
                'start': str(start),
                'limit': '20',
                'verifier': 'all',
                'order': 'desc',
                'filter': 'trc20',
                'sort': 'marketcap',
                'order_current': 'descend'
            }
            yield FormRequest(url=self.url, formdata=params, callback=self.parse, method='get')
            start += 20

    def parse(self, response):
        data = json.loads(response.text)
        item = IconScrapyItem()
        for tokens in data['tokens']:
            item['name'] = tokens['name']
            item['abbr'] = tokens['abbr']
            item['Token_Holders'] = tokens['nrOfTokenHolders']
            item['Contract'] = tokens['contractAddress']
            item['Decimal_Places'] = tokens['decimal']
            item['Official_Website'] = tokens['projectSite']
            item['White_Pape'] = tokens['whitePaper']
            item['imgUrl'] = tokens['imgUrl']
            print(item)

            return item
