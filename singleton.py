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
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyTest(Singleton):
    def __init__(self, a):
        self.a = a


class Fields(Singleton):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Fields, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.apply_map = "apply_map"
        self.friends_map = "friends_map"
        self.wait_agree_map = "wait_agree_map"
        self.black_map = "black_map"


if __name__ == '__main__':
    f1 = Fields()
    print(id(f1))
    print(f1.black_map)
    f2 = Fields()
    print(id(f2))
    print(id(f1))
    from collections import namedtuple

    Fields = namedtuple("Fields", ["apply_name", "mm"], defaults=["apply_name", "mm"])
    u = Fields()
    print(u.apply_name)
    print(u.mm)
    # field_names = list(map(str, [1, 2, 3, 4, "sss"]))
    # print(field_names)
