import scrapy


class CyclebdNsSpider(scrapy.Spider):
    name = 'cyclebd'
    allowed_domains = ['www.motorcyclebd.com']
    start_urls = ['https://www.motorcyclebd.com/brands/']

    def parse(self, response):
        all_brand = response.xpath("//div[@class ='col-md-3 col-sm-3 col-xs-6']")

        for brand in all_brand:
            brand_name = brand.xpath(".//b/a/text()").get()
            brand_name_link = brand.xpath(".//div[@class = 'brand-thumb']/a/@href").get()

            yield response.follow(brand_name_link, callback = self.parseBrand)
            
    def parseBrand(self, response):
        bikes = response.xpath("//div[@class ='col-md-13 col-sm-4 col-xs-6']")
        for bike in bikes:
            bike_detail = bike.xpath(".//div[@class = 'bike-name']/text()").get()
            bike_price = bike.xpath(".//div[@class = 'bike-price']/text()").get()
            bike_price = bike_price.replace('\n' , '').replace('\t' ,'')
            bike_detail_link = bike.xpath(".//div[@class = 'product-thumb']/a/@href").get()
            for_bike_spec_url = bike_detail_link.split("/")
            for_bike_spec_url.insert(3, "specs")
            for_bike_spec_url = "/".join(for_bike_spec_url)
            yield scrapy.Requst(url = for_bike_spec_url, callback = self.parseDetail, meta = {  'bike_full_name' : bike_detail,
                                                                                                'price' : bike_price,
                                                                                               'link' : for_bike_spec_url} )

            # # yield {
            #     'bike_full_name' : bike_detail,
            #     'price' : bike_price,
            #     'link' : for_bike_spec_url
            # # }
    def parseDetail(self, response):
        specs = response.xpath

        for detail in response