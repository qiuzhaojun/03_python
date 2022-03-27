"""
    需求：
        定义函数，在员工列表中获取工资最高的员工
        定义函数，在员工列表中获取员工编号最大的员工
    步骤：
        1. 根据需求，写出函数。
        2. 将通用函数放在IterableHelper类中,get_max
        4. 在当前模块中调用
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
def get_max01():
    max_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if max_value.money < list_employees[i].money:
            max_value = list_employees[i]
    return max_value

def get_max02():
    max_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if max_value.eid < list_employees[i].eid:
            max_value = list_employees[i]
    return max_value

def handle01(max_value):
    return max_value.money


def get_max(func_handle):
    max_value = list_employees[0]
    for i in range(1, len(list_employees)):
        # if max_value.money < list_employees[i].money:
        # if handle01(max_value) < handle01(list_employees[i]):
        if func_handle(max_value) < func_handle(list_employees[i]):
            max_value = list_employees[i]
    return max_value

re = get_max( lambda emp: emp.money  )
print(re.__dict__)
re = get_max( lambda emp: emp.eid  )
print(re.__dict__)
"""

re = IterableHelper.get_max(list_employees,lambda emp:emp.money)
print(re.__dict__)