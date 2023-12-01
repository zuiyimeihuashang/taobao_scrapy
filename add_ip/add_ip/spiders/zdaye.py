import scrapy
from add_ip.items import AddIpItem

class ZdayeSpider(scrapy.Spider):
    name = "zdaye"
    allowed_domains = ["zdaye.com"]
    start_urls = ["https://www.zdaye.com/free/1/"]

    def parse(self, response):
        print("---------------------------------------------------------")
        datas = response.xpath('//*[@id="ipc"]/tbody/tr/td[1]')
        for data in datas:
            items = AddIpItem()
            items["ip_zdy"] = "http://" + str(data.xpath("./text()").extract_first())
            yield items
        print("---------------------------------------------------------")
        for i in range(2,11):
            yield scrapy.Request(url =( "https://www.zdaye.com/free/%d/" % i),callback=self.parse
