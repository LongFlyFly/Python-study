# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import base64
import random
import time
from scrapy import signals

# useful for handling different item types with a single interface

from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from scrapy.http import HtmlResponse
from selenium import webdriver

from Scrapy1.settings import IPPOOL


class Scrapy1SpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Scrapy1DownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SeleniumMiddleware(object):
#初始化浏览器驱动，设置无界面模式
    def process_request(self,request,spider):

        user_list = get_user()  # 获取用户代理列表
        ua = random.choice(user_list)  # 获取随机用户代理
        current_ip = random.choice(IPPOOL)
        currentip = current_ip["ipaddr"]
        opt = webdriver.ChromeOptions()
        opt.add_argument('--head')
        opt.add_experimental_option("excludeSwitches", ['enable-automation'])
        opt.add_experimental_option('useAutomationExtension', False)
        opt.add_argument('user-agent="'+ua+'"')
        # opt.add_argument("--proxy-server="+currentip)
        print(currentip)

        url = request.url
        print(url)
        driver = webdriver.Chrome(executable_path="D:\chromedriver\chromedriver.exe",options=opt)
        try:
            driver.get(url)
            time.sleep(random.randint(0, 1))
            data = driver.page_source
            driver.delete_all_cookies()
            driver.close()
            return HtmlResponse(url=url, body=data, encoding='utf-8', request=request)
        except:
            return HtmlResponse(url=url,  encoding='utf-8', request=request)

# class ChromeOptions:
#     pass
#

# class SeleniumMiddleware():
# #初始化浏览器驱动，设置无界面模式
#     def __init__(self):
# #配置无界面浏览器模式，使用Chrom浏览器
#         opt = ChromeOptions()         # 创建Chrome参数对象
#         opt.headless = True           # 把Chrome设置成无界面模式，windows/Linux 皆可
#         opt.add_argument("--disable-gpu")
#         self.browser = Chrome(options=opt) #实例化浏览器驱动
#         super().__init__()
# #发送请求，返回响应对象
#     def process_request(self, request, spider):
#         try:
#             self.browser.get(request.url) #发送请求
#             time.sleep(4)  #设置等待时间，等待时间可在settings.py文件中配置
# #返回response对象，其中参数self.browser.page_source为返回html文本
#             return HtmlResponse(url=request.url, body=self.browser.page_source,
#                     request=request,encoding='utf-8')
#         except TimeoutException:
#             return HtmlResponse(url=request.url, status=500, request=request)
# class RandomProxy(HttpProxyMiddleware):
#     def get_proxyList(self):
#         pass
#     def process_request(self):
#         pass
#


def get_user():
    with open("D:\python1\Scrapy1\用户代理.txt", "r", encoding="utf8") as f:
        user_list = f.readlines()
        f.close()
    return user_list

class IPProxiesMiddleware(HttpProxyMiddleware):#必须使用继承
    def process_request(self, request, spider):
        current_ip = random.choice(IPPOOL) #随机获取一个ip字典

        user_list=get_user()#获取用户代理列表
        ua = random.choice(user_list) #获取随机用户代理
        request.headers.setdefault('User-Agent', ua) #设置请求头
        print(ua)
        time.sleep(5)
        # 判断IP是否为免费ip
        if 'user_pws' in current_ip:
            # 对密码账号进行加密
            bs64_up = base64.b64encode(current_ip["user_pws"].encode())
            request.headers['Proxy-Authorization'] = 'Basic '+bs64_up.decode()
            # 设置IP代理
            currentip = current_ip["ipaddr"]
            request.meta["proxy"] = currentip
        else:
            # 设置ip代理
            currentip = current_ip["ipaddr"]
            request.meta["proxy"] = currentip

        print("currentip:", currentip)
        # print("currentUseragent:",ua)

