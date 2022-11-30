import scrapy


class AaidSpider(scrapy.Spider):
    name = 'ryansgpu'
    allowed_domains = ['www.ryanscomputers.com']
    start_urls = ['https://www.ryanscomputers.com/category/gaming-desktop-component-graphics-card']

    def parse(self, response):
        item_card = response.xpath("//div[@class = 'cus-col-2 cus-col-3 cus-col-4 cus-col-5 category-single-product mb-2']")
        for item in item_card:
            name = item.xpath(".//p[@class = 'card-text p-0 m-0 grid-view-text']/a/text()").get()
            chipset = item.xpath(".//ul[@class = 'mt-2 mb-2 category-info']/li[1]/text()").get()
            vga_port = item.xpath(".//ul[@class = 'mt-2 mb-2 category-info']/li[2]/text()").get()
            hdmi_port = item.xpath(".//ul[@class = 'mt-2 mb-2 category-info']/li[3]/text()").get()
            capacity = item.xpath(".//ul[@class = 'mt-2 mb-2 category-info']/li[4]/text()").get()
            resoulation = item.xpath(".//ul[@class = 'mt-2 mb-2 category-info']/li[5]/text()").get()
            is_multidisplay_capability = item.xpath(".//ul[@class = 'mt-2 mb-2 category-info']/li[6]/text()").get()
            price = item.xpath(".//p[@class = 'pr-text cat-sp-text pb-1']/text()").get()
            ecommerce_discount = item.xpath(".//span[@title = 'Discount on Special Price for Ecommerce order only']/text()").get()
            ecommerce_discount = ecommerce_discount if ecommerce_discount else "no ecommerce discount"
            product_url = item.xpath(".//p[@class ='card-text p-0 m-0 grid-view-text']/a/@href").get()
            """ yielding all items"""

            yield response.follow(product_url , callback = self.parse_detail, 
                                                                meta = {
                                                                    'name' : name,
                                                                    'chipset': chipset,
                                                                    'vga_port' : vga_port,
                                                                    'hdmi_port' : hdmi_port,
                                                                    'capacity' : capacity,
                                                                    'resulation' : resoulation,
                                                                    'multidisplay' : is_multidisplay_capability,
                                                                    'price' : price,
                                                                    'ecommerce_discount': ecommerce_discount,
                                                                    'url' : product_url
                                                                    } )
        next_page = response.xpath("//a[@rel='next']/@href").get()
        abs_url = response.urljoin(next_page)
        print ("hello world", abs_url)
        if next_page:
            yield response.follow (abs_url , callback = self.parse)

    def parse_detail(self, response):
        prices = response.request.meta['price']
        url = response.request.meta['url']
        discount = response.request.meta['ecommerce_discount']
        resulation = response.request.meta['resulation']

        product_detail_div = response.xpath("//div[@class= 'product_content h-100']")
        product_id = product_detail_div.xpath(".//p/span/text()").get()
        name = product_detail_div.xpath(".//h1/text()").get()
        regular_price = product_detail_div.xpath(".//div[@class='price-block']/span[@class = 'rp-block mb-2']/span/text()").get()
        special_price = product_detail_div.xpath(".//div[@class='price-block mb-2']/span[@class = 'rp-block mb-2']/span[1]/text()").get()

        yield {
            'id': product_id,
            'product_name' : name,
            'price' : prices,
            'url' : url,
            'discount' : discount,
            'resulation' : resulation


        }