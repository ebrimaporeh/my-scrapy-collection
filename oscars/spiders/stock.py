import scrapy
from oscars.items import StockItem

class StockSpider(scrapy.Spider):
    name = "stock"
    allowed_domains = ["finance.yahoo.com"]

    start_urls = ["https://finance.yahoo.com/most-active/?count=100"]

    def parse(self, response):
        table_row = response.xpath("//tr[contains(@class, 'simpTblRow')]")

        for data in table_row:
            symbol = data.xpath("./td[contains(@aria-label,'Symbol')]//a/text()").get()
            name = data.xpath("./td[contains(@aria-label,'Name')]/text()").get()
            price = data.xpath("./td[contains(@aria-label,'Price')]//span/text()").get()
            price_change = data.xpath("./td[contains(@aria-label,'Change')]//fin-streamer//span/text()").get()
            percentage_price_change = data.xpath("./td[contains(@aria-label,'% Change')]//fin-streamer//span/text()").get()
            volume = data.xpath("./td[contains(@aria-label,'Volume')]//fin-streamer/text()").get()
            market_cap = data.xpath("./td[contains(@aria-label,'Market Cap')]//fin-streamer/text()").get()


            stock_items = StockItem()

            stock_items['symbol'] = symbol
            stock_items['name'] = name
            stock_items['price'] = price
            stock_items['price_change'] = price_change
            stock_items['percentage_price_change'] = percentage_price_change
            stock_items['volume'] = volume
            stock_items['market_cap'] = market_cap

            yield stock_items
    
       
