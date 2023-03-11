import pymysql
import requests
from lxml import etree
def get_html(url, time=3000):
    try:
        headers ={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31"
        }
        r = requests.get(url, timeout=time,headers=headers)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except Exception as err:
        print(err)
result = []
def parse_html(html):
    html = etree.HTML(html)
    for row in html.xpath('//*[@id="content"]/div/div[1]/ul/li'):
        Naame = row.xpath("div[2]/h2/a/text()")[0].strip()#//*[@id="content"]/div/div[1]/ul[1]/div[2]/h2/a
        score = row.xpath("div[2]/p[2]/span[2]/text()")[0].strip()#//*[@id="content"]/div/div[1]/ul[1]/div[2]/p[2]/span[2]
        price = row.xpath("div[2]/p[1]/text()")[0].strip().split("/")#//*[@id="content"]/div/div[1]/ul[1]/div[2]/p[1]/text()
        price= price[0]
        content= price[1]
        a=price[2]
        b= price[-1]
        detail = [Naame,score,price,content,a,b]
        result.append(detail)
def join_all(sql_insert,vals,**dbinfo):
    try:
        connet = pymysql.connect(**dbinfo)
        cursor = connet.cursor()
        cursor.executemany(sql_insert,vals)
        connet.commit()
        print('添加成功！')
    except Exception as err:
        print(err)
        connet.rollback()
    cursor.close()
if __name__=="__main__":
    for page in range(1,16):
        url="https://book.douban.com/latest?subcat=%E5%85%A8%E9%83%A8&p={0}".format(str(page))
        parms ={
            "host":"127.0.0.1",
            "port":3306,
            "user":"root",
            "passwd":"123456",
            "db":"db",
            "charset":"utf8"
        }
        html=get_html(url)
        parse_html(html)
    sql_insert = "INSERT INTO db(Naame,score,price,content,a,b)\
                           Values(%s,%s,%s,%s,%s,%s)"
    join_all(sql_insert,result,**parms)
    print(result)