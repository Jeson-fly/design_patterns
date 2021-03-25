#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/3/24 1:04
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 模板方法
"""

# 内容：定义一个算法框架

from abc import ABCMeta, abstractmethod
import time


# 窗口（接口）
class Windows(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        """"""

    @abstractmethod
    def repaint(self):
        """"""

    @abstractmethod
    def close(self):
        """"""

    def run(self):
        self.start()
        while True:
            try:
                self.repaint()
                time.sleep(1)
            except KeyboardInterrupt:
                break
        self.close()


class MyWindow(Windows):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("开始")

    def repaint(self):
        print("窗口正在运行")

    def close(self):
        print("程序结束")


# 客户端
msg = "hello"
MyWindow(msg).run()

# 使用场景：
# 一次性实现一个算法不变的部分
# 各个子类中的公共行为应该被提取出来并集中到一个公共父类中以避免代码重复
# 控制子类扩展
