# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class MyspiderPipeline:
#     def process_item(self, item, spider):
#         return item


import json

# class ItcastJsonPipeline(object):
#
#     def __init__(self):
#         self.file = open('teacher.json', 'wb')
#
#     def process_item(self, item, spider):
#         content = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.file.write(content.encode())
#         return item
#
#     def close_spider(self, spider):
#         self.file.close()

class TencentJsonPipeline(object):

    def __init__(self):
        #self.file = open('teacher.json', 'wb')
        self.file = open('tencent.json', 'wb')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content.encode())
        return item

    def close_spider(self, spider):
        self.file.close()