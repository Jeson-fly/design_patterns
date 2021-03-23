# -*- coding: utf-8 -*-
"""
@Time : 2021/3/3 9:41 上午
@Author : lining
@emial：lining01@tuyooganme.com
@desc: 简单工厂模式
"""
from abc import ABCMeta, abstractmethod


# 接口
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        """"""


class AliPay(Payment):
    def pay(self, money):
        print("支付宝支付：%s元" % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付：%s元" % money)


class PayFactory(metaclass=ABCMeta):
    @abstractmethod
    def creat_payment(self):
        """"""


class AliFactory(PayFactory):
    def creat_payment(self):
        return AliPay()


class WechatFactory(PayFactory):
    def creat_payment(self):
        return WechatPay()


# 客户端
p = AliFactory()
t = p.creat_payment()
t.pay(100)
