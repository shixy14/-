# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from datetime import datetime
import scrapy


class YinchuanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    column = scrapy.Field()
    sub_column = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    date = scrapy.Field()
    pass
