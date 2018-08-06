# -*- coding: utf-8 -*-

# Scrapy settings for spliderTest1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

#my *arg
TXTPATH = "./pip.txt"
DOUBAN ="./douban.txt"

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
]
PROXIES = ['http://190.2.144.122:1080',
           'http://24.172.82.94:53281',
           'http://103.94.121.67:8080',
           'http://108.187.45.85:41258',
           'http://45.116.159.141:53281',
           'http://46.72.139.247:8080',
           'http://94.141.142.17:41258',
           'http://189.126.66.154:20183',
           'http://187.44.1.167:8080',
           'http://91.232.173.248:8080',
           'http://40.113.66.245:8080',
           'http://186.91.213.168:8080',
           'http://83.219.150.55:41258',
           'http://178.128.40.193:8080',
           'http://138.118.85.208:53281',
           'http://45.77.150.218:80',
           'http://103.247.122.134:8080',
           'http://190.2.144.106:1080',
           'http://151.106.52.230:1080',
           'http://110.36.181.37:8080',
           'http://191.102.51.40:8080',
           'http://177.185.138.193:8080',
           'http://82.107.202.30:8080',
           'http://88.146.96.188:3128',
           'http://165.255.217.122:8080',
           'http://124.195.210.4:8080',
           'http://39.135.35.19:80',
           'http://24.41.167.206:8080',
           'http://160.202.42.195:8080',
           'http://89.26.16.177:8080',
           'http://195.138.91.117:9001',
           'http://95.30.208.20:53281',
           'http://188.92.189.154:41258',
           'http://176.237.57.8:8080',
           'http://200.48.41.5:8080',
           'http://91.147.222.83:41766',
           'http://77.78.153.110:8080',
           'http://118.31.14.52:3128',
           'http://187.210.110.214:53281',
           'http://91.196.159.214:8080',
           'http://189.39.122.142:20183',
           'http://50.79.130.114:8080',
           'http://200.164.65.218:80',
           'http://103.81.104.126:53281',
           'http://181.188.166.82:8080',
           'http://188.253.126.52:8080',
           'http://95.170.215.14:53281',
           'http://105.247.240.90:8080',
           'http://195.91.200.216:8080',
           'http://176.37.78.204:41766',
           'http://144.217.161.149:8080',
           'http://103.88.234.242:53281',
           'http://1.179.185.249:8080',
           'http://125.62.213.134:84',
           'http://109.254.93.195:3128',
           'http://178.140.105.116:9001',
           'http://180.210.204.53:3128',
           'http://191.7.218.226:20183']
# 下载图片的pipelines scrapy都做好了
# items 中图片的url
IMAGES_URLS_FIELD = 'IMG_URL'
# .代表当前路径
IMAGES_STORE = './BaiduImages'
#my *arg

BOT_NAME = 'spliderTest1'

SPIDER_MODULES = ['spliderTest1.spiders']
NEWSPIDER_MODULE = 'spliderTest1.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'spliderTest1.middlewares.Splidertest1SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #'spliderTest1.middlewares.Splidertest1DownloaderMiddleware': 543,
    #'spliderTest1.middlewares.RandomUserAgent':100,
    #'spliderTest1.middlewares.ProxyMiddleware':101
    #'spliderTest1.middlewares.AgentandProxy':1,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
                    #'spliderTest1.pipelines.Splidertest1Pipeline': 300,
                    #'spliderTest1.pipelines.doubanPipeline': 300,
                    #'spliderTest1.pipelines.bookPipeline': 1,
                    #'spliderTest1.pipelines.ProxyPipeline':1,
                    'spliderTest1.pipelines.BaiDuImage':2,
                    #'scrapy.pipelines.images.ImagesPipeline': 1,
                }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
