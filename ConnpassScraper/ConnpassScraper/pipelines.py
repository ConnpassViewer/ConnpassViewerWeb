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
    url = 'mysql+pymysql://root:password@mysql:3306/connpassviewer_development'
    Base = automap_base()
    
    def open_spider(self, spider):
        self.engine = sa.create_engine(self.url, pool_recycle=3600)
        self.Base.prepare(self.engine, reflect=True)
        self.Event = self.Base.classes.events
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def process_item(self, item, spider):
        if item.get('catch')== None:
            item['catch']=''
        if self.session.query(self.Event).filter(self.Event.event_id == item['event_id']).count() == 0:
            obj = self.Event(
                title=item['title'],
                catch=item['catch'],
                img_url=item['img_url'],
                event_url=item['event_url'],
                event_id=item['event_id'],
                started_at=datetime.strptime(item['started_at'],'%Y-%m-%dT%H:%M:%S+09:00'),
                ended_at=datetime.strptime(item['ended_at'],'%Y-%m-%dT%H:%M:%S+09:00'),
                address=item['address'],
                created_at = datetime.now(),
                updated_at = datetime.now()
            )
            self.session.add(obj)
        return item

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
