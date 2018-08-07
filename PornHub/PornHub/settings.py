# -*- coding: utf-8 -*-

# Scrapy settings for pornhub project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'PornHub'

SPIDER_MODULES = ['PornHub.spiders']
NEWSPIDER_MODULE = 'PornHub.spiders'

#设置图片保存到本地的地址和过期时间
IMAGES_STORE='/Users/payu/Pictures/Meizi'
IMAGES_EXPIRES = 90

DOWNLOAD_DELAY = 1  # 间隔时间
# LOG_LEVEL = 'INFO'  # 日志级别
CONCURRENT_REQUESTS = 20  # 默认为16
# CONCURRENT_ITEMS = 1
# CONCURRENT_REQUESTS_PER_IP = 1
REDIRECT_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pornhub (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
    # 'PornHub.middlewares.RandomUserAgent': 1,
    "PornHub.middlewares.UserAgentMiddleware": 401,
    "PornHub.middlewares.CookiesMiddleware": 402,
}

ITEM_PIPELINES = {
    "PornHub.pipelines.PornhubMongoDBPipeline": 403,
    "PornHub.pipelines.ImageCachePipeline": 500,
}

FEED_URI=u'C:/Users/payu/Documents/pornhub.csv'
FEED_FORMAT='CSV'

DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'
