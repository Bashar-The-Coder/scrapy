import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css ("div.quote")
        for quote in quotes:
            # text = quote.css("span.text ::text").get()
            # author = quote.css("small.author ::text").get()
            # link = quote.css("span  a").attrib['href']
            # self.log(f'Saved file quotes.html')          
            author_partial_link = quote.xpath('.//span/a/@href').get()    
            author_link = response.urljoin(author_partial_link)
            
            
            # yield {
            #     'text' : text,
            #     'author' : author,
            #     'link' : link
            # }
            print (response.urljoin(author_link))
            author_link = response.urljoin(author_link)
            yield scrapy.Request(author_link, callback=self.parse_author)
            
            
    def parse_author(self, response):
        self.log(f'Saved file sdfasdfsadf.html')
        description = response.xpath('//div[@class="author-description"]/text()').extract_first().strip()

        yield {

            'description': description,
        }