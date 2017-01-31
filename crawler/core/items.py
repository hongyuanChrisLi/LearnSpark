# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class LinkCnx(scrapy.Item):
    from_link = scrapy.Field()
    to_link = scrapy.Field()
    count = scrapy.Field()
