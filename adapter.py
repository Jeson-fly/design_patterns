# -*- coding: utf-8 -*-
"""
@Time : 2021/3/4 12:31 下午
@Author : lining
@emial：lining01@tuyooganme.com
@desc: 适配器模式
"""

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        """"""


class AliaPay(Payment):
    def pay(self, money):
        return "支付宝支付1000"


class WechatPay(Payment):
    def pay(self, money):
        return "微信支付1000元"


class BankPay:
    def cost(self, money):
        print("银联支付1000元")


# # 类适配器
# class NewBankPay(Payment, BankPay):
#     def pay(self, money):
#         self.cost(money)


# 对象适配器
class Adapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


adapter = Adapter(BankPay())
res = adapter.pay(100)
print(res)