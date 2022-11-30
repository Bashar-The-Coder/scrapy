import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath ("//div[@class='quote']")
        for quote in quotes:
            text = quote.xpath("./span[@class='text']/text()").get()
            author = quote.xpath ("./small[@class='author']/text()").get()
            # #for css
            # text = quote.css(".text ::text").get()
            # author = quote.css(".author ::text").get()

            yield {
                'text': text,
                'author' : author
            }

        next_page =  response.xpath("//li[@class='next']/a/@href").get()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)