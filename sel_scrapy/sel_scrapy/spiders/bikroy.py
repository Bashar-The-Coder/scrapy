import scrapy


class BikroySpider(scrapy.Spider):
    name = 'bikroy'
    allowed_domains = ['x']
    def start_requests(self):
        for i in range (1, 5):
            url = f"https://bikroy.com/bn/ads/bangladesh/mobile-phones?sort=date&order=desc&buy_now=0&urgent=0&page={i}"
            yield  scrapy.Request(url = url , callback=self.parse)

    def parse(self, response):
        container = response.xpath("//li[@class='normal--2QYVk gtm-normal-ad']")
        for item in container:
            title = item.xpath(".//h2[@class='heading--2eONR heading-2--1OnX8 title--3yncE block--3v-Ow']/text()").get()
            price = item.xpath(".//div[@class='price--3SnqI color--t0tGX']/span/text()").get()
            yield {
                'title' : title,
                'price' : price
            }
