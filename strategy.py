#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/24 0:43
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 策略模型
"""
from abc import ABCMeta, abstractmethod


# 抽象策略（接口）
class Strategy(metaclass=ABCMeta):
    def execute(self, data):
        """"""


# 具体策略
class FastStrategy(Strategy):
    def execute(self, data):
        print("用较快的策略处理%s" % data)


class SlowStrategy(Strategy):
    def execute(self, data):
        print("用较慢的方式执行%s" % data)


# 上下文Context
class Context:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


# 客户端
data = "xxxxx"
strategy = FastStrategy()
c = Context(strategy, data)
c.do_strategy()

strategy = SlowStrategy()
c.set_strategy(strategy)
c.do_strategy()

# 优点：
# 1.提供了相同行为的不同实现
# 2.消除可一些条件语句
# 3.定义了一系列科重用的算法或行为
#
# 缺点：
# 高层代码人员了解不同策略的长处
