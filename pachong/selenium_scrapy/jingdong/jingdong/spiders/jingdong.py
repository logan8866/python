import scrapy
from jingdong.items import JingdongItem
import scrapy_redis
from scrapy_redis.spiders import RedisSpider
import time 

class JingdongSpider(RedisSpider):
    name = "jingdong"
    redis_key = "jingdong"
    #start_urls = ["https://search.jd.com/Search?keyword=%E6%89%8B%E8%A1%A8&enc=utf-8&page=1"]

    def __init__(self):
        self.page = 0
        self.item = JingdongItem()
        self.url_mode = "https://search.jd.com/Search?keyword=%E6%89%8B%E8%A1%A8&enc=utf-8&page={}"
        self.counter = 1

    def parse(self,response):
        self.page+=1
        for i in range(20):
            yield scrapy.Request(self.url_mode.format((i+2)*2+1))
        lis = response.xpath("//li[@class='gl-item']")
        for li in lis:
            self.item["img_url"] = li.xpath("./div[@class='gl-i-wrap']/div[@class='p-img']/a/img/@source-data-lazy-img").extract_first()
            self.item["title"] = li.xpath("./div[@class='gl-i-wrap']/div[@class='p-name p-name-type-2']/a/@title").extract_first()
            self.item["price"] = li.xpath("./div[@class='gl-i-wrap']/div[@class='p-price']/strong/i/text()").extract_first()
            yield self.item




