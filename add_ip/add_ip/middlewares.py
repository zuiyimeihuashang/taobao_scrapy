# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class AddIpSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class AddIpDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        cookies_dict ={
            'cookie':'__51vcke__20L1wEeeGTFXijbh=c1c68ba9-91ce-55ee-b6c0-b5d6d829265c; __51vuft__20L1wEeeGTFXijbh=1696753781937; __root_domain_v=.zdaye.com; _qddaz=QD.145896753782028; lastSE=baidu; acw_tc=76b20f6617011833555744970e47752909b9361df36ce2b8e61708b3aa26a5; __51uvsct__20L1wEeeGTFXijbh=6; Hm_lvt_dd5f60791e15b399bf200ae217689c2f=1701165074,1701172792,1701178837,1701183357; _qdda=3-1.1; _qddab=3-uedsw4.lpignb01; ASPSESSIONIDSEASARTD=FOGGGDPCDCOEEIFBNFKFCPBM; __vtins__20L1wEeeGTFXijbh=%7B%22sid%22%3A%20%220e159238-3953-5ac8-bc3f-abcaf150bcb8%22%2C%20%22vd%22%3A%202%2C%20%22stt%22%3A%203784%2C%20%22dr%22%3A%203784%2C%20%22expires%22%3A%201701185160255%2C%20%22ct%22%3A%201701183360255%7D; Hm_lpvt_dd5f60791e15b399bf200ae217689c2f=1701183360',
        }
        request.cookies = cookies_dict
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
