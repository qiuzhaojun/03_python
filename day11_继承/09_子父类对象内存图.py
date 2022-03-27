"""
    创建父类：车(品牌，速度)
    创建子类：电动车(电池容量,充电功率)
    创建子类对象并画出内存图。
"""


class Car:
    def __init__(self, bread="", speed=0):
        self.bread = bread
        self.speed = speed


class ElectricCars(Car):
    def __init__(self, bread, speed, battery_capacity, charging_power=100):
        super().__init__(bread, speed)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power


tsl = ElectricCars("特斯拉", 300, 30000, 1000)
print(tsl.bread)
print(tsl.speed)
print(tsl.battery_capacity)
print(tsl.charging_power)
