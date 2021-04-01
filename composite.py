#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2021/4/2 0:04
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 组合模型
"""

from abc import ABCMeta, abstractmethod


class Graphic(metaclass=ABCMeta):
    def draw(self):
        pass


class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "点(%s，%s)" % (self.x, self.y)

    def draw(self):
        print(self)


class Line(Graphic):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        return "线段[%s，%s]" % (self.point1, self.point2)

    def draw(self):
        print(self)


class Picture(Graphic):
    def __init__(self, iterable=[]):
        self.children = []
        for item in iterable:
            self.children.append(item)

    def add(self,graphic):
        self.children.append(graphic)

    def draw(self):
        print("---复合图形---")
        for graphic in self.children:
            graphic.draw()
        print("---复合图形---")

# 客户端
point1 = Point(1, 2)
point2 = Point(2, 3)
print(point1)
line1 = Line(point1, point2)
line2 =Line(Point(3,4),Point(5,5))
print(line1)

p = Picture([line1,point2])
p.add(point2)
p.add(line2)
p.draw()


p2 =Picture()
p2.add(p)
p2.draw()