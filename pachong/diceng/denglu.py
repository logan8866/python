import urllib.request
from http import cookiejar
import urllib.parse
import time
def login_it():
    http_header = {
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    url = "https://www.yaozh.com/login/"
    login_data_form = {
            "username":"13256343203",
            "pwd":"wyq123456789",
            "formhash":"A826FF0362",
            "backurl":"https%3A%2F%2Fwww.yaozh.com%2F"
    }
    login_data = urllib.parse.urlencode(login_data_form).encode("utf8")
    request = urllib.request.Request(url,headers=http_header,data=login_data,method="POST")
    cookiejar_1 = cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookiejar_1)
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)
    request = urllib.request.Request("http://www.yaozh.com/member",headers=http_header)
    response = opener.open(request)
    data = response.read().decode("utf8")
    with open("yaozh.html","w") as f:
        f.write(data)


login_it()


