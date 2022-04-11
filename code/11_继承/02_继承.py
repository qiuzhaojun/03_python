"""
    继承
        财产：钱,孩子不用挣,但是可以花.
        皇位：江山,太子不用打,但是可以坐.
        编程：代码,子类不用写,但是可以用.
"""


# 多个类有共性,且都属于一个概念,可以创建父类

class Person:
    def say(self):
        print("说话")


class Teacher(Person):

    def teach(self):
        self.say()
        print("教学")


class Student(Person):
    def play(self):
        self.say()
        print("玩耍")


# 创建父类对象
p01 = Person()
# 只能访问父类成员
p01.say()

# 创建子类对象
s01 = Student()
# 能访问父类成员和子类成员
s01.say()
s01.play()

# 关系判定相关函数
# 1. isinstance( 对象 , 类型 )
# 人对象 是一种 人类型
print(isinstance(p01, Person))  # True

# 学生对象 是一种 人类型
print(isinstance(s01, Person))  # True

# 学生对象 是一种 学生类型
print(isinstance(s01, Student))  # True

# 人对象 是一种 学生类型
print(isinstance(p01, Student))  # False

# 2. issubclass( 类型 , 类型 )
# 人类型 是一种 人类型
print(issubclass(Person, Person))  # True

# 学生类型 是一种 人类型
print(issubclass(Student, Person))  # True

# 学生类型 是一种 学生类型
print(issubclass(Student, Student))  # True

# 人类型 是一种 学生类型
print(issubclass(Person, Student))  # False

# 3.  type(对象) == 类型
# 人对象 是 人类型
print(type(p01) == Person)  # True

# 学生对象 是 人类型
print(type(s01) == Person)  # False

# 学生对象 是 学生类型
print(type(s01) == Student)  # True

# 人对象 是 学生类型
print(type(p01) == Student)  # False
