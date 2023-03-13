import scrapy
# from items import RenyouItem
from renyou.items import RenyouItem
class TushuSpider(scrapy.Spider):
    name = 'tushu'
    allowed_domains = ['www.renyou.com']
    start_urls = ['https://www.ryjiaoyu.com/tag/books/7?X-Requested-With=XMLHttpRequest&_=1637817714872&page='+str(i) for i in range(0,6)]
    def parse(self, response):
        for row in response.xpath("//div[@class='block block-books block-books-grid']/ul//li/div[2]"):
            items = RenyouItem()
            items["book_name"] = row.xpath('./h4/a/text()').get()
            # print(items["book_name"])
            items["author"] = row.xpath('normalize-space(string(./div[@class="author"]))').get()
            # print(items["author"])
            items["price"] = row.xpath('./span/span/text()').get()
            # print(items["price"])
            items["link"] = row.xpath('./h4/a/@href').get()
            # print(items["link"])
            items["book_text"] = row.xpath('./p/text()').get()
            # print( items["book_text"])
            yield items


