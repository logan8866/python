from lxml import etree
import requests

header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}
url = "https://www.chexiu.com/search/list-0-6-0-0-0-0-0-12.html"
response = requests.get(url,headers = header)
data = response.content.decode("utf8")
etree_data = etree.HTML(data)
result_1 = etree_data.xpath('//div[@class="m g-fl"]')
print(result_1)
for result in result_1:
    result_2 = result.xpath('./a/div[@class="text"]/h3/text()')
    print(result_2)
