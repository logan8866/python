import scrapy
from dianshang.items import DianshangItem

class Wangshangyuan(scrapy.Spider):
    name = "wangshangyuan"
    start_urls = ["https://www.wsy.com/category.htm?cid=50000436&page=1"]
    def __init__(self):
        self.time = 1
        self.item = DianshangItem()

    def parse(self,response):
        ware_divs = response.xpath("//div[@class='item-c clearfix']/div[@class='item posR']")
        for ware_div in ware_divs:
            self.item["foto_url"] = ware_div.xpath("./div[@class='pic']/a/img/@data-original").extract_first()
            self.item["name"] = ware_div.xpath("./div[@class='tit']/a/text()").extract_first()
            self.item["price"] = ware_div.xpath("./div[@class=' pri-look clearfix']/div[@class='pri fl']/strong/text()").extract_first()
            self.item["click_num"] = ware_div.xpath("./div[@class=' pri-look clearfix']/div[@class='fr look']/span/text()").extract_first()
            yield self.item
        if self.time<101:
            self.time+=1
            yield scrapy.Request("https://www.wsy.com/category.htm?cid=50000436&page=%d"%self.time)


