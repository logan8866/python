import requests

url = "https://weibo.com/6107512706/follow"
header = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
}
#parmas = {"wd":"beautiful girl","value":1}
#proxy = {"http":"121.237.148.139:3000"}
response = requests.get(url,headers=header)#params=parmas,verify=False)
data = response.content#.content.decode("utf8")
"""
print(response.request.url)
#request_header
request_header = response.request.headers
print(request_header)
print("----------------------------\n")
#response_header
response_header = response.headers
print(response_header)
print("-----------------------------\n")
#request_cookie
request_cookie = response.request._cookies
print(request_cookie)
print("-----------------------------\n")
#response_cookie
response_cookie = response.cookies
print(response_cookie)
"""
with open("jingdong.html","wb") as f:
    f.write(data)


