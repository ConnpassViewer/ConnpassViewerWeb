import sqlite3
from datetime import datetime

conn = None
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


conn = sqlite3.connect(DATABASE_NAME)
cur = conn.cursor()

sql = "select name from sqlite_master where type='table';";
cur.execute(sql)
print("hogehoge")
for row in cur:
    print(row)
sql = "select * from events;";
cur.execute(sql)
print("hogehoge")
for row in cur:
    print(row)
cur = conn.cursor()
cur.execute(CREATE_EVENT,(
    "item['title']",
    "item['catch']",
    "item['img_url']",
    "item['event_url']",
    89880,
    '2018-07-17 21:30:00+09:00',
    '2018-07-17 21:30:00+09:00',
    "item['address']",
))
conn.commit()
cur.execute(CREATE_EVENT,(
    "item['title']",
    "item['catch']",
    "item['img_url']",
    "item['event_url']",
    89880,
    '2018-07-17 21:30:00+09:00',
    '2018-07-17 21:30:00+09:00',
    "item['address']",
))
conn.commit()
conn.close()
#2018-06-21 04:49:45.277155
#
#datetime.strptime('2018-06-21 04:49:00', '%Y-%m-%d %H:%M:%S'),
#datetime.strptime('2018-06-22 04:49:00', '%Y-%m-%d %H:%M:%S'),
