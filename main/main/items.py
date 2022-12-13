# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from w3lib.html import remove_tags, replace_escape_chars
from itemloaders.processors import MapCompose, TakeFirst , Join
# def rating(value):
#     x = value.split(' ')[-1]
#     return x

class MainItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BooksItem(scrapy.Item):
    # here input processor working with iterable object as well as list item and apply various function to
    # clean up data
    # and output processor take the item from a list
    # we can use regular or lambda function in mapcompose for cleansing data
    title = scrapy.Field(output_processor = TakeFirst())
    rating = scrapy.Field(input_processor = MapCompose (lambda x : x.split(' ')[-1]), output_processor = TakeFirst())
    # here we remove html element via remove tags method and we also apply lambda function to replace # to Tk
    price = scrapy.Field(input_processor = MapCompose (remove_tags , lambda x : x.replace('£' , 'Tk-')), output_processor =( TakeFirst()))
    in_stock = scrapy.Field(input_processor = MapCompose (remove_tags, lambda x: x.strip(), lambda x : 'True' if x=='In stock' else 'False'), output_processor =( TakeFirst()))
    link = scrapy.Field(output_processor = TakeFirst())
    # in article field we found many utf-8 character like tm, !@ and so on  which is need  to encoded to ascii
    article = scrapy.Field(input_processor = MapCompose(lambda x:x.encode('ascii', errors='ignore')), output_processor = TakeFirst())