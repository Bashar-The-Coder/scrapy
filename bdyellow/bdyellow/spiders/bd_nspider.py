from requests import HTTPError
import scrapy

from urllib.parse import urlencode
# this is scraperapi api key
API_KEY = '1fb55a799e4bf83bea437f4835c3aa8c'

def get_proxy_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url


class BdNspiderSpider(scrapy.Spider):
    name = 'bd_nspider'
    allowed_domains = ['bangladeshyellowpages.com']
    def start_requests(self):
        urls = [
            'http://bangladeshyellowpages.com/business.html',
        ]
        for url in urls:
            yield scrapy.Request(url=get_proxy_url(url), callback=self.parse)

    def parse(self, response):
        categories = response.xpath("//div[@class='category-list']")

        for category in categories:
            link = category.xpath(".//a/@href").get()
            yield response.follow(link, callback = self.parse_address)

    def parse_address(self, response):
        industries = response.xpath("//div[@class = 'cate-list']/div[@class='cate-list-top']/div[@class='row']")

        for ind in industries:
            try:
           
                ind_name = ind.xpath (".//div[@class='row']/div/div/div[@class='col-md-12']/a/text()").get()
            except HTTPError as e:
                print ("service unavailable")
            finally:
                ind_name = ind.xpath (".//div[@class='row']/div/div/div[@class='col-md-12']/a/text()").get()

                yield {
                    'ind' : ind_name
                }
