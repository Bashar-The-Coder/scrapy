# scrapy genspider -t crawl best_movies imdb.com

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import logging

# to export a file we should add 3rd parameter filename
logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] %(name)s %(levelname)s:%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', filename='debug.log')
logger = logging.getLogger('logging.py') # filename


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['www.imdb.com']
    start_urls = []
    def start_requests(self):
        yield scrapy.Request(url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250' , params  ={
                                                                                    'api_key': '73904be3-d285-4c20-9940-5c82d64ece85',
                                                                                    'url': 'https://quotes.toscrape.com/', 
                                                                                },)

    rules = (
        # here allow= r'Items means which link that contains Items word then please extract it follow it and and parse
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # here deny = r'Items means which link that contains Items word then please escape it
        # Rule(LinkExtractor(deny=r'Items/'), callback='parse_item', follow=True),
        # another way to follow link is restrict_xpaths or restrict_css which mean please follow the given xpath link
        # this mean please follow all the a link where a's class is active. we dont need to add //a[@class = 'active']/@href
        # coz linkExtractor object automatically find the href attribute from a link
        # tips: if we need two or many xpath expression then we should use tuple bracke, otherwise not
        # after given xpath we check the link works or not to parse section just using logger.info(response.url)
        # scrapy crawl best_movies
        Rule(LinkExtractor(restrict_xpaths="//td[@class = 'titleColumn']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        logger.info(response.url)

