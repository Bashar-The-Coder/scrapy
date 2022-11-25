import scrapy


class FixitSpider(scrapy.Spider):
    name = 'fixit'
    allowed_domains = ['fixit.com.bd']
    start_urls = ['https://fixit.com.bd/?s=yato&post_type=product']

# //div[@class = 'bg-white product-main-wrap']//div[@class='product-info-wrap']/a/h2/text()

    def parse(self, response):
        items = response.xpath("//div[@class = 'bg-white product-main-wrap']")
        
        for item in items:
            
            item_name = item.xpath(".//div[@class='product-info-wrap']/a/h2/text()").get()
            price = item.xpath(".//div[@class='product-info-wrap']/span[@class='price']/span/bdi/text()").get()
            
            yield{
                'namel' : item_name,
                'price' : price
                
            }

        next_page = response.xpath("//li/a[@class='next page-numbers']/@href").get()
        abs_url = response.urljoin(next_page)
        if next_page:
            yield (scrapy.Request(next , callback = self.parse))