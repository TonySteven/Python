# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class MyspiderItem(scrapy.Item):
#     # define the fields for your item here like:
#     name = scrapy.Field()

class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()


class TencentItem(scrapy.Item):
    name = scrapy.Field()
    # detailLink = scrapy.Field()
    positionInfo = scrapy.Field()
    # peopleNumber = scrapy.Field()
    workLocation = scrapy.Field()
    publishTime = scrapy.Field()