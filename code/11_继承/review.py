"""
    复习 - 面向对象
    1. 字面意思：考虑问题从对象的角度出发.
                 谁？    干么？
    2. 类与对象关系：
        现实事物  -抽象-> 类 -具体-> 对象
    3. 语法
        创建类
            class 类名:
                def __init__(slef,参数):
                    self.数据 = 参数

                def 方法名(self):
                    方法体

        创建对象
            对象名 = 类名(构造函数的实际参数)

        实例成员:通过对象点
            class 类名:
                def __init__(slef,参数):
                    self.实例变量 = 参数

                def 方法名1(self):
                    self.实例变量

                def 方法名2(self):
                    self.方法名1()

            对象名 = 类名(构造函数的实际参数)
            对象名.方法名1() # 方法名1(对象名)
            对象名.实例变量

        类成员:通过类点
            class 类名:
                 变量名 = 数据

                @classmethod
                def 方法名1(cls):
                     类名.变量名
                     cls.变量名

                @classmethod
                def 方法名2(cls):
                    cls.方法名1()

            类名.变量名
            类名.方法名1() # 方法名1(类名)
            类名.方法名2()

    4. 封装
        数据角度：多个变量 合并为 一个类型
           cid,name,price...  Commodity

        行为角度：隐藏实现细节
        属性：保护私有变量
            class 类名：
                def __init__(self,参数):
                    self.数据 = 参数

            @property
            def 数据(self):
                return self.__数据

            @数据.setter
            def 数据(self,value):
                self.__数据 = value

            对象名 = 类名(构造函数的实参)
            对象名.数据 = 意外值
"""