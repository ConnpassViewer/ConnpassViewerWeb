FROM python:3.6.5
ENV LANG C.UTF-8

ENV APP ./ConnpassScraper
COPY ./ ./ConnpassScraper
WORKDIR $APP
RUN pip install scrapy
RUN pip install requests
RUN pip install SQLAlchemy
RUN pip install pymysql
