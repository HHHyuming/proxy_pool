"""
API 逻辑具体实现
"""
from ProxyGetter import ProxyGetter
from Config.settings import PROXY_GETTER,DATABASE,PROXY_DB_TABLES
from DB import DBClient
from ProxyHelper.Proxy import Proxy
from Utils.verify_proxy import validation
from threading import Thread
from types import GeneratorType
from Config.settings import PROXY_DB_TABLES
import random
class ProxyManager:
    def __init__(self):
        self.db = DBClient.DbClient()

    # 从freeproxy 抓取proxy入库
    def fetch(self):
        for getter in PROXY_GETTER:
            getter_generator = getattr(ProxyGetter.ProxyGetter,getter)()
            if not isinstance(getter_generator,GeneratorType):
                continue
            try:
                for proxy, port, proxy_type in getter_generator:
                    self.db.changeTable(PROXY_DB_TABLES.get('raw'))
                    proxy_obj = Proxy(proxy=proxy,port=port,proxy_type=proxy_type,source=getter)
                    Thread(target=validation,args=(proxy_obj,self.db)).start()
            except Exception as e:
                print(e)
                continue


    def get_proxy(self):
        self.db.changeTable(PROXY_DB_TABLES.get('useful'))
        proxy_dics = self.db.getAll()
        proxy_list = proxy_dics.values()
        proxy = random.choice(list(proxy_list))
        return proxy

    def get_all_proxy(self):
        self.db.changeTable(PROXY_DB_TABLES.get('useful'))
        proxy_dic = self.db.getAll()
        proxy_list = list(proxy_dic.values())
        return proxy_list

    def delete_proxy(self, proxy):
        self.db.changeTable(PROXY_DB_TABLES.get('useful'))
        return self.db.delete(proxy)

    def get_proxy_number(self):
        self.db.changeTable(PROXY_DB_TABLES.get('useful'))
        return self.db.getNumber()

    def get_http_proxy(self):
        self.db.changeTable(PROXY_DB_TABLES.get('useful'))
        proxy_dic = self.db.getAll()
        http_proxy_list = list()
        # key 形如 192.168.1.1:8080
        for key, value in proxy_dic.items():
            print(value)
            if value['proxy_type'].lower() == 'http':
                http_proxy_list.append(value)
        return http_proxy_list

    def get_https_proxy(self):
        self.db.changeTable(PROXY_DB_TABLES.get('useful'))
        proxy_dic = self.db.getAll()
        http_proxy_list = list()
        # key 形如 192.168.1.1:8080
        for key, value in proxy_dic.items():
            if value['proxy_type'].lower() == 'https':
                http_proxy_list.append(value)
        return http_proxy_list


if __name__ == '__main__':
    proxy_manage = ProxyManager()
    proxy_manage.fetch()