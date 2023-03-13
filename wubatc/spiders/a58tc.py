import scrapy
from ..items import WubatcItem


class A58tcSpider(scrapy.Spider):
    name = 'a58tc'
    allowed_domains = ['58.com']
    start_urls = ['https://www.baidu.com']

    def parse(self, response):
        print(response)
        global url, item
        for row in response.xpath("/html/body/div[1]/div/div/section/section[3]/section[1]/section[2]/div"):
            item = WubatcItem()
            url = row.xpath("a/@href").get()
            item['url'] = url
            item['name'] = row.xpath("a/div[2]/div[1]/div[1]/h3/text()").get()
            item['price'] = row.xpath("a/div[2]/div[2]/p[1]/span[1]/text()").get()
            item['unitprice'] = row.xpath("a/div[2]/div[2]/p[2]/text()").get()
            yield scrapy.Request(url,meta={"item":item},callback=self.parse_detail)
        next_url = response.xpath("//*[@class='next next-active']/@href").get()  # 获取下一页的href属性
        if next_url:  # 判断是否为最后一页
            url = response.urljoin(next_url)  # 拼接url地址的绝对路径
            yield scrapy.Request(url)  # 发送下一页请求
    def parse_detail(self, response):
        item = response.meta["item"]
        item["type"] = response.xpath("//*[@class='maininfo-model']/div[1]/div[1]/i[1]/text()").get()+\
                       response.xpath("//*[@class='maininfo-model']/div[1]/div[1]/span[1]/text()").get()+\
                       response.xpath("//*[@class='maininfo-model']/div[1]/div[1]/i[2]/text()").get()+\
                       response.xpath("//*[@class='maininfo-model']/div[1]/div[1]/span[2]/text()").get()+\
                       response.xpath("//*[@class='maininfo-model']/div[1]/div[1]/i[3]/text()").get()+\
                       response.xpath("//*[@class='maininfo-model']/div[1]/div[1]/span[3]/text()").get()
        item["area"] = response.xpath("//*[@class='maininfo-model']/div[2]/div[1]/i/text()").get()
        item["towards"] = response.xpath("//*[@class='maininfo-model']/div[3]/div[1]/i/text()").get()
        item["floor"] = response.xpath("//*[@class='maininfo-model']/div[1]/div[2]/text()").get()
        item["fitment"] = response.xpath("//*[@class='maininfo-model']/div[2]/div[2]/text()").get()
        item["time"] = response.xpath("//*[@class='maininfo-model']/div[3]/div[2]/text()").get().strip().replace('\n', '')
        item["location"] = response.xpath("//*[@class = 'maininfo-community']/div[1]/a/text()").get().strip().replace('\n', '')+\
                          response.xpath("//*[@class = 'maininfo-community']/div[2]/span[2]/a[1]/text()").get().strip().replace('\n', '')+\
                          response.xpath("//*[@class = 'maininfo-community']/div[2]/span[2]/a[2]/text()").get().strip().replace('\n', '')
        yield item