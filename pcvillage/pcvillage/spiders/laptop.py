import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LaptopSpider(CrawlSpider):
    name = 'laptop'
    allowed_domains = ['www.computervillage.com.bd']
    start_urls = ['https://www.computervillage.com.bd/pavilion']

    rules = (
        Rule(LinkExtractor(restrict_xpaths = "//h4[@class='h4 grid-view-item__title text-truncate-2']/a"), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        title = response.xpath("//div [@class ='product-single__meta']/div/h3/text()").get()
        yield {
            'title' : title,
            'url' :response.url
        }
