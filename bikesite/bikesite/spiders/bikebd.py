import scrapy
from scrapy.utils.response import open_in_browser
from urllib.parse import urlencode

#scraper api
SCRAPER_API_KEY     = '1fb55a799e4bf83bea437f4835c3aa8c'
def get_scraperapi_url(url):
    payload         = {'api_key': SCRAPER_API_KEY, 'url': url}
    proxy_url       = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url

class BikebdSpider(scrapy.Spider):
    name = 'bikebd'
    allowed_domains = ['www.bikebd.com']
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'accept-encoding': 'deflate',
            'accept-language': 'en-US,en;q=0.9,da;q=0.8',
            'cache-control':'no-cache',
            'pragma': 'no-cache',
            'cookie': '_ga=GA1.1.1513438114.1669697183; _ga_HEG073JLWK=GS1.1.1670747303.4.1.1670748957.0.0.0; XSRF-TOKEN=eyJpdiI6InNiamIxTS80U25BazFyb1hpZk9OMHc9PSIsInZhbHVlIjoiZmxUSENWNHJJU01VME5ZSzQ4OWdSY3JTM2dDZHFLZnRHMGZlWjVYd0FWcDA0dUlBanBVbVZkR3FRUW5RV2w2K0FreXlrNlRISm9RRUVuL25GcmlTY0JqbzdHRmdya1lUbjN4azM2SWZrQkhTbE9weTdLMlJJSWt0LzQyQWdtZkQiLCJtYWMiOiI2OGIxYjA1MDQ4Yzc3MDlkZWUwMzc0N2UxMDMyOTE3M2NmNjZjOWVjNDY5ZmI3ZWNmMmFmYTNjMTY2ZGI1ZWNhIiwidGFnIjoiIn0%3D; bikebd_session=eyJpdiI6InVMSFQ2OEROZzlQR2kzSitTLzRMT2c9PSIsInZhbHVlIjoiVi9BeUdqa1FTVzJJT2pldkplbnpCMit1MUtZMjhsT0o3RTFiZ3pPYkVJS3JMemdGblJpaHc4aW1SM0FwMFQ3Q2JCeWlGMmFFZ1FKVnJQYklLaHgzd2ZldlFWV3dWZWViV2JMSFFma3lDS0FVZ0xkMFFURFVPTW9UTUM0QjRsRWwiLCJtYWMiOiIxNGE3OGJmNWM4OGYyMDhiMzFmZGQwZmVlYjRhNTdjOGQ2NzI1OTIwYTFhYmEzOGZkZTRhYzU5YjAzNGM2MDYyIiwidGFnIjoiIn0%3D',
            'referer': 'https://www.bikebd.com/',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': 1,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            }

    def start_requests(self):
        urls = ["https://www.bikebd.com/bn/blog/category/motrsaikel-malikana-riviu"]
        for url in urls:
            yield scrapy.Request(url = url ,  callback=self.parse, headers=self.headers)

    def parse(self, response):
        container = response.xpath("//p/text()").get()

            # title = item.xpath(".//p/strong/text()").get()
            # address = item.xpath(".//p[@class = 'm-sh-dtl']/text()").get()
            # link = item.xpath(".//div[@class = 'more-sh-main']/a/@href").get()
        yield {
            'title' : container,


        }


    def parse(self, response):
        open_in_browser(response)
