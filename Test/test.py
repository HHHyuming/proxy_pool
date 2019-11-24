from DB import DBClient
from DB import RedisClient
from ProxyHelper import Proxy
from datetime import datetime
if __name__ == '__main__1':
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

if __name__ == '__main__':
    from apscheduler.schedulers.blocking import BlockingScheduler


    def job1():
        print("job 1")
    def job2(name):
        print("hello %s" % name)
    schedule = BlockingScheduler()

    # 每秒执行一次 有参数
    # schedule.add_job(func=job2, args=('lierl',), trigger='interval', seconds=1)
    # 每秒执行一次 无参数
    # schedule.add_job(func=job1, trigger='interval', seconds=1)
    # schedule.start()  # 启动定时器
    # print("start end")
    print(None['aa'])