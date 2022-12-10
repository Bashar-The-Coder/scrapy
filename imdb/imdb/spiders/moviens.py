import scrapy
from scrapy.utils.response import open_in_browser
import logging
from urllib.parse import urlencode

#scraper api
SCRAPER_API_KEY     = '1fb55a799e4bf83bea437f4835c3aa8c'

def get_scraperapi_url(url):
    payload         = {'api_key': SCRAPER_API_KEY, 'url': url}
    proxy_url       = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url

#scrapeops api
SCRAPE_OPS_API_KEY  = '73904be3-d285-4c20-9940-5c82d64ece85'
def get_scrapeops_url(url):
    payload         = {'api_key': SCRAPE_OPS_API_KEY, 'url': url}
    proxy_url       = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


# logger settings> for color log you should pipenv install colorlog
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(name)s %(levelname)s:%(message)s',
                    datefmt='%Y-m-%d %H:%M:%S')

logger = logging.getLogger('nsquote.py') # filename





class MoviensSpider(scrapy.Spider):
    name = 'moviens'
    allowed_domains = ['www.imdb.com']

    headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,da;q=0.8",
            "cache-control": "no-cache",
            "cookie": "ubid-main=135-1544469-9109103; uu=eyJpZCI6InV1ODE3MDQ0NWQ3NjcwNDIxNDkxMjIiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfX0=; session-id-time=2082787201l; session-id=131-1268280-9950462; adblk=adblk_no; session-token=pJkwsyqKWAhM7f+7yQzDwyrxYKSRhWluYp6bc3dtOVpt2bft5fngImlmWFPvIUI8jk2TQslSZKvncwC4gtvBlJ1qeCTKrkiozlU5Kk0y0mCFdTAxY9A9Zo0zzA4jARPpwBpLcy1560GIL9SdmBRpIZUYT9A+G3GPbwMG+1wfKtGqs7kcRCWCXCKQkQj1DJfcK77pIn855wNJ3Rsd4EO5NVx/LiOct7KLxesSdDEowZk=; csm-hit=tb:s-5DJG6Y8V7QQM7GB5D8VK|1670484910485&t:1670484910486&adb:adblk_no",
            "pragma": "no-cache",
            "referer":"https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm",
            "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",

            }

    def start_requests(self):
        urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]
        for urlx in urls:
            yield scrapy.Request(get_scraperapi_url(url = urlx), headers=self.headers, callback=self.parse)

    def parse(self, response):
        # open_in_browser(response)
        items = response.xpath("//td[@class ='titleColumn']")
        for item in items:
            title = item.xpath(".//a/text()").get()
            link = "https://www.imdb.com"+(item.xpath(".//a/@href").get())

            yield scrapy.Request(url=link, callback=self.parse_item, meta={"title" : title} ,headers=self.headers)

    def parse_item(self, response):
        movie_name = response.request.meta['title']
        desc = response.xpath("//span[@class='sc-16ede01-1 kgphFu']/text()").get()
        director = response.xpath("(//div[@data-testid='title-pc-wide-screen']/ul/li/div//a/text())[1]").get()
        meta_score = response.xpath("//span[@class='score-meta']/text()").get()
        score = response.xpath("//span[@class='score']/text()").get()
        story_line = response.xpath("//div[@class='ipc-html-content-inner-div']/text()").get()
        tags = response.xpath("//div[@class='ipc-chip-list__scroller']/a[@class='ipc-chip ipc-chip--on-base']/span/text()").getall()
        user_review = response.xpath("//div[@data-testid='review-overflow']/div/div/text()").getall()
        actors = response.xpath("(//ul[@class='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt'])[3]/li/a/text()").getall()
        budget = response.xpath("(//label[@class='ipc-metadata-list-item__list-content-item'])[3]/text()").get()

        yield {
            'movie_name' : movie_name,
            'description' : desc,
            'director' : director,
            'meta_score' : meta_score,
            'score': score,
            'story_line': story_line,
            'tags' : tags,
            'user_review' : user_review,
            'actors' : actors,
            'budget' : budget,
            }
