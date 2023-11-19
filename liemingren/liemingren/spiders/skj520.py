import scrapy
from liemingren.items import LiemingrenItem

class Skj520Spider(scrapy.Spider):
    name = "skj520"
    allowed_domains = ["skj520.com"]
    start_urls = ["https://www.skj520.com/a/90673/90673153/724462645.html"]
    def parse(self, response,**kwargs):
        my_item = LiemingrenItem()
        my_item['book'] = response.xpath('//*[@id="content"]/text()').extract()
        #my_item['book'] = response.text
        yield my_item
        href = response.xpath('//*[@id="wrapper"]/div[5]/div[2]/div[3]/ul/li[3]/a/@href')
        new_url = response.urljoin(href.extract())
        my_item['urln'] = new_url
        yield  scrapy.Request(url=new_url,callback=self.parse)
