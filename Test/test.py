from DB import DBClient
from DB import RedisClient
from ProxyHelper import Proxy
from datetime import datetime
if __name__ == '__main__':
    # proxy = proxy
    # fail_count = fail_count
    # type = proxy_type
    # check_count = check_count
    # last_status = last_status
    # last_time = last_time
    proxy_obj = Proxy.Proxy(proxy='127.0.0.1',fail_count=0, proxy_type='http',check_count=0,last_status='', last_time=datetime.now())
    print(proxy_obj)
    # print(__import__(r'../DB/RedisClient'))
    db = DBClient.DbClient()
    db.get('127.0.0.1')