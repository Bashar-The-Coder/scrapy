import scrapy
import re

class ProtidinSpider(scrapy.Spider):
    name = 'protidin'
    allowed_domains = ['www.bd-pratidin.com']
    start_urls = ['https://www.bd-pratidin.com/world-cup-2022/']

    def parse(self, response):
        world_cup_card = response.xpath("//div[@class='col-md-6 mt-4']")
        for news in world_cup_card:
            headline = news.xpath(".//div[@class = 'col-md-5 text']/text()").get()
            link     = news.xpath(".//div[@class='cat-2nd-lead']/a/@href").get()
            absurl = response.urljoin(link)

            
            yield scrapy.Request(url = absurl , callback = self.parse_detail)
            
    def remove_html_tags(self,text):
        #  """Remove html tags from a string"""
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)
    
    def parse_detail(self, response):
        detail = response.xpath("//article[@class ='mt-3']").get()
        # remove html
        detail = self.remove_html_tags(detail)
        detail = detail.replace("\n", "")
        rep = detail.strip()
        rep = re.sub("^\r" , "" , rep)
        rep = re.sub("^google.*;" , "" , rep)
        rep = rep.replace("\r", "").strip()
        
        
            
        yield{
            'detail' : rep
        }
