# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 卖点
    selling_points = scrapy.Field()
    # 总价
    total_prices = scrapy.Field()
    # 单价
    unit_price = scrapy.Field()
    # 户型
    house_type = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 朝向
    orientation = scrapy.Field()
    # 装修情况
    secorate_situatino=scrapy.Field()
    # 楼层
    floor = scrapy.Field()
    # 建筑年代
    building_age = scrapy.Field()
    # 所属小区
    plot = scrapy.Field()
    # 所在区域
    region = scrapy.Field()
