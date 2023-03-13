# Scrapy settings for Scrapy1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Scrapy1'

SPIDER_MODULES = ['Scrapy1.spiders']
NEWSPIDER_MODULE = 'Scrapy1.spiders'

# LOG_FILE='all.log'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/4.0'
IPPOOL=[
#
#
#
#
#
#
#
#
#
#

# {"ipaddr": "http://183.166.145.156:4273"},
# {"ipaddr": "http://114.239.1.52:4212"},
# {"ipaddr": "http://117.34.192.128:4210"},
# {"ipaddr": "http://114.104.141.99:4278"},
# {"ipaddr": "http://117.26.193.93:4245"},
# {"ipaddr": "http://60.172.83.42:4231"},
# {"ipaddr": "http://61.188.26.230:4210"},
# {"ipaddr": "http://139.203.22.219:4227"},
# {"ipaddr": "http://111.72.137.27:4230"},
# {"ipaddr": "http://42.87.57.169:4270"}
{"ipaddr": "http://58.243.29.124:4231"},
{"ipaddr": "http://114.99.222.234:4226"},
{"ipaddr": "http://27.155.219.12:4245"},
{"ipaddr": "http://120.43.97.92:4214"},
{"ipaddr": "http://114.239.198.176:4245"},
{"ipaddr": "http://113.128.123.216:4242"},
{"ipaddr": "http://117.69.146.251:4247"},
{"ipaddr": "http://60.166.163.244:4227"},
{"ipaddr": "http://175.165.231.0:4210"},
{"ipaddr": "http://121.57.84.127:4235"}

]


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#
#    # 'Scrapy1.middlewares.Scrapy1SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
      'Scrapy1.middlewares.SeleniumMiddleware': 90,
      'Scrapy1.middlewares.IPProxiesMiddleware': 80,

}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
   'scrapy.extensions.telnet.TelnetConsole': None,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Scrapy1.pipelines.Scrapy1BaoChun': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
DUPEFILTE_CLASS='scrapy_redis.dupefilter.RFPDupeFilter'
SCHDULER='scrapy_redis.scheduler.Scheduler'

SCHEDULER_PERSIST=True

# ITEM_PIPELINES = {
#    'Tushu.pipelines.TushuPipeline': 300,
# }

REDIS_URL = 'redis://127.0.0.1:6379'