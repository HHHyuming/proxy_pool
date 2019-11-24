from datetime import datetime
import sys, os
from Config.ConfigGetter import ConfigGetter
from ProxyHelper import Proxy
from Utils.utilClass import Singleton

sys.path.append(os.path.dirname(__file__))

class DbClient(metaclass=Singleton):
    def __init__(self):
        self.client = None
        self.__init_db_client()

    def __init_db_client(self):
        __type = None
        config = ConfigGetter('default')
        if config.db_type == 'ssdb':
            __type = 'SsdbClient'
        if config.db_type == 'redis':
            __type = 'RedisClient'
        print(__type)
        self.client = getattr(__import__(__type), __type)(config.db_hname, host=config.db_host, port=config.db_port)

    def get(self, key, **kwargs):
        return self.client.get(key, **kwargs)

    def put(self, key, **kwargs):
        return self.client.put(key, **kwargs)

    def update(self, key, value, **kwargs):
        return self.client.update(key, value, **kwargs)

    def delete(self, key, **kwargs):
        return self.client.delete(key, **kwargs)

    def exists(self, key, **kwargs):
        return self.client.exists(key, **kwargs)

    def pop(self, **kwargs):
        return self.client.pop(**kwargs)

    def getAll(self):
        return self.client.getAll()

    def clear(self):
        return self.client.clear()

    def changeTable(self, name):
        self.client.changeTable(name)

    def getNumber(self):
        return self.client.getNumber()

    def redis_hset(self, key, value):

        if hasattr(self.client, 'hset'):
            self.client.hset(key, value)






if __name__ == '__main__':
    proxy_obj = Proxy.Proxy(proxy='192.168.1.1',fail_count=0, proxy_type='http',check_count=0,last_status='', last_time=datetime.now().strftime('%Y-%m-%d %X'))
    print(proxy_obj.info_dic)
    #
    db = DbClient()
    #
    # res = db.get('127.0.0.1')
    # db.redis_hset('192.168.1.1',proxy_obj.info_json)
    # print(res,type(res))
    res =db.getAll()
    print(res,type(res))
