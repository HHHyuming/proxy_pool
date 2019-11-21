import json


class Proxy:

    def __init__(self, proxy, fail_count=0, proxy_type="", check_count=0, last_status="", last_time="", source=''):
        self.proxy = proxy
        self.fail_count = fail_count
        self.type = proxy_type
        self.check_count = check_count
        self.last_status = last_status
        self.last_time = last_time
        self.source = source

    @property
    def info_dic(self):
        return {"proxy": self.proxy,
                "fail_count": self.fail_count,
                "type": self.type,
                "check_count": self.check_count,
                "last_status": self.last_status,
                "last_time": self.last_time
                }

    @property
    def info_json(self):
        return json.dumps(self.info_dic)
