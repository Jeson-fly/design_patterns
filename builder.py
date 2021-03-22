# -*- coding: utf-8 -*-
"""
@Time : 2021/3/3 12:24 下午
@Author : lining
@emial：lining01@tuyooganme.com
@desc: 建造者模式
"""

from abc import ABCMeta, abstractmethod


class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s,%s,%s,%s" % (self.face, self.body, self.arm, self.leg)


class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        """"""

    @abstractmethod
    def build_body(self):
        """"""

    @abstractmethod
    def build_arm(self):
        """"""

    @abstractmethod
    def build_leg(self):
        """"""


class SexGrilBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "漂亮的脸蛋"

    def build_body(self):
        self.player.body = "苗条的身材"

    def build_arm(self):
        self.player.arm = "xxxxx"

    def build_leg(self):
        self.player.leg = "大长腿"


class Monster(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "怪物量"

    def build_body(self):
        self.player.body = "怪物身材"

    def build_arm(self):
        self.player.arm = "张茆"

    def build_leg(self):
        self.player.leg = "张茆的腿"


class PlayerDirect:
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


print(bin(3).count("1"))
