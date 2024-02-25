import scrapy
import json
from scrapy.selector import Selector


class CoachSpider(scrapy.Spider):
    name = "coach"
    allowed_domains = ["www.bhs.org.uk"]
    start_urls = ["https://www.bhs.org.uk/api/contentfilter/get?id=1419&page=1"]

    def parse(self, response):

        data = json.loads(response.body)
        html_content = data.get("html")
        if html_content:
            selector = Selector(text=html_content)
            
        coach_page_urls = selector.xpath('//a[contains(@class, "m-card m-card--coach")]/@href').getall()
        for url in coach_page_urls:
            domain = "https://www.bhs.org.uk/"
            url = domain + url
            yield scrapy.Request(url, callback=self.parse_coach_page, meta={'data': data})

    def parse_coach_page(self, response):
        data = response.meta.get('data')

        name = response.xpath("//h1/text()").get().strip()
        qualification = response.xpath('//i[contains(@class, "icon-star")]/following-sibling::span/text()').get().strip()
        phone = response.xpath('//i[contains(@class, "icon-phone")]/following-sibling::span/text()').get().strip()
        email = response.xpath('//i[contains(@class, "icon-mail")]/following-sibling::span/a/text()').get().strip()

        yield {
            'name': name,
            'email': email,
            "qualification": qualification,
            "phone": phone
        }

        next_page_url = data.get("next")
        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse)
