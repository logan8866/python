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
        
    def downloader(self,url):
        response = requests.get(url,headers=self.agent)
        if requests.status_code == 200:
            return response.content.decode("utf8")
        else:
            return None




















