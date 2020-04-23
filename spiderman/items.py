# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidermanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    index = scrapy.Field()
    title = scrapy.Field()
    star = scrapy.Field()
    release_time = scrapy.Field()
    score = scrapy.Field()


class XiaoFeiQuanItem(scrapy.Item):
    url = scrapy.Field()
    news_title = scrapy.Field()
    news_content = scrapy.Field()
    # province = scrapy.Field()
    # city = scrapy.Field()
    publish_date = scrapy.Field()
    # issue_circle = scrapy.Field()
    # issue_date = scrapy.Field()
    # total_issue = scrapy.Field()
    # issue_amount = scrapy.Field()
    # cover_sector = scrapy.Field()
