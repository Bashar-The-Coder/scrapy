import scrapy


class LaptopsSpider(scrapy.Spider):
    name = 'laptops'
    allowed_domains = ['x']
    start_urls = ['http://x/']

    def parse(self, response):
        pass
