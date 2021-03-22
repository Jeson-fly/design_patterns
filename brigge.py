# -*- coding: utf-8 -*-
"""
@Time : 2021/3/4 12:44 下午
@Author : lining
@emial：lining01@tuyooganme.com
@desc: 乔模式
"""

from abc import ABCMeta, abstractmethod


# -----接口-----
class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        """"""


class Color(metaclass=ABCMeta):
    @abstractmethod
    def print(self, shape):
        """"""
