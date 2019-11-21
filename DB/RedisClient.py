import json

from redis import Redis, BlockingConnectionPool,ConnectionPool


class RedisClient(object):

    def __init__(self, name, **kwargs):
        self.name = name
        self.__conn = Redis(**kwargs)

    def get(self, key, **kwargs):

        return json.loads(self.__conn.hget(self.name, key).decode())

    def put(self, proxy_obj):
        self.__conn.hset(self.name, proxy_obj.proxy, proxy_obj.info_json)
        return proxy_obj.info_dic

    def delete(self, key, **kwargs):
        self.__conn.hdel(self.name, key)

    def getAll(self):
        dic_data = self.__conn.hgetall(self.name)
        new_dic = {}
        for k, v in dic_data.items():
            new_dic[k.decode()] = json.loads(v.decode())
        return new_dic

    def getNumber(self):
        self.__conn.hlen(self.name)

    def exists(self, key, **kwargs):
        return self.__conn.exists(self.name, key)

    def pop(self, **kwargs):
        return

    def clear(self):
        self.__conn.delete(self.name)

    def changeTable(self, name):
        self.name = name

    def hset(self, key, value):
        self.__conn.hset(self.name, key, value)

if __name__ == '__main__':
    client = RedisClient('proxy')
    client.hset('127.0.0.1',1)
