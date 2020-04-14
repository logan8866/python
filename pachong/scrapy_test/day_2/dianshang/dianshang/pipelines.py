# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import dianshang.settings as settings

class WangshangyuanPipeline(object):
    def __init__(self,host,port,name,pwd,dbname):
        self.client = pymongo.MongoClient(host,port)
        db = self.client["admin"]
        db.authenticate(name,pwd)
        self.db = self.client[dbname]
    
    @classmethod
    def from_crawler(cls,crawler):
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        name = settings.MONGODB_USER
        pwd = settings.MONGODB_PWD
        dbname = settings.MONGODB_DBNAME
        return cls(
                host,port,name,pwd,dbname
        )
    
    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        dict_save = {
                "foto_url":item["foto_url"],
                "name":item["name"],
                "price":float(item["price"]),
                "click_num":float(item["click_num"])
        }
        docname = settings.MONGODB_DOCNAME
        self.db[docname].insert_one(dict_save)
        return item
