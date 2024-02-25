# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    symbol = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    price_change = scrapy.Field()
    percentage_price_change = scrapy.Field()
    volume = scrapy.Field()
    market_cap = scrapy.Field()
    
