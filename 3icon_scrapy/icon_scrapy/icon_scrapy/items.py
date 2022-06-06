# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IconScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    abbr = scrapy.Field()
    Token_Holders = scrapy.Field()
    imgUrl = scrapy.Field()
    Contract = scrapy.Field()
    Decimal_Places = scrapy.Field()
    Official_Website = scrapy.Field()
    White_Pape = scrapy.Field()
