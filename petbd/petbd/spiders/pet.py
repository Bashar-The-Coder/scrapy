import scrapy


class PetSpider(scrapy.Spider):
    name = 'pet'
    allowed_domains = ['www.pet.com.bd']
    start_urls = ['https://www.pet.com.bd/page/1/?s&post_type=product&product_cat=0']

    def parse(self, response):
        item_card = response.xpath("//div[contains(@class , 'product-grid-item')]")

        for item in item_card:
            title = item.xpath(".//h3[@class = 'wd-entities-title']/a/text()").get()
            price = item.xpath(".//span[@class='price']").getall()

            yield{
                'title' : title,
                'price' : price
            }

            
        next_page = response.xpath("//a[@class='next page-numbers']/@href").get()
        if next_page:
            yield response.follow(next_page, callback= self.parse)