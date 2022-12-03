import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrBooksSpider(CrawlSpider):
    name = 'cr_books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/index.html']

    rules = (
        Rule( LinkExtractor(restrict_xpaths='//h3/a'),callback='parse_item', follow=False ),

        Rule( LinkExtractor(restrict_xpaths="//li[@class= 'next']/a"), follow = True )

    )

    def parse_item(self, response):
        title = response.xpath("//h1/text()").get()


        yield {
            'title' :title
        }