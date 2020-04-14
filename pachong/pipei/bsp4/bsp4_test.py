from bs4 import BeautifulSoup
import requests 

header = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
url = "http://data.cnstock.com/thematic/blockTrading.html"

response = requests.get(url,headers = header)
data = response.content.decode("utf8")
#with open("stock.html","w") as f:
#    f.write(data)
soup = BeautifulSoup(data,'lxml')
result = soup.prettify()
result = soup.table
result = result.select("tr")
ziduan = result[0]
result = result[1:]
list_ziduan = []
for i in ziduan.select("th"):
    list_ziduan.append(i.get_text())
list_1 = {}
list_r = []
for i in result:
    list_1 = {}
    for j in range(len(list_ziduan)):
        list_1[list_ziduan[j]] = i.select("td")[j].get_text()
    list_r.append(list_1)
import json
with open("data.json","w") as f:
    json.dump(list_r,f)

import csv
fp = open("data.csv","w")
writter = csv.writer(fp)
writter.writerow(list_ziduan)
data_list = []
for i in list_r:
    data_list.append(i.values())
writter.writerows(data_list)
fp.close()


