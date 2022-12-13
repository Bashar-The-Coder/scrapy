import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class DarazSpider(scrapy.Spider):
    name = 'daraz'
    allowed_domains = ['www.daraz.com']
    # start_urls = ['https://www.daraz.com.bd/catalog/?spm=a2a0e.home.search.1.573712f7eJUJKN&q=laptops&_keyori=ss&from=search_history&sugg=laptops_0_1']
    
    def start_requests(self):
        for i in range (1,5):
         url = f'https://www.daraz.com.bd/catalog/?_keyori=ss&from=search_history&page={i}&q=laptops&spm=a2a0e.home.search.1.573712f7eJUJKN&sugg=laptops_0_1'
         yield SeleniumRequest(url=url, callback=self.parse, 
                             
                                            wait_time=40,
                                            wait_until=EC.element_to_be_clickable((By.CLASS_NAME, 'inner--SODwy')))


    def parse(self, response):
        container = response.xpath("//div[@class='box--pRqdD']")
        for item in container:
            title = item.xpath(".//div[@class='title--wFj93']/a/text()").get()
            yield{
                'title' : title
            }