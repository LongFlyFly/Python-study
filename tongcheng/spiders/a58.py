import scrapy

from tongcheng.items import TongchengItem


class A58Spider(scrapy.Spider):
    name = '58'
    allowed_domains = ['www.cq.58.com']
    start_urls = ['https://cq.58.com/ershoufang/' + str(i)
                  for i in range(0, 6)]

    def parse(self, response):
        global url, item
        for row in response.xpath("/html/body/div[1]/div/div/section/section[3]/section[1]/section[2]/div"):
            items = TongchengItem()
            url = row.xpath("a/@href").get()
            items["url"] = url

            items["DanJia"] = row.xpath('a/div[2]/div[1]/div[1]/h3/text()').get()

            items["ZongJia"] = row.xpath('a/div[2]/div[2]/p[1]/span[1]/text()').get()

            items["MaiDian"] = row.xpath('a/div[2]/div[2]/p[2]/text()').get()

            items["HuXing"] = row.xpath('./p/text()').get()

            items["`MianJi`"] = row.xpath('./p/text()').get()

            items["ChaoXiang"] = row.xpath('./p/text()').get()

            items["ZhuangXiu"] = row.xpath('./p/text()').get()

            items["Floors"] = row.xpath('./p/text()').get()

            items["Year"] = row.xpath('./p/text()').get()

            items["XiaoQu"] = row.xpath('./p/text()').get()

            items["QuYu"] = row.xpath('./p/text()').get()
            yield items
