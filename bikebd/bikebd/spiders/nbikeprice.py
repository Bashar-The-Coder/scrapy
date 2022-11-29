import scrapy


class NbikepriceSpider(scrapy.Spider):
    name = 'nbikeprice'
    allowed_domains = ['x']
    start_urls = ['http://x/']

    def parse(self, response):
        pass
