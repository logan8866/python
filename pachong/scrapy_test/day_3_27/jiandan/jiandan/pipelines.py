# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.exceptions import DropItem

class JiandanPipeline(ImagesPipeline):

    def get_media_requests(self,item,info):
        for url in item["foto_url"]:
            url_ok = "http:"+url
            yield scrapy.Request(url_ok)
    
    def item_completed(self,results,item,info):
        image_path = [x['path'] for ok,x in results if ok]
        if not image_path:
            raise DropItem("no image")
        return item

