# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SbdspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tid = scrapy.Field()    # 网盘类型ID
    cid = scrapy.Field()    # 资源分类ID
    uid = scrapy.Field()    # 资源用户ID
    name = scrapy.Field()
    avatar = scrapy.Field()
    title = scrapy.Field()  # 资源标题
    size = scrapy.Field()   # 资源大小
    url = scrapy.Field()    # 资源URL
    pwd = scrapy.Field()    # 资源密码
    description = scrapy.Field() # 资源描述
    available = scrapy.Field()   # 是否可用
    sharetime = scrapy.Field()   # 分享时间