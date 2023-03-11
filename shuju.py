import  requests
from lxml import etree
import csv
#获取数据
def get_html(url,time=30):
    try:
        r = requests.get(url, timeout=time)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except Exception as error:
        print(error)

def parser(html): #解析函数
    doc=etree.HTML(html) #html转换为soup对象
    out_list=[] #解析函数输出数据的列表
    #二次查找法
    for row in  doc.xpath("//*[@class='testid']//li/h3"):
        row_data=[
            row.xpath("h3/a/text()")[0],
            row.xpath("h3/a/text()")[0],
            row.xpath("a[@class='testid']/text()")[0]
        ]
        out_list.append(row_data) #将解析的每行数据插入到输出列表中
    return out_list
def  save_csv(item,path): #数据存储，将list数据写入文件，防止乱码
    with open(path, "a+", newline='',encoding="utf-8") as f: #创建utf8编码文件
        csv_write = csv.writer(f) #创建写入对象
        csv_write.writerows(item) #一次性写入多行
if __name__=="__main__":
    for i in range(1,6):
        url="https://www.baidu.com/".format(i)
        html=get_html(url) #获取网页数据
        out_list=parser(html) #解析网页，输出列表数据
        save_csv(out_list,"d:\\book.csv") #数据存储
