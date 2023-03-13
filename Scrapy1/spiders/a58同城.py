import scrapy

from Scrapy1.items import Scrapy1Item

def get_text(list_all):
    str = ""
    for i in list_all:
        str = str + i
    return str

def get_star_urls(num):
    url_list = []
    for i in range(3, num):
        url_list.append('https://cq.58.com/ershoufang/'+"p"+str(i))
    return url_list

class A58同城Spider(scrapy.Spider):
    name = '58同城'
    allowed_domains = ['cq.58.com']
    start_urls = get_star_urls(4)

    def parse(self, response):
        i = 0
        all_list = response.xpath("//div[@tongji_tag='fcpc_ersflist_gzcount']")
        print("开始抓取数据1")
        # print(all_list[1].extract(    ))

        for all in all_list:
            i = i + 1
            print("开始抓取数URL",i)
            item = Scrapy1Item()
            url = all.xpath(".//a[@class='property-ex']/@href")[0].extract()
            item['selling_points'] = all.xpath(".//h3/@title")[0].extract()
            t1=all.xpath(".//p[@class='property-price-total']/span[@class='property-price-total-num']//text()")[0].extract()
            t2=all.xpath(".//p[@class='property-price-total']/span[@class='property-price-total-text']//text()")[0].extract()
            item['total_prices']=t1+t2
            item['unit_price'] = all.xpath(".//p[@class='property-price-average']//text()")[0].extract()
            yield scrapy.Request(url=url,meta={'item':item},callback=self.parse2)

    def parse2(self,response):
        print("开始抓取数据2")
        item = response.meta['item']
        ## 户型
        item['house_type'] = get_text(response.xpath("//div[@class='maininfo-model-item maininfo-model-item-1']/div[@class='maininfo-model-strong']//text()").extract())
    # # 面积
        item['area'] = get_text(response.xpath("//div[@class='maininfo-model-item maininfo-model-item-2']/div[@class='maininfo-model-strong']//text()").extract())
    # # 朝向
        item['orientation'] = get_text(response.xpath("//div[@class='maininfo-model-item maininfo-model-item-3']/div[@class='maininfo-model-strong']//text()").extract())
    # # 装修情况
        item['secorate_situatino'] = get_text(response.xpath("//div[@class='maininfo-model-item maininfo-model-item-2']/div[@class='maininfo-model-weak']//text()").extract())
    #  # 楼层
        item['floor'] = get_text(response.xpath("//div[@class='maininfo-model-item maininfo-model-item-1']/div[@class='maininfo-model-weak']//text()").extract())
    # # 建筑年代)
        item['building_age'] = get_text(response.xpath("//div[@class='maininfo-model-item maininfo-model-item-3']/div[@class='maininfo-model-weak']//text()").extract())
    #  # 所属小区
        item['plot'] = get_text(response.xpath("//div[@class='maininfo-community-item'][1]/a[1]//text()").extract())
    # 所在区域
        item['region'] = get_text(response.xpath("//div[@class='maininfo-community-item'][2]/span[2]//text()").extract())
        yield item


