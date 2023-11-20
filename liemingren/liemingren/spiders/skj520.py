import scrapy
from liemingren.items import LiemingrenItem


class Skj520Spider(scrapy.Spider):
    name = "skj520"
    allowed_domains = ["skj520.com"]
    start_urls = ["https://www.skj520.com/a/90673/90673153/index.html"]

    def parse(self, response,**kwargs):

        # html_content = response.text
        # # 将HTML内容写入文件
        # with open('new_file.html', 'w', encoding='utf-8') as file:
        #     file.write(html_content)
        new_urls = response.xpath('//*[@class="listmain"]/dl/dd/a')
        #print(response.xpath('/html/body/div[6]/dl/dd[67]/a/@href').extract_first())
        print("---------------------------------------------------------------------")
        print(new_urls,len(new_urls))
        print("---------------------------------------------------------------------")
        if new_urls != []:
            for new_url in new_urls:
                new_url = response.urljoin(new_url.xpath('@href').extract_first())
                #new_url = response.urljoin(new_url.xpath('@href').extract())
                print("---------------------------------------------------------------------")
                print(new_url)
                print("---------------------------------------------------------------------")
                print("\n")
                yield scrapy.Request(url= new_url,callback=self.xqy_parse)
        else:
            print("NULL\n")

    def xqy_parse(self,resopnse):
        items = LiemingrenItem()
        items['book'] = resopnse.xpath('//*[@class="showtxt"]/text()').extract()
        items['title'] = resopnse.xpath('//*[@class="p"]//text()[2]').extract()
        yield items
