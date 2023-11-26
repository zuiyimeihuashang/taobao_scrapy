import scrapy


class KuaidailiSpider(scrapy.Spider):
    name = "kuaidaili"
    allowed_domains = ["kuaidaili.com"]
    start_urls = ["https://kuaidaili.com"]

    def parse(self, response):
        pass
