# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.inspection import inspect


class ConnpassPipeline(object):
    DATABASE_NAME="../../Api/db/development.sqlite3"
    CREATE_EVENT ="""
    INSERT INTO events(
      title,
      catch,
      img_url,
      event_url,
      event_id,
      started_at,
      ended_at,
      address,
      created_at,
      updated_at
    )
    VALUES (
    ?,?,?,?,?,?,?,?,
    datetime('now', 'localtime'),
    datetime('now', 'localtime')
    )
    """
    conn = None

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.DATABASE_NAME)

    def process_item(self, item, spider):
        cur = self.conn.cursor()
        if item.get('catch')== None:
            item['catch']=""
        cur.execute(self.CREATE_EVENT,(
            item['title'],
            item['catch'],
            item['img_url'],
            item['event_url'],
            item['event_id'],
            item['started_at'],
            item['ended_at'],
            item['address'],
        ))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
