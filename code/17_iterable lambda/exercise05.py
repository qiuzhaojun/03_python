# 练习： 在员工列表中查找编号是1003的员工
#       在员工列表中查找姓名是孙悟空的员工
#       在员工列表中部门编号是9001的所有员工
#       在员工列表中工资小于50000的所有员工
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

# def condition01(item):
#     return item.eid == 1003


re = IterableHelper.find_single(list_employees,
                                lambda item: item.eid == 1003)
print(re.__dict__)

re = IterableHelper.find_single(list_employees, lambda emp: emp.name == "孙悟空")
print(re.__dict__)


for item in IterableHelper.find_all(list_employees,lambda element:element.did == 9001):
    print(item.__dict__)

for item in IterableHelper.find_all(list_employees,lambda element:element.money < 50000):
    print(item.__dict__)
