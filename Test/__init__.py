# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__
   Description :
   Author :        JHao
   date：          2019/2/15
-------------------------------------------------
   Change Activity:
                   2019/2/15:
-------------------------------------------------
"""
__author__ = 'JHao'
# def tcpConnect(proxy):
#     """
#     TCP 三次握手
#     :param proxy:
#     :return:
#     """
#     from socket import socket, AF_INET, SOCK_STREAM
#     s = socket(AF_INET, SOCK_STREAM)
#     ip, port = proxy.split(':')
#     result = s.connect_ex((ip, int(port)))
#     print(result)
#     return True if result == 0 else False
#
# res = tcpConnect('39.106.217.14:8002')
# print(res)
import inspect
class GetFreeProxy:
    def a(self):
        pass
    @property
    def b(self):
        return 1

# member_list = inspect.getmembers(GetFreeProxy, predicate=inspect.isfunction)
# print(member_list)
from six import iteritems
dic = {'a':1,'b':2}
for key, v in iteritems(dic):
    print(key,v)