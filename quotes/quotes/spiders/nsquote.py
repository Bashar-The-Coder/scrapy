import scrapy
import logging


logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] %(name)s %(levelname)s:%(message)s',
                        datefmt='%Y-m-%d %H:%M:%S')
logger = logging.getLogger('logging.py') # filename

class NsquoteSpider(scrapy.Spider):
    name = 'nsquote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath ("//div[@class = 'quote']")
        for quote in quotes:
            text = quote.xpath(".//span[@class = 'text']/text()").get()
            author = quote.xpath(".//small[@class = 'author']/text()").get()
            tags = quote.xpath(".//div[@class = 'tags']/a/text()").getall()
            author_relative_link = response.urljoin (quote.xpath(".//a[contains(text(),'about')]/@href").get())

            yield response.follow(author_relative_link , callback =  self.parse_auth, meta = {
                                                                                                'text' : text,
                                                                                                'author': author,
                                                                                                'tags':tags,
                                                                                                'auth_link' : author_relative_link
                                                                                                } )
       
        next_page = response.css('li.next a::attr(href)').get() 
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print (next_page)
            yield scrapy.Request(next_page, callback=self.parse)


    def parse_auth(self, response):


        yield { 'auth_name' : response.xpath("//h3[@class = 'author-title'] /text()").get(),
                'birth_day' : response.xpath("//span[@class = 'author-born-date'] /text()").get(),
                'born_in' : response.xpath("//span[@class = 'author-born-location'] /text()").get(),
                'auth_desc' : response.xpath("//div[@class = 'author-description'] /text()").get(),
                'quote' : response.request.meta['text'],
                'tags' : response.request.meta['tags'],
                # 'auth_link' : response.request.meta['author_relative_link']
                }

