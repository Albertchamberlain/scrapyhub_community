# -*- coding: utf-8 -*-

# Scrapy settings for xiaoqu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiaoqu'

SPIDER_MODULES = ['xiaoqu.spiders']
NEWSPIDER_MODULE = 'xiaoqu.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 49

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 49
CONCURRENT_REQUESTS_PER_IP = 49

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'xiaoqu.middlewares.XiaoquSpiderMiddleware': 543,
# }
# RETRY_TIMES = 1 # 自定义请求失败重试次数
# #重试的包含的错误请求代码
# RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
# PROXY_LIST = r'D:\\cmder\\community_spiders\\proxies.txt'  # proxy 代理文件存放位置，此处为程序所在磁盘根目录下
# PROXY_MODE = 0 # 每次请求都使用不同的

#代理模式
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings

# 代理
# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html

# DOWNLOADER_MIDDLEWARES = {
#     # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
#     # 'scrapy_proxies.RandomProxy': 100,
#     # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None, # 关闭默认方法
#     'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400, # 开启
# }
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'xiaoqu.pipelines.XiaoquRedisPipeline': 1,
    'xiaoqu.pipelines.MysqlPipeline': 2,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': ,
    'Host': 'sz.loupan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Upgrade-Insecure-Requests': 1,
}
LOG_LEVEL = 'ERROR'
RETRY_ENABLED = False
#DOWNLOAD_TIMEOUT = 10

MYSQL_HOST = '123.43.2.72'
MYSQL_DATABASE = 'jobspider'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'houboxue'
MYSQL_PORT = 3306
