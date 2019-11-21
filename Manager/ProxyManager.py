"""
API 逻辑具体实现
"""
from Config.settings import PROXY_GETTER
from DB import DBClient
import random
class ProxyManager:
    def __init__(self):
        self.db = DBClient.DbClient()

    # 从freeproxy 抓取proxy入库
    def fetch(self):
        pass



    def get_proxy(self):
        proxy_dics = self.db.getAll()
        proxy_list = proxy_dics.values()
        proxy = random.choice(proxy_list)
        return proxy

    def get_all_proxy(self):
        proxy_dic = self.db.getAll()
        proxy_list = proxy_dic.values()
        return proxy_list

    def delete_proxy(self, proxy):
        return self.db.delete(proxy)

    def get_proxy_number(self):
        return self.db.getNumber()

    def get_http_proxy(self):
        proxy_dic = self.db.getAll()
        http_proxy_list = list()
        # key 形如 192.168.1.1:8080
        for key, value in proxy_dic.items():
            if value['type'] == 'http':
                http_proxy_list.append(value)
        return http_proxy_list

    def get_https_proxy(self):
        proxy_dic = self.db.getAll()
        http_proxy_list = list()
        # key 形如 192.168.1.1:8080
        for key, value in proxy_dic.items():
            if value['type'] == 'https':
                http_proxy_list.append(value)
        return http_proxy_list
