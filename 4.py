from bs4 import BeautifulSoup
import requests
def getHTMLTest(url):
    try:
        r = requests.get(url)
        r.raise_for_status()  # 状态码不是200会引起HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'
url = 'http://search.dangdang.com/?key=python&act=input'
urls = ['http://search.dangdang.com/?key=python&act=input&page_index={}.html'.format(i) for i in range(2, 4)]
urls.insert(0, url)
with open('999.TXT','w',encoding='utf-8') as f:
    for url in urls:
        text = getHTMLTest(url)
        soup = BeautifulSoup(text)
        ul = soup.find_all("ul", {'class': "bigimg"})
        lis = ul[0].find_all("li")
        for li in lis:
            # 书名
            bookname1 = li.find("a")
            name = bookname1["title"]
            # 作者出版社
            author_p = li.find_all("p", {"class": "search_book_author"})
            span = author_p[0].find_all('span')

            a_author = span[0].text
            chuban = span[2].find('a')
            a_chuban = chuban.contents

            # 价格
            price_p = li.find_all("p", {"class": "price"})
            span_p = price_p[0].find("span")
            price = span_p.contents
            print(name, a_author, a_chuban, price)
            f.write('书名：{} \n 作者：{} \n出版社：{} \n价格：{}\n'.format(name,a_author,a_chuban,price)+'\n')