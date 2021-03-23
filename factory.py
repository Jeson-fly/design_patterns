# -*- coding: utf-8 -*-
"""
@Time : 2021/3/23  21:40
@Author : lining
@email：lining01@tuyooganme.com
@desc: 工厂方法模式
"""
from abc import ABCMeta, abstractmethod


# 抽象产品（接口）
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        """"""


# 具体产品
class AliaPayment(Payment):
    def pay(self, money):
        print("支付宝支付%s元" % money)


class WechatPayment(Payment):
    def pay(self, money):
        print("微信支付%s元" % money)


class HuabaiPayment(Payment):
    def pay(self, money):
        print("花呗支付%s元" % money)


# 抽象工厂（接口）
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        """"""


# 具体工厂
class AliaFactory(PaymentFactory):
    def create_payment(self):
        return AliaPayment()


class WechatFactory(PaymentFactory):
    def create_payment(self):
        return WechatPayment()


class HuabaiFactory(PaymentFactory):
    def create_payment(self):
        return HuabaiPayment()


# 客户端

a = HuabaiFactory().create_payment()
a.pay(100)
