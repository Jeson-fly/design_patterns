# -*- coding: utf-8 -*-
"""
@Time : 2021/3/4 12:44 下午
@Author : lining
@emial：lining01@tuyooganme.com
@desc: 乔模式
"""

from abc import ABCMeta, abstractmethod


# 抽象类
class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        """"""


# 具体类
class Color(metaclass=ABCMeta):
    @abstractmethod
    def print(self, shape):
        """"""


# 具体实现类
class Red(Color):
    def print(self, shape):
        print("红色的%s" % shape.name)


# 具体实现类
class Blue(Color):
    def print(self, shape):
        print("蓝色的%s" % shape.name)


# 细化抽象类
class Line(Shape):
    name = "直线"

    def draw(self):
        return self.color.print(self)


# 细化抽象类
class Circle(Shape):
    name = "圆形"

    def draw(self):
        return self.color.print(self)


# 客户端
t = Line(Red())
t = Circle(Blue())
d = t.draw()
