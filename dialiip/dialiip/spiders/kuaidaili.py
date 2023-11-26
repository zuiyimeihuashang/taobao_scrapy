import scrapy


class KuaidailiSpider(scrapy.Spider):
    name = "kuaidaili"
    allowed_domains = ["kuaidaili.com"]
    start_urls = ["https://www.kuaidaili.com/free/"]

    def parse(self, response):
        pass
