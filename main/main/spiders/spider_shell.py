import scrapy
from scrapy.shell import inspect_response # this is so handy. for inspecting response in a shell while parsing

class SpiderShellSpider(scrapy.Spider):
    name = 'spider_shell'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        if ".com" in response.url:
            from scrapy.shell import inspect_response 
            inspect_response(response, self)
