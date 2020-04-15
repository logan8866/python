from multiprocessing.managers import BaseManager
import requests
from bs4 import BeautifulSoup

class NodeSpider():

    def __init__(self):
        BaseManager.register("get_task_queue")
        BaseManager.register("get_result_queue")
        self.address = ("127.0.0.1",5002)
        self.manager = BaseManager(address=self.address,authkey=b"abc")
        try:
            self.manager.connect()
        except:
            print("no master")
        self.task_queue = self.manager.get_task_queue()
        self.result_queue = self.manager.get_result_queue()
        self.downloader = HTMLDownloader()
        self.parse = HTMLParse()

    def crawl(self):
        while True:
            if self.task_queue.empty():
                url = self.task_queue.get()
                if url == "end":
                    self.result_queue.put({"new_urls":url,"data":url})
                    return 
                content = self.downloader.download(url)
                urls,data = self.parse.parse(content)
                self.result_queue.put({"new_urls":urls,"data":data})

        return


class HTMLDownloader():

    def __init__(self):
        self.agent = {
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
        }
        
    def download(self,url):
        response = requests.get(url,headers=self.agent)
        if response.status_code == 200:
            return response.content.decode("utf8")
        else:
            return None


class Parse():

    def __init__(self):
        self.url_header = "http:"

    def parse(self,content):
        self.soup = BeautifulSoup(content,"lxml")
        self.soup.prettify()
        next_urls = self._find_next_urls()
        data = self._find_data()
        return next_urls,data

    def _find_next_urls(self):
        urls = self.soup.select("a[class='previous-comment-page']")
        next_urls = list()
        next_urls.append(self.url_header+urls[0].get("href"))
        return next_urls

    def _find_data(self):
        imgs = self.soup.select("img[referrerpolicy='no-referrer']")
        data = list()
        for img in imgs:
            url = self.url_header+img.get("src")
            data.append(url)
        return data



















