"""
    练习2：
    需求：
        定义函数，在员工列表中查找编号是1003的员工
        定义函数，在员工列表中查找姓名是孙悟空的员工
    步骤：
        1. 根据需求，写出函数。
        2. 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数find_single
        3. 在当前模块中调用
"""
from common.iterator_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money


# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

""" 
def find_single01():
    for item in list_employees:
        if item.eid == 1009:
            return item


def find_single02():
    for item in list_employees:
        if item.name == "孙悟空":
            return item


def condition01(item):
    return item.name == "孙悟空"


def condition02(item):
    return item.money == 60000


def find_single(func_condition):
    for item in list_employees:
        # if item.name == "孙悟空":
        # if condition01(item):
        if func_condition(item):
            return item


re = find_single(condition02)
print(re.__dict__)
"""


def condition02(item):
    return item.money == 60000


re = IterableHelper.find_single(list_employees, condition02)
print(re.__dict__)


