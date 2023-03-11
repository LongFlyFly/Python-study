import pymysql
import requests
from bs4 import BeautifulSoup
result=[]

def get_html(url):
    try:
        headers ={
            'User - Agent':'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 94.0.4606.71Safari / 537.36'
        }
        r = requests.get(url,headers=headers)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except Exception as err:
        print(err)

def parser_html(html): #解析函数
    soup=BeautifulSoup(html,"lxml") #html转换为soup对象
    for row in soup.select("#pane-news "):
       row_list= row.find_all('a')
       for li in row_list:
            Link= li['href']
            Title = li.text
            detail = [Title,Link]
            result.append(detail)

def join_all(sql_insert,vals,**dbinfo):
    try:
        db = pymysql.connect(**dbinfo)
        cursor = db.cursor()
        cursor.executemany(sql_insert,vals)
        db.commit()
        print('添加成功！')
    except Exception as err:
        print(err)
        db.rollback()
        db.close()


url="https://news.baidu.com/"
html = get_html(url)
parser_html(html)
parms ={
            "host":"127.0.0.1",
            "port":3306,
            "user":"root",
            "passwd":"123456",
            "db":"company",
            "charset":"utf8"
        }
sql_insert = "INSERT INTO date(Title,Link) Values(%s,%s)"
join_all(sql_insert,result,**parms)
# print(result)