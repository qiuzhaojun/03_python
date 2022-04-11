# 方式1：
import module_exercise

print(module_exercise.data)

module_exercise.func01()

m01 = module_exercise.MyClass()
m01.func02()

module_exercise.MyClass.func03()

# 方式2：
# from module_exercise import func01
# from module_exercise import data
# from module_exercise import MyClass
from module_exercise import *

print(data)

func01()

m02 = MyClass()
m02.func02()

MyClass.func03()