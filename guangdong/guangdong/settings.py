# -*- coding: utf-8 -*-

# Scrapy settings for gaungdong project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'guangdong'

SPIDER_MODULES = ['guangdong.spiders']
NEWSPIDER_MODULE = 'guangdong.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'guangdong (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
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
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'gaungdong.middlewares.GaungdongSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'gaungdong.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #'gaungdong.pipelines.GaungdongPipeline': 300,
    'guangdong.pipelines.MsSQLDALPipeline': 200,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# start MySQL database configure setting
MSSQL_SERVER ='218.241.178.211'
MSSQL_DB ='CrawData'
MSSQL_USER ='cfc'
MSSQL_PASSWORD ='!QAZxsw2'
# end of MySQL database configure setting

#mssql excute setting
QUERY={"mes_gd":'''INSERT INTO mes_guangdongss (credit_num,re_num,
or_name,or_type,or_date,manager,person,address,city) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''}
#end of mssql excute setting

#访问链接
URLS=['茂名','江门','揭阳','云浮市']
#茂名市
# url1 = 'http://mm.gdnpo.gov.cn/home/publist2/webmjzzlist'
# #江门市
# url2= 'http://jm.gdnpo.gov.cn/home/publist2/webmjzzlist'
# #揭阳市
# url3='http://jy.npo.gdnpo.gov.cn/home/publist2/webmjzzlist'
# #云浮市
# url4='http://yf.npo.gdnpo.gov.cn/home/publist2/webmjzzlist'
# #潮州市
# #url5='http://cznpo.czmzw.gov.cn/info8/mjzzlist.html'
# #中山市
# #url6='http://zhongshan.gdnpo.jmeii.com/info8/mjzzlist.html'
# #东莞市
# url7='http://dg.gdnpo.gov.cn/home/publist2/webmjzzlist'
# #清远市
# url8='http://qy.gdnpo.gov.cn/home/publist2/webmjzzlist'
# #阳江市
# url9='http://yj.npo.gdnpo.gov.cn/home/publist2/webmjzzlist'
# #汕尾市
# url0='http://sw.npo.gdnpo.gov.cn/home/publist2/webmjzzlist'
# #梅州市
# url11='http://mz.npo.gdnpo.gov.cn/home/publist2/webmjzzlist'
# #惠州市
# url12='http://hz.npo.gdnpo.gov.cn/home/publist2/webmjzzlist'
# URLS={url1:'茂名市',url2:'江门市',url3:'揭阳市',url4:'云浮市'}