from master import *
from multiprocessing import Process
import queue

def run_master():
    start_url = "http://jandan.net/ooxx"
    url_manager = UrlManager()
    data_storer = DataStorer()
    master_spider = SpiderManager(url_manager,data_storer)
    task_queue = queue.Queue()
    result_queue = queue.Queue()
    conn_queue = queue.Queue()
    store_queue = queue.Queue()
    manager = master_spider.get_manager(task_queue,result_queue,conn_queue,store_queue)
    manager.start()
    task_queue = manager.get_task_queue()
    result_queue = manager.get_result_queue()
    conn_queue = manager.get_conn_queue()
    store_queue = manager.get_store_queue()
    url_manager_process = Process(target=master_spider.url_manager_processing,args=(task_queue,conn_queue,start_url))
    result_process = Process(target=master_spider.result_processing,args=(conn_queue,result_queue,store_queue))
    store_process = Process(target=master_spider.store_processing,args=(store_queue,))
    url_manager_process.start()
    result_process.start()
    store_process.start()
    while True:
        pass

if __name__ == "__main__":
    run_master()

