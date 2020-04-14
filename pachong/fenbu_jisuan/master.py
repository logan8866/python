import random
import queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

class MasterManager(BaseManager):
    pass

def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

MasterManager.register("get_task_queue",callable=return_task_queue)
MasterManager.register("get_result_queue",callable=return_result_queue)

master_manager = MasterManager(address=('127.0.0.1',5001),authkey=b"abc")

master_manager.start()

task_queue = master_manager.get_task_queue()
result_queue = master_manager.get_result_queue()

for i in range(10):
    task_queue.put(i)

for i in range(10):
    result = result_queue.get(timeout=5)
    print(result)



