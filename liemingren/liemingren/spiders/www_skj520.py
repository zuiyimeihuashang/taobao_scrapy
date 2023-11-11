import scrapy


class WwwSkj520Spider(scrapy.Spider):
    name = "www.skj520"
    allowed_domains = ["www.skj520.com"]
    start_urls = ["https://www.skj520.com"]

    def parse(self, response):
       sel = Selector(response)
