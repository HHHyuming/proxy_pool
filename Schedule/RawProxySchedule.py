"""
把数据库raw中无效的proxy换掉
"""
from DB import DBClient
from queue import Queue
from threading import Thread
from Manager.ProxyManager import ProxyManager
from ProxyHelper.Proxy import Proxy
from Utils.verify_proxy import validation
from Config.settings import PROXY_DB_TABLES

class RawProxyCheck(Thread):

    def __init__(self,queue):
        super().__init__()
        self.db = DBClient.DbClient()
        self.queue = queue


    def run(self):
        proxy_dict = self.queue.get()
        self.db.changeTable(PROXY_DB_TABLES.get('useful'))

        proxy_obj = Proxy(proxy=proxy_dict['proxy'], port=proxy_dict['port'], proxy_type=proxy_dict['proxy_type'], source=proxy_dict['source'])

        validation(proxy_obj,self.db)
        self.queue.task_done()
def do_raw_check():
    # 验证数据库中的proxy
    proxy_queue = Queue()
    pm = ProxyManager()
    pm.db.changeTable(pm.db.client.name)

    proxy_dicts = pm.db.getAll()
    for key, value in proxy_dicts.items():
        proxy_queue.put(value)
    pm.db.clear()

    for i in range(proxy_queue.qsize()):
        RawProxyCheck(proxy_queue).start()

    proxy_queue.join()