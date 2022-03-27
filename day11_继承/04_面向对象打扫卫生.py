"""
    练习1：以面向对象思想,描述下列情景.
        小明请保洁打扫卫生
        理念：找行为不同
"""
"""
写法1：小明每次通知一个新保洁员
class Client:
    def __init__(self, name=""):
        self.name = name

    def notify(self):
        print(self.name,"通知")
        cleaner = Cleaner()
        cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("保洁员打扫卫生")

xm = Client("小明")
xm.notify()
"""

# 写法2：小明请自己的保洁
"""
class Client:
    def __init__(self, name=""):
        self.name = name
        self.cleaner = Cleaner()

    def notify(self):
        print(self.name,"通知")
        self.cleaner.cleaning()

class Cleaner:
    """

"""
def cleaning(self):
    print("保洁员打扫卫生")

xm = Client("小明")
xm.notify()
"""

# 写法3：小明通过保洁服务(保洁员...)打扫卫生
class Client:
    def __init__(self, name=""):
        self.name = name

    def notify(self, service):
        print(self.name, "通知")
        service.cleaning()

class Cleaner:
    """
        保洁员
    """

    def cleaning(self):
        print("保洁员打扫卫生")

xm = Client("小明")
cleaner = Cleaner()
xm.notify(cleaner)
