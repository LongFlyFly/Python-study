# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WubatcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()#链接
    name = scrapy.Field()#名字
    price = scrapy.Field()#价格
    unitprice = scrapy.Field()#单价
    type = scrapy.Field()#户型
    area = scrapy.Field()#面积
    towards = scrapy.Field()#朝向
    floor = scrapy.Field()  # 楼层
    fitment = scrapy.Field()#装修情况
    time = scrapy.Field()#时间
    location = scrapy.Field()#位置
    pass
