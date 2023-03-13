# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WubatcPipeline:
    def process_item(self, item, spider):
        return item
class MySQLPipeline:
    def open_spider(self, spider):
        # 读取settings.py中的配置项
        host = spider.settings.get("MYSQL_DB_HOST", "缺省服务器ip")
        port = spider.settings.get("MYSQL_DB_PORT", "缺省端口号")
        dbname = spider.settings.get("MYSQL_DB_NAME", "缺省数据库")
        user = spider.settings.get("MYSQL_DB_USER", "缺省用户名")
        pwd = spider.settings.get("MYSQL_DB_PASSWORD", "缺省密码")
        # 创建数据库链接
        self.db_conn = pymysql.connect(host=host, port=port, db=dbname, user=user, password=pwd)
        # 打开游标
        self.db_cur = self.db_conn.cursor()

    def process_item(self, item, spider):
        values = (
            item["url"],
            item["name"],
            item["price"],
            item["unitprice"],
            item["type"],
            item["area"],
            item["towards"],
            item["floor"],
            item["fitment"],
            item["time"],
            item["location"],
        )
        # sql语句，数据部分使用占位符%s代替
        sql = "insert into wubatc(url,name,price,unitprice,type,area,towards,floor,fitment,time,location) " \
              "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.db_cur.execute(sql, values)  # 执行SQL语句
        self.db_conn.commit()  # 提交事务
        return item
    def close_spider(self, spider):
        self.db_cur.close()  # 关闭游标
        self.db_conn.close()  # 关闭数据库连接