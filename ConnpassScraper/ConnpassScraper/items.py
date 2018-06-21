# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ConnpassItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    event_id = scrapy.Field()
    title = scrapy.Field()
    catch = scrapy.Field()
    event_url = scrapy.Field()
    img_url = scrapy.Field()
    started_at = scrapy.Field()
    ended_at = scrapy.Field()
    address = scrapy.Field()