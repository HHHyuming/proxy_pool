import time
import random

import requests
import json
from lxml import etree
from Utils.fake_header import headers
class ProxyGetter:

    @staticmethod
    def freeProxy01():
        url = "http://www.kxdaili.com/dailiip/1/{}.html"
        for page in range(1,5):
            request_url = url.format(page)
            response = requests.get(request_url,headers=headers)
            if response and response.status_code != 200:
                continue
            html = response.text
            selector = etree.HTML(html)
            ip_list = selector.xpath("//table[@class='active']//tr/td[1]/text()")
            port_list = selector.xpath("//table[@class='active']//tr/td[2]/text()")
            proxy_type_list = selector.xpath("//table[@class='active']//tr/td[4]/text()")
            time.sleep(random.random() + 1 ** 2)
            for index, ip in enumerate(ip_list):
                # print(url.format(i))
                # ('117.69.51.224', '9999', 'HTTP')
                proxy = ip+':'+port_list[index]
                yield proxy,port_list[index],proxy_type_list[index]
    # 快代理
    @staticmethod
    def freeProxy02():
        url = 'https://www.kuaidaili.com/free/inha/{}'
        for i in range(1,5):
            response = requests.get(url.format(i),headers=headers)
            if response and response.status_code != 200:
                continue

            time.sleep(random.random() + 1 ** 2)
            selector = etree.HTML(response.text)
            ip_list = selector.xpath("//tbody//tr/td[1]/text()")
            port_list = selector.xpath("//tbody//tr/td[2]/text()")
            proxy_type_list = selector.xpath("//tbody//tr/td[4]/text()")
            for index, ip in enumerate(ip_list):
                # print(url.format(i))
                # ('117.69.51.224', '9999', 'HTTP')
                proxy = ip+':'+port_list[index]
                yield proxy,port_list[index],proxy_type_list[index]

        # time.sleep(random.random()+1**2)
        # pass
    # 西刺代理
    @staticmethod
    def freeProxy03():
        "https://www.xicidaili.com/nn/5"
        url = 'https://www.xicidaili.com/nn/{}'
        for i in range(1,5):
            response = requests.get(url.format(i),headers=headers)
            if response and response.status_code != 200:
                print(111)
                continue

            time.sleep(random.random() + 1 ** 2)
            print(response.text)
            selector = etree.HTML(response.text)
            ip_list = selector.xpath("//tbody//tr/td[2]/text()")
            port_list = selector.xpath("//tbody//tr/td[3]/text()")
            proxy_type_list = selector.xpath("//tbody//tr/td[6]/text()")
            for index, ip in enumerate(ip_list):
                # print(url.format(i))
                # ('117.69.51.224', '9999', 'HTTP')
                proxy = ip+':'+port_list[index]
                yield proxy,port_list[index],proxy_type_list[index]
    @staticmethod
    def freeProxy04():
        """
        guobanjia http://www.goubanjia.com/
        :return:
        """
        url = "http://www.goubanjia.com/"
        response = requests.get(url,headers=headers)
        proxy_list = etree.HTML(response.text).xpath('//td[@class="ip"]')
        # 此网站有隐藏的数字干扰，或抓取到多余的数字或.符号
        # 需要过滤掉<p style="display:none;">的内容
        xpath_str = """.//*[not(contains(@style, 'display: none'))
                                        and not(contains(@style, 'display:none'))
                                        and not(contains(@class, 'port'))
                                        ]/text()
                                """
        proxy_type_list = etree.HTML(response.text).xpath("//tbody//tr//td[3]//text()")
        for index, each_proxy in enumerate(proxy_list):
            try:
                # :符号裸放在td下，其他放在div span p中，先分割找出ip，再找port
                ip_addr = ''.join(each_proxy.xpath(xpath_str))

                # HTML中的port是随机数，真正的端口编码在class后面的字母中。
                # 比如这个：
                # <span class="port CFACE">9054</span>
                # CFACE解码后对应的是3128。
                port = 0
                for _ in each_proxy.xpath(".//span[contains(@class, 'port')]"
                                          "/attribute::class")[0]. \
                        replace("port ", ""):
                    port *= 10
                    port += (ord(_) - ord('A'))
                port /= 8

                # yield '{}:{}'.format(ip_addr, int(port))
                yield ip_addr, port,proxy_type_list[index]
            except Exception as e:
                print(e)
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
    @staticmethod
    def freeProxy09():
        pass


if __name__ == '__main__':
    # print(random.random()+1**2)
    # print( 'https://www.kuaidaili.com/free/inha/{}'.format(1))
    # try:
    getter_obj = ProxyGetter()
    res = getter_obj.freeProxy03()
    for index,i in enumerate(res):
        print(index+1,i)

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
