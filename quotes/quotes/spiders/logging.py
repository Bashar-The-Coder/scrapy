import scrapy
import logging

# to export a file we should add 3rd parameter filename
logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] %(name)s %(levelname)s:%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', filename='debug.log')
logger = logging.getLogger('logging.py') # filename

class LoggingSpider(scrapy.Spider):
    name = 'logging'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

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
       
        next_page = response.css('li.next a::attr(href)').get() 
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print (next_page)
            yield scrapy.Request(next_page, callback=self.parse)

# to see only log level info then we should run
#scrapy crawl logging -L INFO

# if we dont want any kind of warning debug or else info then we should run
# scrapy crawl logging --nolog