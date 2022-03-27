"""
    主动创造异常
        目的：快速传递错误信息
        语法：
            "发送消息"
                raise Exception(传递的信息)
            "接收消息"
                try:

                except Exception as 变量:
                    变量.args
"""


class Wife:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 25 <= value <= 35:
            self.__age = value
        else:
            # 人为制造异常：快速传递错误信息的技术
            raise Exception("我不要", 1001, "if 25 <= value <= 35")
            # "发送"


# "接收"
while True:
    try:
        age = int(input("请输入年龄："))
        w01 = Wife(age)
        print(w01.age)
        break
    except Exception as e:
        print("年龄超过范围")
        print(e.args)
