import scrapy

class Skj520Spider(scrapy.Spider):
    name = "skj520"
    allowed_domains = ["skj520.com"]
    start_urls = ["https://www.skj520.com/a/90673/90673153/758158077.html"]

    def parse(self, response,**kwargs):
        list_items = response.xpath('//*[@id="content"]/text()')
        my_item = LiemingrenItem()