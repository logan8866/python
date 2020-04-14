import scrapy
class CarXiu(scrapy.Spider):
    name = "carxiu"
    start_urls = ["https://www.chexiu.com/search/list-0-6-0-0-0-0-0-1.html"]
    def __init__(self):
        self.time = 1
    def parse(self,response):
        for car_div in response.xpath('//div[@class="m g-fl"]'):
            r = {
                    "car_name":car_div.xpath('./a/div[@class="text"]/h3/text()').extract_first(),
                    "car_price":car_div.xpath('./a/div[@class="bottom"]/span[@class="price"]/em/text()').extract_first(),
                    "car_foto":car_div.xpath('./a/img/@data-src').extract_first()
            }
            yield r
        self.time+=1
        if self.time<13:
            yield scrapy.Request("https://www.chexiu.com/search/list-0-6-0-0-0-0-0-%d.html"%self.time)

