import csv
import pymysql
from lxml import etree
import requests
from bs4 import BeautifulSoup

# 得到html
class get_html():
    def __init__(self):
        self.url = ""
        self.heasers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
        }

    def get_Html(self, url):
        self.url = url
        res = requests.get(url=self.url, headers=self.heasers,)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        return res.text

# xpath解析
class xpath():
    def __init__(self):
        self.html = ""
        self.list = []

    def get_xpath(self, html, xpath):
        self.html = etree.HTML(html)
        self.list = self.html.xpath(xpath)
        return self.list

# Csv保存
class set_csv():

    def __init__(self):
        self.path = ""
        self.list = []
        with open("C:/Users/Anaerobic/Desktop/ads/sfa.csv", "w+", newline='') as f:
            wrte = csv.writer(f)
            wrte.writerow(self.list)

    def set_Csv(self, list):
        self.list = list
        with open("C:/Users/Anaerobic/Desktop/ads/sfa.csv", "a+", newline='') as f:
            wrte = csv.writer(f)
            wrte.writerow(self.list)

    def set_title(self, list):
        self.list = list
        with open("C:/Users/Anaerobic/Desktop/ads/sfa.csv", "w+", newline='') as f:
            wrte = csv.writer(f)
            wrte.writerow(self.list)
# 存入mysql数据库
class mysql():
    def __init__(self):
        self.mysql = ""
    # 连接数据库
    # 创建游标对象cursor
    def lianjie(self,**mysql):
        self.conn = pymysql.Connect(**mysql)
        self.conn.cursor()
        self.cursor = self.conn.cursor()

    def chaxun(self):
        self.cursor = self.conn.cursor()
        sql_select = "select * from text"#表名
        self.cursor.execute(sql_select)
        self.results = self.cursor.fetchall()
        self.cursor.close()
        return self.results

    def xiugai(self,sql,valus):
        try:
            self.cursor.execute(sql, valus)
            self.conn.commit()
            print('添加成功！')
        except Exception as e:
            print(e)
            self.conn.rollback()
        self.cursor.close()

class BeautifulSoup1():
    def __init__(self):
        self.soup = ""
        self.beautifulSoup=""
    def get_BeautifulSoup(self,html,beautifulSoup,features='lxml'):
        self.soup = BeautifulSoup(html,features)
        return self.soup.find_all(beautifulSoup)
def name():
    print("name")