import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksCrawlSpider(CrawlSpider):
    name = 'books_crawl'
    """# dont add https and remove backslash and it is so important to allowed_domains rule 
            without allowed domain the spider goes to any wheree
         """
    allowed_domains = ['books.toscrape.com']
    start_urls = [
        'https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html']
# rules attribute are tuple
    # linkextractors as le
    # it will extract all the link and it only allow the links that contain this particular item and ignore rest all the item

##############################* THIS PART IS FOR CREATING LINK EXTRACTOR ############################ 
    le_book_details = LinkExtractor(restrict_css="h3 > a")
    # if we have more than one parameter then we should create a tuple inside restict_css assignment (restrict_css = "h3 > a")
    # এখানে প্রথমে xpath  হিসাবে উপ্রক্ত আইটেম পাসস করার পর spider প্রতিতা লিঙ্ক এ যাবে তারপর সে প্রতিতা detail পেজ এ গিয়েও follow করবে যদি আমরা follow = true রাখি
    # তারমানে সে প্রতিতা detail page এ গিয়েও h3 > a খুজবে। কিন্তু আমরা টা চাই না।
    le_next             = LinkExtractor(restrict_css='.next > a')  # next_button
    le_cats             = LinkExtractor(restrict_css='.side_categories > ul > li > ul > li a')  # Categories

##############################* THIS PART IS FOR CREATING SINGLE RULE ############################ 
    rule_book_details   = Rule( le_book_details, callback='parse_item', follow=False)
    rule_next           = Rule(le_next, follow=True)
    rule_cats           = Rule(le_cats, follow=True)

##############################* THIS PART IS FOR CREATING MULTIPLE RULES ############################ 
    rules               = ( rule_book_details,
                            rule_next,
                            rule_cats
                          )

    # এখন আমরা জেসকল details page theke আইটেম পার্স করব তাহলো হেডলাইন, category url,

    def parse_item(self, response):
        yield {
            'Title': response.css("h1 ::text").get(),
            'Category': response.xpath("//ul[@class = 'breadcrumb']/li[last()-1]/a[@href]").get(),
            # debugging purpose we should add link
            'links': response.url

        }
