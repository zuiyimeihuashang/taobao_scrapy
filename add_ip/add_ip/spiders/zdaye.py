import scrapy


class ZdayeSpider(scrapy.Spider):
    name = "zdaye"
    allowed_domains = ["zdaye.com"]
    start_urls = ["https://www.zdaye.com/free/10/"]

    def parse(self, response):
        pass
