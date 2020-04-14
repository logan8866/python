from multiprocessing.managers import BaseManager

class SlaveManager(BaseManager):
    pass

SlaveManager.register("get_task_queue")
SlaveManager.register("get_result_queue")

slave_manager = SlaveManager(address=("127.0.0.1",5001),authkey=b"abc")
slave_manager.connect()

task_queue = slave_manager.get_task_queue()
request_queue = slave_manager.get_result_queue()

for i in range(10):
    task = task_queue.get(timeout=5)
    task = task+2
    request_queue.put(task)

