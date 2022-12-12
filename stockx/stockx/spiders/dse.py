import scrapy


class DseSpider(scrapy.Spider):
    name = 'dse'
    allowed_domains = ['www.dsebd.org']
    start_urls = ['https://www.dsebd.org/top_20_share.php']

    def parse(self, response):
        rows = response.xpath("(//table[@class='table table-bordered background-white shares-table'])[1]/tbody/tr")

        for row in rows:
            name = row.xpath(".//td[2]/a/text()").get()
            LTP = row.xpath(".//td[3]/text()").get().strip()
            high = row.xpath(".//td[4]/text()").get().strip()
            low = row.xpath(".//td[5]/text()").get().strip()
            ycp = row.xpath(".//td[6]/text()").get().strip()
            closep = row.xpath(".//td[7]/text()").get().strip()
            trade = row.xpath(".//td[8]/text()").get().strip()
            value = row.xpath(".//td[9]/text()").get().strip()
            volume = row.xpath(".//td[10]/text()").get().strip()
            link = response.urljoin(row.xpath(".//td[2]/a/@href").get())

            yield {
                'name' : name,
                'ltp'  : LTP,
                'high': high,
                'low' : low,
                'ycp' : ycp,
                'closep' : closep,
                'trade' : trade,
                'value' : value,
                'volume' : volume,
                'link' : link
            }
