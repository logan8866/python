import requests
from bs4 import BeautifulSoup
import csv

def downloader(url):
    user_agent = {
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    response = requests.get(url,headers=user_agent)
    data = response.content.decode("utf8")
    return data

def generator_list(list_dist):
    for i in list_dist:
        yield i

def generator_data(data):
    soup = BeautifulSoup(data,"lxml")
    detail_list = soup.select(".grid-item")
    data_dict = {}
    for div in generator_list(detail_list):
        img_url = div.select(".thumb a")[0].get("href")
        data_dict["img_url"] = "https://www.ywart.com/"+img_url
        detail = div.select(".detail")[0]
        p_list = detail.select("p")
        data_dict["auther"] = p_list[0].select_one("a").get_text()
        data_dict["name"] = p_list[1].select_one("a").get_text()
        data_dict["year"] = p_list[1].select_one("span").get_text()
        data_dict["cailiao"] = p_list[2].select("span")[0].get_text()
        data_dict["area"] = p_list[2].select("span")[1].get_text()
        data_dict["price"] = p_list[3].get_text()
        yield data_dict

class Saver():
    def __init__(self):
        self.csv_fp = open("data.csv","w")
        self.writer = csv.writer(self.csv_fp)
        self.writer.writerow(["img_url","auther","name","year","cailiao","area","price"])
    def save(self,data_dict):
        self.writer.writerow(data_dict.values())

    def __del__(self):
        self.csv_fp.close()

def main():
    url = "https://www.ywart.com/buy?category=%E6%B2%B9%E7%94%BB&page="
    saver = Saver()
    for i in range(230):
        url_now = url+str(i)
        data = downloader(url)
        for data_dict in generator_data(data):
            saver.save(data_dict)
if __name__ == "__main__":
    main()
