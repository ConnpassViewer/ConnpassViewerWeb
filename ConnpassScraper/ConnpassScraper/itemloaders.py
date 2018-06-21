# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity, TakeFirst


class ConnpassLoader(ItemLoader):
    default_input_processor = TakeFirst()
    default_output_processor = TakeFirst()
    