import scrapy
from main.items import BooksItem
from scrapy.loader import ItemLoader



class ItemloadsSpider(scrapy.Spider):
    name = 'itemloads'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        container = response.xpath ("//article[@class = 'product_pod']")
        for item in container:
            title        = item.xpath(".//h3/a/text()").get()
            rating       = item.xpath(".//div[@class='image_container']/following-sibling::p[1]/@class").get()
            price        = item.xpath(".//p[@class='price_color']").get()
            in_stock     = item.xpath(".//p[@class='instock availability']").get()
            link         = item.xpath(".//h3/a/@href").get()
            link         = response.urljoin(link)
            # yield loader.load_item()
            yield scrapy.Request(url = link , callback = self.parse_item , meta = {
                                                                                    'title' :title,
                                                                                    'rating' : rating,
                                                                                    'price' : price,
                                                                                    'in_stock' : in_stock,
                                                                                    'link' : link        
                                                                                        })

        next_page =  response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            yield response.follow(next_page , callback = self.parse)

    def parse_item(self,response):

        loader = ItemLoader(item = BooksItem() ,  response=response)
        loader.add_value ('title' , response.request.meta['title'])
        loader.add_value ('rating' , response.request.meta['rating'])
        loader.add_value ('price' , response.request.meta['price'])
        loader.add_value ('in_stock' , response.request.meta['in_stock'])
        loader.add_value ('link' , response.request.meta['link'])
        loader.add_xpath('article' , "//article[@class='product_page']/p[1]/text()")
        yield loader.load_item()
