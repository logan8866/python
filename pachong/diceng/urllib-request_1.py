import urllib.request
import urllib.parse

def downloader():
    url = "http://www.tupianzj.com/meinv/siwa/"
    response = urllib.request.urlopen(url)
    data = response.read().decode("gbk")
    with open("meinv.html",'w') as f:
        f.write(data)

def parse_chinese():
    url = "http://baidu.com/s?wd="
    sousuo = "美女"
    new_url = urllib.parse.quote(sousuo)
    new_url = url+new_url
    print(new_url)
    response = urllib.request.urlopen(new_url)
    data = response.read()
    with open("baidu.html","wb") as f:
        f.write(data)

def urlencode_test():
    url = "http://baidu.com/"
    parmas = {
            "wd":"nihao",
            "key":"zhang",
            "value":"san"
    }
    parmas = urllib.parse.urlencode(parmas)
    print(url+parmas)

def agent():
    url = "http://www.tupianzj.com/meinv/siwa/"
    parmas = {
            "wd":"meinv",
    }
    parmas = urllib.parse.urlencode(parmas)
    final_url = url+parmas
    request = urllib.request.Request(final_url)
    print(request.headers)
    header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }
    request.add_header("User-Agent",header.get("User-Agent"))
    print(request.get_header("User-agent"))
    response = urllib.request.urlopen(url)
    data = response.read()
    with open("baidu_2.html","wb") as f:
        f.write(data)




"""
downloader()
parse_chinese()
urlencode_test()
"""
print("--------------------------------------")
agent()
