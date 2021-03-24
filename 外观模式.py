# -*- coding: utf-8 -*-
"""
@Time : 2021/3/24  13:01
@Author : lining
@email：lining01@tuyooganme.com
@desc: 外观模式（结构型）
"""


# 例子电脑开机
# 子系统
class CPU:
    def run(self):
        print("CPU启动")

    def stop(self):
        print(("CPU停止"))


class Disk:
    def run(self):
        print("硬盘启动")

    def stop(self):
        print(("硬盘停止"))


class Memory:
    def run(self):
        print("内存启动")

    def stop(self):
        print("内存停止工作")


# 外观（facade）
class Facade(object):
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


# 客户端
window = Facade()
window.run()
window.stop()
