import scrapy
from requests import HTTPError

class ErrorSpider(scrapy.Spider):
    name = 'error'
    allowed_domains = ['bangladeshyellowpages.com']
    def start_requests(self):
        urls = [
            'http://bangladeshyellowpages.com/business.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        categories = response.xpath("//div[@class='category-list']")

        for category in categories:
            link = category.xpath(".//a/@href").get()
            yield response.follow(link, callback = self.parse_address)

    def parse_address(self, response):
        industries = response.xpath("//div[@class = 'cate-list']/div[@class='cate-list-top']/div[@class='row']")

        for ind in industries:
            if response.status != 200:
                break
            ind_name = ind.xpath (".//[@class='col-md-12']/a/@href").get()

            yield {
                'ind' : ind_name
            }
