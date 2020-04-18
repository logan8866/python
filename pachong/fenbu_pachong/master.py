import queue
from multiprocessing.managers import BaseManager
import hashlib, pickle
from multiprocessing import Process

class UrlManager:

    def __init__(self):
        self.path_new = './process_new.pkl'
        self.path_old = './process_old.pkl'
        self.new_urls = self.load_process_new()
        self.old_urls = self.load_process_old()
        self.hash_obj = hashlib.md5()

    def has_new_url(self):
        if self.new_urls:
            return True
        else:
            return False

    def add_new_url(self, new_url):
        if not new_url:
            return False
        else:
            self.hash_obj.update(new_url.encode('utf8'))
            new_url_md5 = self.hash_obj.hexdigest()
            if new_url_md5 in self.old_urls:
                return False
            self.new_urls.insert(0, new_url)
            return True

    def pop_new_url(self):
        if not self.new_urls:
            return
        else:
            url = self.new_urls.pop()
            self.hash_obj.update(url.encode('utf8'))
            url_md5 = self.hash_obj.hexdigest()
            self.old_urls.append(url_md5)
            return url

    def new_urls_size(self):
        return len(self.new_urls)

    def old_urls_size(self):
        return len(self.old_urls)

    def add_new_urls(self, new_url_list):
        for url in new_url_list:
            self.add_new_url(url)

        return True

    def save_process(self):
        with open(self.path_new, 'wb') as (f):
            pickle.dump(self.new_urls, f)
        with open(self.path_old, 'wb') as (f):
            pickle.dump(self.old_urls, f)

    def load_process_new(self):
        try:
            with open(self.path_new, 'rb') as (f):
                return pickle.load(f)
        except:
            return list()

    def load_process_old(self):
        try:
            with open(self.path_old, 'rb') as (f):
                return pickle.load(f)
        except:
            return list()

    def __del__(self):
        self.save_process()
        print('Bey Bey')


class SpiderManager:

    def __init__(self, url_manager,data_storer):
        self.url_manager = url_manager
        self.data_storer = data_storer

    def get_manager(self, task_queue, result_queue, conn_queue, store_queue):

        def _return_task_queue():
            return task_queue

        def _return_result_queue():
            return result_queue

        def _return_conn_queue():
            return conn_queue

        def _return_store_queue():
            return store_queue

        BaseManager.register('get_task_queue', callable=_return_task_queue)
        BaseManager.register('get_result_queue', callable=_return_result_queue)
        BaseManager.register('get_conn_queue', callable=_return_conn_queue)
        BaseManager.register('get_store_queue', callable=_return_store_queue)
        manager = BaseManager(address=('127.0.0.1', 5001), authkey=b'abc')
        return manager

    def url_manager_processing(self, task_queue, conn_queue, start_url):
        self.url_manager.add_new_url(start_url)
        while 1:
            if self.url_manager.has_new_url():
                new_url = self.url_manager.pop_new_url()
                if new_url == 'end':
                    task_queue.put('end')
                    self.url_manager.save_process()
                    return
                task_queue.put(new_url)

            if not conn_queue.empty():
                urls = conn_queue.get()
                self.url_manager.add_new_urls(urls)

    def result_processing(self, conn_queue, result_queue, store_queue):
        while True:
            if not result_queue.empty():
                content = result_queue.get()
                if content['new_urls'] == 'end':
                    conn_queue.put('end')
                    return
                new_urls = content['new_urls']
                conn_queue.put(new_urls)
                data = content['data']
                store_queue.put(data)

    def store_processing(self, store_queue):
        while True:
            if not store_queue.empty():
                data = store_queue.get()
                if data == 'end':
                    del self.data_storer
                    return
                self.data_storer.store_file(data)

class DataStorer():

    def __init__(self):
        self.datas = list()
        self.store_path = "./store.html"
        self.start_store()
        self.count = 0

    def __del__(self):
        self.end_store()

    def start_store(self):
        f = open(self.store_path,"w")
        f.write("<html>")
        f.write("<body>")
        f.close()

    def data_store(self,data):
        self.datas.append(data)
        if len(self.datas) == 10:
            f = open(self.store_path,"a")
            for data in self.datas:
                f.write(str(data))
            self.datas = []
            f.close()
        else:
            return
    
    def store_file(self,data):
        for text in data:
            f = open("./img/"+str(self.count)+".jpg","wb")
            f.write(text)
            f.close()
            self.count+=1

    def end_store(self):
        f = open(self.store_path,"a")
        f.write("</body>")
        f.write("</html>")
        f.close()









