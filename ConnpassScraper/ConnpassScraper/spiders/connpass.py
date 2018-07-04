# -*- coding: utf-8 -*-
import scrapy
import requests
from ConnpassScraper.items import ConnpassItem
from ConnpassScraper.itemloaders import ConnpassLoader


class ConnpassSpider(scrapy.Spider):
    name = 'connpass'
    allowed_domains = ['connpass.com']
    events = requests.get("https://connpass.com/api/v1/event/").json()["events"]
    start_urls = [event["event_url"] for event in events]
    
    def parse(self, response):
        event = self.events[self.start_urls.index(response.url)]
        item = ConnpassLoader(ConnpassItem(), response=response)
        item.add_xpath('img_url', '//*[@id="main"]/div[1]/div[1]/a/@href')
        item.add_value('event_id', event['event_id'])
        item.add_value('title', event['title'])
        item.add_value('catch', event['catch'])
        item.add_value('event_url', event['event_url'])
        item.add_value('started_at', event['started_at'])
        item.add_value('ended_at', event['ended_at'])
        item.add_value('address', event['address'])
        yield item.load_item()
