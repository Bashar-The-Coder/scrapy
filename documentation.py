# Today we crawl books to scrape page

# 1. to see all available genspider commands
# scrapy genspider -l # l for list

# 2. to create crawlspider
# scrapy genspider -t crawl books_crawl x # here -t for template and crawl for crawl spider if we dont declare crawl scrapy generate simple spider for us
# code .

# rules attribute are tuple
    #linkextractors as le
    # it will extract all the link and it only allow the links that contain this particular item and ignore rest all the item
    
# 3. to crawl any website we inspect the link 

# to run crawler inside the directory
# scrapy crawl books_crawl

##### change user agent . it is good idea for changing user agent if site is not allow to me scraping #########
USER_AGENT = 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'

###### Add A User-Agent To Every Request  #########
# Another option is to set a user-agent on every request your spider makes by defining a user-agent in the headers of your request:
def start_requests(self):
    for url in self.start_urls:
        return scrapy.Request(url=url, callback=self.parse,
                       headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"})

# for ommit unicode in settings
FEED_EXPORT_ENCODING = 'utf-8'

#for xpath contains
