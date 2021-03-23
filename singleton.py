# -*- coding: utf-8 -*-
"""
@Time : 2021/3/23  22:04
@Author : lining
@email：lining01@tuyooganme.com
@desc: 单例模式
"""


# 创建单例模式
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__()
        return cls._instance



class MyTest(Singleton):
    def __init__(self,a):
        self.a =a
