import scrapy


class W3resSpider(scrapy.Spider):
    name = 'w3res'
    allowed_domains = ['www.w3resource.com']
    start_urls = ['https://www.w3resource.com/sql-exercises/sql-subqueries-exercises.php']

    def parse(self, response):
        links = response.xpath('//article[@itemtype="https://schema.org/TechArticle"]//a[contains(@href,"sql-subqueries-exercise")]/@href')
        q = response.xpath ("//p[@class]/text()[2]").get()
        for link in links:
            

            yield response.follow (url = link, callback = self.parse_all , meta = {'ques' : q})


    def parse_all(self, response):
        ques = response.xpath ("//article[@itemtype ='https://schema.org/TechArticle']/p[1]/text()").get()
        h2 = response.xpath(".//textarea [@id='query']/text()").get()

        yield {
            'question' : ques,
            'query' : h2
        }