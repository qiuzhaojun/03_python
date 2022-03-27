"""
    day11/homework/exercise02
"""
class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    # Employee类型比较大小的依据：钱
    def __gt__(self, other):
        return self.money > other.money

    # Employee类型比较相同的依据：姓名
    def __eq__(self, other):
        return self.name == other.name

list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

# 使用代码完成下列功能 day11/homework/exercise02
# 1. 找出最有钱的员工
# TypeError: '>' not supported between instances of 'Employee' and 'Employee'
max_emp = max( list_employees  )
print(max_emp.__dict__)

# # 2. 按照工资升序排列
list_employees.sort()
print(list_employees)

# # 3. 判断猪八戒在列表中的索引
target = Employee(1003, 9002, "猪八戒", 20000)
print(list_employees.index(target))
