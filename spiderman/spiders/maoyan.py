# -*- coding: utf-8 -*-
import scrapy
from ..items import SpidermanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/board/7']

    def parse(self, response: scrapy.http.Response):
        dl = response.css(".board-wrapper dd")
        for dd in dl:
            item = SpidermanItem()
            item["index"] = dd.css(".board-index::text").extract_first()
            item["title"] = dd.css(".name a::text").extract_first()
            item["star"] = dd.css(".star::text").extract_first().strip()
            item["release_time"] = dd.css(".releasetime::text").extract_first()
            # item["score"] = dd.css(".integer::text").extract_first(default=-1) + \
            #                 dd.css(".fraction::text").extract_first(default=-1)
            item["score"] = dd.css(".integer::text").extract_first() + \
                            dd.css(".fraction::text").extract_first()
            yield item
