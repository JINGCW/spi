# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy import Spider
from scrapy.item import Item
from json import dump


class SpidermanPipeline(object):
    def __init__(self):
        self.score = 8.5

    def process_item(self, item: Item, spider: Spider):
        # return item
        # print(f"***********{item}\n")
        if item["score"]:
            if float(item["score"]) <= self.score:
                item["score"] = "不好看!"
            return item

        return DropItem("missing score!")


class JsonPipeline(object):
    indent = 2
    separators = (', ', ': ')

    def __init__(self, path="maoyan.json"):
        self.path = path

    def process_item(self, item: Item, spider: Spider):
        print(f"???????????????????{type(item)}---{type(dict(item))}")
        with open(self.path, mode="a", encoding="utf-8") as fd:
            print("(((((((((((((((((((")
            dump(item, fd, indent=self.indent, separators=self.separators, ensure_ascii=False)
        return item
