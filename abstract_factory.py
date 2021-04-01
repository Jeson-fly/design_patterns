# -*- coding: utf-8 -*-
"""
@Time : 2021/3/23  22:02
@Author : lining
@email：lining01@tuyooganme.com
@desc: 抽象工厂模式
"""

from abc import ABCMeta, abstractmethod


# 抽象产品
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        """"""


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        """"""


class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        """"""


# 抽象工厂接口
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        """"""

    @abstractmethod
    def make_cpu(self):
        """"""

    @abstractmethod
    def make_os(self):
        """"""


# 具体产品
class SmallShell(PhoneShell):
    def show_shell(self):
        print("小手机壳")


class BigShell(PhoneShell):
    def show_shell(self):
        print("大手机壳")


class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果Cpu")


class MediaTekCPU(CPU):
    def show_cpu(self):
        print("联发科CPU")


class Android(OS):
    def show_os(self):
        print("安卓系统")


class Ios(OS):
    def show_os(self):
        print("ios系统")


# 具体工厂
class MiFactory(PhoneFactory):
    def make_shell(self):
        return BigShell()

    def make_cpu(self):
        return MediaTekCPU()

    def make_os(self):
        return Android()


class HuaWeiFactory(PhoneFactory):
    def make_shell(self):
        return SmallShell()

    def make_cpu(self):
        return MediaTekCPU()

    def make_os(self):
        return Android()


# 客户端
class Phone:
    def __init__(self, shell, cpu, os):
        self.shell = shell
        self.cpu = cpu
        self.os = os

    def show_info(self):
        self.shell.show_shell()
        self.cpu.show_cpu()
        self.os.show_os()


def make_phone(factory):
    shell = factory.make_shell()
    cpu = factory.make_cpu()
    os = factory.make_os()
    return Phone(shell, cpu, os)


factory = MiFactory()
phone = make_phone(factory)
phone.show_info()
