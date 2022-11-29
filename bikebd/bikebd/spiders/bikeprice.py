import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BikepriceSpider(CrawlSpider):
    name = 'bikeprice'
    allowed_domains = ['www.bikebd.com']
    start_urls = ['https://www.bikebd.com/bike-price-in-bd']


    le_get_all_brand_list = LinkExtractor(restrict_css=".text-center >a ")
    rule_book_details   = Rule( le_get_all_brand_list,  follow=True, callback = 'parse_item')

    rules               = ( rule_book_details,

                          )

    def parse_item(self, response):
        print (response.url)



