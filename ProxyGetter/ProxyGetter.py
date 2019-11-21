import time
import random

import requests
import json
from lxml import etree
from Utils.fake_header import headers
class ProxyGetter:

    @staticmethod
    def freeProxy01(self):
        pass
    # 快代理
    @staticmethod
    def freeProxy02():
        url = 'https://www.kuaidaili.com/free/inha/{}'
        for i in range(1,5):
            html = requests.get(url.format(i),headers=headers)
            time.sleep(random.random() + 1 ** 2)
            selector = etree.HTML(html.text)
            ip_list = selector.xpath("//tbody//tr/td[1]/text()")
            port_list = selector.xpath("//tbody//tr/td[2]/text()")
            proxy_type_list = selector.xpath("//tbody//tr/td[4]/text()")
            for index, ip in enumerate(ip_list):
                # print(url.format(i))
                # ('117.69.51.224', '9999', 'HTTP')
                yield ip,port_list[index],proxy_type_list[index]

        # time.sleep(random.random()+1**2)
        # pass
    # 西刺代理
    @staticmethod
    def freeProxy03():
        pass
    @staticmethod
    def freeProxy04():
        pass
    @staticmethod
    def freeProxy05():
        pass
    @staticmethod
    def freeProxy06():
        pass
    @staticmethod
    def freeProxy07():
        pass
    @staticmethod
    def freeProxy08():
        pass


if __name__ == '__main__':
    # print(random.random()+1**2)
    # print( 'https://www.kuaidaili.com/free/inha/{}'.format(1))
    # try:
    getter_obj = ProxyGetter()
    res = getter_obj.freeProxy02()
    for ind,i in enumerate(res):
        print(ind+1,i)

    # # except Exception:
    #     if True:
    #         url = 'https://www.kuaidaili.com/free/inha/{}'
    #         print(url)
    #         response = requests.get(url=url.format(1),headers=headers)
    #         print(response.status_code)
    # def t():
    #     for i in range(5):
    #         for j in range(5):
    #             yield j
    # for ind ,i in enumerate(t()):
    #     print(ind,i)
