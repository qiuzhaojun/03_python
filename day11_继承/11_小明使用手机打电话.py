"""
    需求：小明使用手机打电话
    识别对象：
            人类        手机
    分配职责：
            打电话      通话
    建立交互：
           人类  调用  手机
"""

class Person:
    def __init__(self, name=""):
        self.name = name

    def call(self, communication):
        print(self.name, "打电话")
        communication.dialing()

class MobilePhone:
    def dialing(self):
        print("呼叫")

xm = Person("小明")
xm.call(MobilePhone())
