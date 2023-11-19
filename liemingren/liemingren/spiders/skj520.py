import scrapy
from liemingren.liemingren.items import liemingrenItem

class Skj520Spider(scrapy.Spider):
    name = "skj520"
    allowed_domains = ["skj520.com"]
    start_urls = ["https://www.skj520.com/a/90673/90673153/758158077.html"]

    def parse(self, response,**kwargs):
        list_items = response.xpath('//*[@id="content"]/text()')
        my_item = liemingrenItem()
        my_item['data'] = list_items.xpath('//*[@id="content"]/text()').extract()
        yield my_item
        href = response.css('//*[@id="wrapper"]/div[5]/div[2]/div[3]/ul/li[3]/a')
        url = response.urljoin(href.extract_first())
        yield scrapy.Request(url=url)  
        