"""
调度器，负责替换raw表中的数据
        负责替换useful表中的数据
        API从useful中拿取
"""
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

from Schedule.RawProxySchedule import do_raw_check
from Schedule.UsefulProxySchedule import do_useful_check
from Manager.ProxyManager import ProxyManager

def fet_main():
    ProxyManager().fetch()

def raw_shedule():
    print("raw 被定时器执行")
    fet_main()
    do_raw_check()

def useful_schedule():
    print("useful 被定时器执行")
    do_useful_check()


def run_shedule():
    raw_shedule()
    useful_schedule()

    scheduler = BlockingScheduler()
    scheduler.add_job(raw_shedule, trigger='interval', seconds=5, id="raw_proxy_check", name="raw_proxy定时采集")
    scheduler.add_job(useful_schedule, trigger='interval', minutes=1, id="useful_proxy_check", name="useful_proxy定时检查")

    scheduler.start()
    print("start")
if __name__ == '__main__':
    run_shedule()