import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/s?i=computers-intl-ship&rh=n%3A16225007011&fs=true&qid=1669391918&ref=sr_pg_1/']

    def parse(self, response):
        items = response.xpath("//div[contains (@class, 's-card')]")
        for item in items:
            item_name = item.xpath(".//span[@class='a-size-base-plus a-color-base a-text-normal']/text()").get()
            price = item.xpath(".//span[contains (@class, 'a-price-whole')]/text()").get()
            yield {
                'item' : item_name,
                'price' : price
            }