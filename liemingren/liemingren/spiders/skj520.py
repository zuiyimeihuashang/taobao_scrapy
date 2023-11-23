import scrapy
from liemingren.items import LiemingrenItem


class Skj520Spider(scrapy.Spider):
    name = "skj520"
    allowed_domains = ["skj520.com"]
    start_urls = ["https://www.skj520.com/a/90673/90673153/index.html"]

    def parse(self, response,**kwargs):

        new_urls = response.xpath('//*[@class="listmain"]/dl/dd/a')
        #print(response.xpath('/html/body/div[6]/dl/dd[67]/a/@href').extract_first())
        if new_urls != []:
            i = 0
            for new_url in new_urls:
                i += 1
                new_url = response.urljoin(new_url.xpath('@href').extract_first())
                #new_url = response.urljoin(new_url.xpath('@href').extract())
                if i == 964:
                    break
                yield scrapy.Request(url= new_url,callback=self.xqy_parse)
        else:
            print("NULL\n")

    def xqy_parse(self,resopnse):
        items = LiemingrenItem()
        items['book'] = resopnse.xpath('//*[@class="showtxt"]/text()').extract()
        items['title'] = resopnse.xpath('//*[@class="content"]/h1/text()').extract_first()
        yield items