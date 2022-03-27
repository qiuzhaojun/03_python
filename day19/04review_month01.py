"""
    面向对象-语法总复习
        1. 类和对象
            class 类名:
                def __init__(self,参数):
                    self.数据 = 参数

                def 方法名(self):
                    方法体

            对象名 = 类名(参数)
            对象名.数据
            对象名.方法名()
            注意：
                类名命名规范：所有单词首字母大写,不要使用下划线隔开.
                变量名方法名命名规范：所有单词字母小写,使用下划线隔开.
        2.  实例成员：自己的
            类成员：大家的
            静态方法:工具的
            class 类名:
                类变量 = 数据
                def __init__(self,参数):
                    self.实例变量 = 参数

                #             为了自动传递对象
                def 实例方法名(self):
                    方法体

                @classmethod # 为了自动传递类
                def 类方法名(cls):
                    方法体

                @staticmethod # 为了不自动传递信息
                def 类方法名():
                    方法体

            对象 = 类名()
            对象.实例变量
            对象.实例方法()
            类名.类变量
            类名.类方法
            类名.静态方法

        3. 属性(内置装饰器):保护数据
            class 类名:
                def __init__(self,参数):
                    self.data = 参数

            @property #  data = property( data  )
            def data(self):
                return self.__data

            @data.setter # data = data.setter(data)
            def data(self,value):
                self.__data = value

            对象 = 类名()
            对象.data = ?
            ? = 对象.data
        4. MVC
            了解软件整体结构
                数据模型  界面逻辑  核心算法
                  数据类   输入       业务
                          输出       数据计算方法
"""


class XXView:
    def __init__(self):
        self.__controller = XXController()

    def func01(self):
        print("func01")
        self.__controller.func02()

class XXController:
    def func02(self):
        print("func02")

view = XXView()
view.func01()
