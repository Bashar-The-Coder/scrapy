import scrapy


class JsquotesSpider(scrapy.Spider):
    name = 'jsquotes'
    allowed_domains = ['x']
    start_urls = ['http://x/']

    def parse(self, response):
        pass
