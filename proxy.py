# -*- coding: utf-8 -*-
"""
@Time : 2021/3/24  21:53
@Author : lining
@email：lining01@tuyooganme.com
@desc: 代理模式（结构型）
"""
from abc import ABCMeta, abstractmethod

"""
内容：
    为其他对象提供一种代理，以控制这个对象的访问。
应用场景：
    远程代理：为远程对象提供代理；可以隐藏对象位于远程空间的事实
    虚代理：根据需要创建很大的对象；可以进行优化，例如根据要求创建对象。
    保护代理：控制对原始对象的访问，用于对象不同访问权限时。允许在创建一个对象时有一些附加内务处理
角色：
    抽象实体（Subject）
    实体（RealSubject）
    代理（Proxy）
"""


# 抽象实体
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        """"""

    @abstractmethod
    def set_content(self, content):
        """"""


# 实体
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        with open(filename, "r") as f:
            self.content = f.read()

    def get_content(self):
        return self.content

    def set_content(self, content):
        with open(self.filename, "w") as f:
            f.write(content)


# 代理（虚代理）
class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        self.subj.set_content(content)


# 代理（保护代理）
class ProtectedSubject(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError("没有权限")
