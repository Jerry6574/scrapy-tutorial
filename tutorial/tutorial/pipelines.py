# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Scraped data -> Item containers -> JSON/CSV files
# Scraped data -> Item containers -> Pipeline -> SQL/Mongo database


class TutorialPipeline(object):
    def process_item(self, item, spider):
        print("Pipeline: " + item['title'][0])
        return item
