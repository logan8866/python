import urllib.request

def admin_yanzheng():
    username = "wangyiqing"
    password = "wyq123456789"
    url = "http://www.baidu.com"
    manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    manager.add_password(None,url,username,password)
    handler = urllib.request.HTTPBasicAuthHandler(manager)
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    data = response.read()
    with open("hello_2.html","w") as f:
        f.write(data.decode("utf8"))

admin_yanzheng()
