# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql

from Scrapy1.myutlity import mysql


class Scrapy1Pipeline:
    def process_item(self, item, spider):
        return item


class Scrapy1BaoChun(object):
    def process_item(self, item, spider):
        w = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'passwd': '123456',
            'db': 'db',  # 库名
            'charset': 'utf8'
        }
        print("开始存入")
        sql = "insert into 58tc(selling_points, total_prices, unit_price, house_type, area, orientation, secorate_situatino, floor, building_age, plot, region) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        list = []
        for i, t in item.items():
            list.append(t)
        test = mysql()
        test.lianjie(**w)
        test.xiugai(sql=sql, valus=list)
        print(list)
        return item