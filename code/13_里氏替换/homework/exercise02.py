"""
    小明使用手机打电话
    要求:增加座机,卫星电话时不影响小明.
    封装[分]：创建人类和手机类
    继承[隔]：使用通信工具类,隔离人类与手机、座机等具体工具的变化
    多态[做]：通过重写实现手机的功能
"""
# 餐厅
# 迎宾 -- 点餐服务员 -- 厨师 -- 配送员
class Communication:
    def dialing(self):
        pass

class Person:
    def __init__(self, name=""):
        self.name = name

    def call(self, communication:Communication):
        print(self.name, "打电话")
        # 1. 编码时  调用父
        # 运行时  执行子
        communication.dialing()

class MobilePhone(Communication):
    # 2. 体现个性(实现变化)
    def dialing(self):
        print("手机呼叫")

class Landline(Communication):
    def dialing(self):
        print("座机呼叫")

xm = Person("小明")
# 3. 创建子对象
xm.call(MobilePhone())
xm.call(Landline())
