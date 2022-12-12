import scrapy


class SpiderShellSpider(scrapy.Spider):
    name = 'spider_shell'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        pass
