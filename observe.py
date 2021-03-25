#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/24 0:11
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 观察者模式（发布订阅模式） 行为行模式
"""
# 定义对象之间的一种或多种的以来关系，当一个对象的状态发生改变时，所有以来于它的对象都得到通
# 知并被自动更新，观察者模式又被称为发布-订阅模式
from abc import ABCMeta, abstractmethod


# 抽象主题（Subject）
class Notice:
    def __init__(self):
        self.observer = []

    def attach(self, observer):
        self.observer.append(observer)

    def detach(self, observer):
        self.observer.remove(observer)

    def notify(self):
        for obs in self.observer:
            obs.update(self)


# 具体主题（ConcreteSubject）---发布者
class StaffNotice(Notice):
    def __init__(self, comp_info):
        super().__init__()
        self.__comp_info = comp_info

    # 负责读
    @property
    def comp_info(self):
        return self.__comp_info

    # 负责写
    @comp_info.setter
    def comp_info(self, info):
        self.__comp_info = info
        self.notify()


# 抽象观察者（Observer）
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):
        """"""


# 具体观察者（ConcreteObserver）---订阅者
class Staff(Observer):
    def __init__(self):
        self.comp_info = None

    def update(self, notice):
        self.comp_info = notice.comp_info


# 客户端
if __name__ == '__main__':
    notice = StaffNotice("初始化公司信息")
    s1 = Staff()
    s2 = Staff()
    notice.attach(s1)
    notice.attach(s2)
    notice.comp_info = "今年业绩不错"
    print(s1.comp_info)
    notice.detach(s2)
    notice.comp_info = "公司倒闭了"
    print(s1.comp_info)
