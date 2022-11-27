import scrapy

# in this section we find out product reviews from specific product from amazon


review_url = "https://www.amazon.com/product-reviews/{}"
asin_list= "B00DBL0NLQ"


class ReviewsSpider(scrapy.Spider):
    name = 'reviews'

    def start_requests (self):
        for asin in asin_list:
            url = review_url.format(asin)
            scrapy.Request(url)


    def parse(self, response):
        print ("i am parsed")
