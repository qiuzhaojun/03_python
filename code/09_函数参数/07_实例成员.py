"""
    实例成员
        实例变量：对象的数据
            每个对象存储一份
        实例方法：对象的行为
"""
# 面向过程
name = "建宁"
age = 26


def print_self():
    print("我叫:", name, "今年", age, "岁了")


print_self()


# 面向对象
# 写法1:
class Wife:
    def __init__(self, name="", age=0):
        # 创建实例变量
        self.name = name
        self.age = age

    # 实例方法：操作实例变量
    def print_self(self):
        print("我叫:", self.name, "今年", self.age, "岁了")


jn = Wife("建宁")
# 读取实例变量
print(jn.name)

# 该变量存储的是对象所有数据成员
# 　{'name': '建宁'}
print(jn.__dict__)
# jn.__dict__["name"] = "建宁公主"
jn.name = "建宁公主"
print(jn.name)

# 写法2: 不建议(应该在类内创建实例变量)
"""
class Wife:
    pass


jn = Wife()
# 创建实例变量
jn.name = "建宁"
# 读取实例变量
print(jn.name)
"""

# 写法3:不建议(应该在构造函数中创建)
"""
class Wife:
    def set_name(self, name):
        self.name = name

jn = Wife()
jn.set_name("建宁")
# 读取实例变量
print(jn.name)
"""

ak = Wife("阿柯", 25)
ak.print_self()  # print_self(ak)
# 如果通过类名调用实例方法,必须手动传递对象地址
Wife.print_self(ak)
