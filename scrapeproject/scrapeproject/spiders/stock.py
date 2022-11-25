import scrapy


class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['dse.com.bd']
    start_urls = ['http://www.dse.com.bd/dseX_share.php/']

    def parse(self, response):
        table = response.xpath("//table[@class ='table table-bordered background-white shares-table']")
        
        for data in table:
            b_name = data.xpath(".//td/a/text()").get()
            print (b_name)
            
            yield {
                'name' : b_name
            }
