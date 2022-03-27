"""
    需求：
        定义函数，在员工列表中查找所有员工的姓名
        定义函数，在员工列表中查找所有员工的编号与薪资
    步骤：
        1. 根据需求，写出函数。
        2. 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数 select
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
def select01():
    for item in list_employees:
        yield item.name


def select02():
    for item in list_employees:
        yield (item.eid, item.money)


for item in select02():
    print(item)


def handle01(item):
    return item.name


def select(func_handle):
    for item in list_employees:
        # yield item.name
        # yield handle01(item)
        yield func_handle(item)


# for item in select( handle01  ):
for name in select(lambda item: item.name):
    print(name)
"""

for name in IterableHelper.select(list_employees, lambda emp: emp.name):
    print(name)

for name in IterableHelper.select(list_employees, lambda emp: (emp.eid, emp.money)):
    print(name)
