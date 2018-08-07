# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from pymongo import IndexModel, ASCENDING
from PornHub.items import PornVideoItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import json


class PornhubMongoDBPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["PornHub"]
        self.PhRes = db["PhRes"]
        idx = IndexModel([('link_url', ASCENDING)], unique=True)
        self.PhRes.create_indexes([idx])
        # if your existing DB has duplicate records, refer to:
        # https://stackoverflow.com/questions/35707496/remove-duplicate-in-mongodb/35711737

    def process_item(self, item, spider):
        print('MongoDBItem', item)
        """ 判断类型 存入MongoDB """
        if isinstance(item, PornVideoItem):
            print('PornVideoItem True')
            try:
                self.PhRes.update_one({'link_url': item['link_url']}, {'$set': dict(item)}, upsert=True)
            except Exception:
                pass
        return item


class ImageCachePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        pics = item['pics']
        list = json.loads(pics)
        for image_url in list:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths=[x['path'] for ok,x in results if ok]
        if not image_paths:
            print("图片未下载好:%s" % image_paths)
            raise DropItem('图片未下载好 %s'%image_paths)