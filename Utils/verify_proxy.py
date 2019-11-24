import requests
from datetime import datetime
from Utils.fake_header import headers
def validation(proxy_obj,db):
    proxy = {
        proxy_obj.proxy_type: proxy_obj.proxy
    }
    try:
        response = requests.get('http://www.baidu.com/',proxies=proxy, headers=headers, timeout=10)
    except Exception as e:
        print(e)
        response =None
    if response and response.status_code != 200:
        proxy_obj.fail_count += 1
        return False
    proxy_obj.fail_count -= 1
    proxy_obj.check_count += 1
    proxy_obj.last_time = datetime.now().strftime('%Y-%m-%d %X')
    db.put(proxy_obj)
