"""
    内置高阶函数
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

# 1. 映射
# for item in IterableHelper.select(list_employees,lambda emp:(emp.eid,emp.name)):
#     print(item)

# 生成器 = map(lambda,可迭代对象)
for item in map(lambda emp: (emp.eid, emp.name), list_employees):
    print(item)

# 2. 过滤器
# for emp in IterableHelper.find_all(list_employees,lambda item:item.did == 9002):
#     print(emp.__dict__)

# 生成器 = filter(lambda,可迭代对象)
for emp in filter(lambda item: item.did == 9002, list_employees):
    print(emp.__dict__)

# 3. 获取极值(最大最小) max   min
# re = IterableHelper.get_max(list_employees,lambda element:element.money)
# print(re.__dict__)

# 元素 = max(可迭代对象,key = lambda)
re = max(list_employees, key=lambda element: element.money)
print(re.__dict__)

# 4.
# IterableHelper.order_by(list_employees,lambda item:item.money)
#
# for item in list_employees:
#     print(item.__dict__)

# 升序排列
# 新列表 = sorted(可迭代对象,key = lambda)

# 降序排列(翻转后的升序排列)
# 新列表 = sorted(可迭代对象,key = lambda,reverse=True)
result = sorted(list_employees, key=lambda item: item.money, reverse=True)
for item in result:
    print(item.__dict__)
