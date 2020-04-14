# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import car_50.settings as settings

class CarPipeline(object):
    def __init__(self):
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        db_name = settings.MONGODB_DBNAME
        client = pymongo.MongoClient(host=host,port=port)
        db = client.admin
        pwd = settings.MONGODB_PASSWORD
        username = settings.MONGODB_USERNAME
        db.authenticate(username,pwd)
        db = client[db_name]
        self.table_name = settings.MONGODB_DOCNAME
        self.table = db[self.table_name]
    
    def process_item(self,item,spider):
        car = dict(item)
        self.table.insert_one(car)
        return item
