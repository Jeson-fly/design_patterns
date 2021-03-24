#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/24 1:15
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 责任链模式（请假方式）
"""
from abc import ABCMeta, abstractmethod


# 抽象处理者（Handler）
class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, days):
        """"""


# 具体处理者（ConcreteHandler）
class GeneralManger(Handler):
    def handle_leave(self, days):
        if days < 20:
            print("准假")
        else:
            print("你还是离职吧")


class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManger()

    def handle_leave(self, days):
        if days < 10:
            print("准假")
        else:
            print("主管职权不足")
            self.next.handle_leave(days)


class ProjectManager(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, days):
        if days < 5:
            print("准假")
        else:
            print("项目经理职权不足")
            self.next.handle_leave(days)


# 客户端
day = 20
h = ProjectManager()
h.handle_leave(day)
