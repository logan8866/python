import urllib.request
def daili():
    url = "http://www.tupianzj.com/meinv/siwa/"
    proxy = {
            "http":"http://121.227.89.58:8118",
    }
    handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    data = response.read()
    with open("hello.html","wb") as f:
        f.write(data)

daili()
