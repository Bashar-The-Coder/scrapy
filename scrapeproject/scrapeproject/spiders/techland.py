import scrapy


class TechlandSpider(scrapy.Spider):
    name = 'techland'
    allowed_domains = ['techlandbd.com']
    start_urls = ['http://www.techlandbd.com/computer-monitor/']

    def parse(self, response):
        div = response.xpath ("//div[@class= 'product-thumb']")
        for item in div:
            item_name = item.xpath(".//*[@class = 'name']/a/text()").get()
            link = item.xpath("./div[@class='caption']/div[@class = 'name']/a/@href").get()
            price = item.xpath (".//span[@class='price-new']/text()").get()
            # //div[@class='product-thumb']/div[@class='caption']/div[@class = 'name']/a/@href
            # yield {
            #     'item' : item_name,
            #     'link' : link,
            #     'price' : price
            # }
            yield scrapy.Request(link, callback = self.parse_item, meta={
                'itemt' : item_name , 'links' : link, 'pricex' : price})
            # yield scrapy.Request( url(link), callback = self.parse_item)
            
        next_page = response.xpath("//li/a[@class='next']/@href").get()
        if next_page is not None:
            yield response.follow(next_page , callback=self.parse)

    def parse_item(self, response):
        items = response.request.meta['itemt']
        links = response.request.meta['links']
        price = response.request.meta['pricex']
        # item_nam = response.request.meta['item_nam']
        # item_price = response.request.meta['price']
        desc = response.xpath("//div[@class = 'block-content  block-description']/p[1]/text()").get()

        
        yield {
            'item' : items,
            'prices' : price,
            'description' : desc
        }
                
                    
            

