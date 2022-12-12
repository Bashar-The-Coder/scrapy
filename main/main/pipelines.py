# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface

#insert to postgresql db
# 1. pip install pyscopg2 for postgres connection
from itemadapter import ItemAdapter
import psycopg2

# 2. Setup Our Pipeline
class PostgresPipeline:
    def __init__(self):
        """Inside the __init__ method, we will configure the pipeline to do the following everytime
            the pipeline gets activated by a spider:
           1. Try to connect to our database books, but if it doesn't exist create the database.
           2. Create a cursor which we will use to execute SQL commands in the database.
           3. Create a new table quotes with the columns content, tags and author, if one doesn't already exist in the database.        """
        hostname = 'localhost'
        username = 'postgres'
        password = 'postgres' # your password
        database = 'scrape'
         ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()
        ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id serial PRIMARY KEY, 
            title text,
            rating text,
            price text,
            in_stock VARCHAR(255),
            link VARCHAR(255),
            article text

        )
        """)
    #process item is a method by it we can call allitems from items.py class
    #     # and spider
    # 4. Save Scraped Items Into Database
    # Next, we're going to use the process_item event inside in our Scrapy 
    # pipeline to store the data we scrape into our Postgres database.
    # The process_item will be activated everytime, a item is scraped by our spider so we need to configure 
    # the process_item method to insert the items data in the database.
    # We will also the close_spider method, which will be called when the Spider is shutting down, 
    # to close our connections to the cursor and database to avoid leaving the connection open.
    def process_item(self, item, spider):
        self.cur.execute(""" insert into books (title, rating, price, in_stock, link, article) values (%s,%s,%s,%s,%s,%s)""", (
            item["title"],
            str(item["rating"]),
            item["price"],
            item["in_stock"],
            str(item["link"]),
            # as article is byte type. we need to decode it to utf
            item["article"].decode('utf-8'),
        ))

        ## Execute insert of data into database
        self.connection.commit()
        return item

    def close_spider(self, spider):
    ## Close cursor & connection to database 
        self.cur.close()
        self.connection.close()

# 5. Activate Our Item Pipeline
# Finally, to activate our Item Pipeline we need to include it in our settings.py file:
# ITEM_PIPELINES = {
#    'postgres_demo.pipelines.PostgresDemoPipeline': 300,
# }

# we can also create an excel file to export the data
import openpyxl
import pandas as pd
import numpy as np
import csv
from openpyxl import Workbook

# wb = load_workbook(r'C:\Users\DEVANSH SHARMA\Desktop\demo.xlsx')  

class ExportToExcel:
    def __init__(self):
        pass

    def process_item(self, item, spider):
        spider.logger.info("process item")

    
    def open_spider(self, spider):
        spider.logger.info("open spider")


    def close_spider(self, spider):
        spider.logger.info("close spider")



