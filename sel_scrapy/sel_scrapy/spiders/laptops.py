## spider.py
import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        url = 'https://quotes.toscrape.com/js/'
        yield SeleniumRequest(url=url, callback=self.parse, 
                             
                                            wait_time=10,
                                            wait_until=EC.element_to_be_clickable((By.CLASS_NAME, 'quote')))

    def parse(self, response):
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author = quote.css('small.author::text').get()
            # tags = quote.css('div.tags a.tag::text').getall()
            yield {
                'text' : text,
                'author' : author,
                # 'tags' : tags
            }

        next_page = response.xpath ("//li[@class='next']/a/@href").get()
        next_page_url = response.urljoin(next_page)

        if next_page:
            yield SeleniumRequest(url = next_page_url , callback=self.parse, 
                                          
                                            wait_time=10,
                                            wait_until=EC.element_to_be_clickable((By.CLASS_NAME, 'quote')) )