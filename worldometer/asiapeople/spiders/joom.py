import scrapy


class JoomSpider(scrapy.Spider):
    name = 'joom'
    allowed_domains = ['joom.com']
    start_urls = ['https://www.joom.com/en/best/spain-t-shirts']

    def parse(self, response):
        products = response.xpath("//div[@class='product___FMuVK product___QZMb0']")
        for product in products:
            name = product.xpath(".//div[@class='name___vIcd9']/text()").get()
            price = product.xpath("//div[@class='price___XVu2a']/span[last()]/text()").get()
            yield{
                'name' : name,
                'price' : price
            }

        
        next_page = response.xpath ("//a[@class='button___HyMJo']/@href").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)       

        house_hold_product = response.xpath ("//a[@class='category___vfPOI'][position()=3]/@href").get()
        house_hold_product = response.urljoin(house_hold_product)
        yield scrapy.Request(house_hold_product, callback=self.parse)   