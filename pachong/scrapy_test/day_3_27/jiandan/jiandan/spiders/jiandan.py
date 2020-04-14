import scrapy
from jiandan.items import JiandanItem

class JiandanSpider(scrapy.Spider):
    
    name = "jiandan"
    start_urls = ["http://jandan.net/ooxx"]
    
    def __init__(self):
        self.item = JiandanItem()

    def parse(self,response):
        next_url = response.xpath("//a[@class='previous-comment-page']/@href").extract_first()
        yield scrapy.Request("http:"+next_url)
        rows = response.xpath("//div[@class='row']")
        for row in rows:
            self.item['foto_url'] = row.xpath("./div[@class='text']/p/img/@src").extract()
            yield self.item

