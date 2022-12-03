import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urlencode

#scraper api
SCRAPER_API_KEY = '1fb55a799e4bf83bea437f4835c3aa8c'

def get_scraperapi_url(url):
    payload = {'api_key': SCRAPER_API_KEY, 'url': url}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url

#scrapeops api
SCRAPE_OPS_API_KEY = '73904be3-d285-4c20-9940-5c82d64ece85'
def get_scrapeops_url(url):
    payload = {'api_key': SCRAPE_OPS_API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url




class BdCrawlSpider(CrawlSpider):
    name = 'bd_crawl'
    allowed_domains = ['x']
    start_urls = ['http://x/']
    api_key = ''
    url = "http://bangladeshyellowpages.com/business.html"

    def start_requests(self):
        yield scrapy.Request(url = "https://proxy.scrapeops.io/v1/" , params={ 'api_key': self.api_key, 'url' : self.url })

    rules = (
        Rule(LinkExtractor(allow=r'bangladesh/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print (response.url)


