# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class RenyouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    book_text = scrapy.Field()
    pass
