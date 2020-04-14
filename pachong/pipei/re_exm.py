import requests

import re

url = "http://news.xnnews.com.cn/"
header = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
response = requests.get(url,headers=header)
data=response.content.decode("utf8")

def a_generator(data):
    pattern = re.compile("<a .*?href=(.*?).*?>(.*?)</a>")
    result = pattern.finditer(data)
    return result
with open("a.html","w") as f:
    for i in a_generator(data):
        f.write(i.group())

