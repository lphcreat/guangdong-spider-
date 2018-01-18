# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuangdongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    credit_num=scrapy.Field()
    re_num=scrapy.Field()
    or_name= scrapy.Field()
    or_type=scrapy.Field()
    or_date=scrapy.Field() 
    manager=scrapy.Field()
    person=scrapy.Field()
    address=scrapy.Field()
    city=scrapy.Field()
    pass
