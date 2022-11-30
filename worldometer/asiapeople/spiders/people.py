import scrapy
import logging

class PeopleSpider(scrapy.Spider):
    name = 'people'
    allowed_domains = ['www.worldometers.info'] # this is so importan if this url wrong then program should broken
    start_urls = ['https://www.worldometers.info/world-population/population-by-country']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            self.country_name = name
            link = country.xpath(".//@href").get()

            # mainurl = "https://www.worldometers.info"
            # absolute_url = mainurl + link
            # other way to join url and send request is
            # absolute_url = response.urljoin(link)
# lets send request to the url in anchor tag
            # print (absolute_url)
            yield response.follow (url = link, callback = self.parse_country, meta = {'country_name': name} ) # when we want to send data from one parse to another we should pass dict by meta name
# another way to follow url without take pain of relative and concat absolute url is
# yield response.follow(url = link)
# by this we dont need to concat relative url with absoulut
# scrapy automaticaly join this this is very shortcut method

# in here scrapy iterate through all the url and send request to each url and then call this parse method
# now we can gather information from each link response
    def parse_country(self, response):
# to catch the whatever sent from the meta argument we should receive as response object
        name = response.request.meta['country_name']
        print ("hello parse country",response.url)
        rows = response.xpath("(//table[@class = 'table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
#to see whats happening in this time we call loging method and crawl again
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            yield {
                'country_name' : name,
                'year' : year,
                'population' : population
            }
