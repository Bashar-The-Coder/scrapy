import scrapy

import time
class StartechSpider(scrapy.Spider):
    name = 'startech'
    allowed_domains = ['startech.com.bd']
    start_urls = ['https://www.startech.com.bd/monitor/']

    def parse(self, response):
        monitors = response.xpath("//div[@class='p-item']")
        for monitor in monitors:
            item = monitor.xpath(".//h4[@class = 'p-item-name']/a/text()").get()
            price = monitor.xpath(".//div[@class = 'p-item-price']/span/text()").get()
            
            yield{
                'item' : item,
                'price' : price
            }
            
        next_page = response.xpath("//ul[@class = 'pagination']/li/a/@href").get()
        print (next_page)
        
        if next_page:
            yield response.follow(next_page, callback = self.parse)

