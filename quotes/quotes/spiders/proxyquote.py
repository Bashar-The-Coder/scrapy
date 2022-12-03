import scrapy
import logging
from urllib.parse import urlencode


#scraper api
SCRAPER_API_KEY     = '1fb55a799e4bf83bea437f4835c3aa8c'

def get_scraperapi_url(url):
    payload         = {'api_key': SCRAPER_API_KEY, 'url': url}
    proxy_url       = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url

#scrapeops api
SCRAPE_OPS_API_KEY  = '73904be3-d285-4c20-9940-5c82d64ece85'
def get_scrapeops_url(url):
    payload         = {'api_key': SCRAPE_OPS_API_KEY, 'url': url}
    proxy_url       = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


# logger settings> for color log you should pipenv install colorlog
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(name)s %(levelname)s:%(message)s',
                    datefmt='%Y-m-%d %H:%M:%S')

logger = logging.getLogger('nsquote.py') # filename



class ProxyquoteSpider(scrapy.Spider):
    name = 'proxyquote'
    allowed_domains = ['quotes.toscrape.com']
# send http requests
    def start_requests(self):
        urls = ['https://quotes.toscrape.com/']
        for url in urls:
            yield scrapy.Request(url=get_scraperapi_url(url), callback=self.parse)

# parse http response
    def parse(self, response):
        quotes = response.xpath ("//div[@class = 'quote']")
        for quote in quotes:
            text = quote.xpath(".//span[@class = 'text']/text()").get()
            author = quote.xpath(".//small[@class = 'author']/text()").get()
            tags = quote.xpath(".//div[@class = 'tags']/a/text()").getall()
            author_relative_link = response.urljoin (quote.xpath(".//a[contains(text(),'about')]/@href").get())

            yield  {
                    'text' : text,
                    'author': author,
                    'tags':tags,
                    'auth_link' : author_relative_link
                    }

            next_page = response.xpath("//li[@class = 'next']/a/@href").get()
            main_url = "https://quotes.toscrape.com/"
            abs_url = main_url + next_page
            if next_page:
                yield  scrapy.Request(url = abs_url , callback=self.parse)

            