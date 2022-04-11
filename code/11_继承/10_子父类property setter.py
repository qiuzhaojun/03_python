"""
        父类：车(品牌，速度)
                     0-280
        创建子类：电动车(电池容量,充电功率)
                      0 - 50000  200 - 250
        -- 通过属性限制数据范围
"""


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0 <= value <= 280:
            self.__speed = value
        else:
            raise Exception("速度超过范围")


class ElectricCars(Car):
    # 1. 子类构造函数参数：父类参数+子类参数
    def __init__(self, brand, speed, battery_capacity, charging_power):
        # 2. 通过super调用父类构造函数
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value):
        if 0 <= value <= 50000:
            self.__battery_capacity = value
        else:
            raise Exception("电池容量超过范围")

    @property
    def charging_power(self):
        return self.__charging_power

    @charging_power.setter
    def charging_power(self, value):
        if 200 <= value <= 250:
            self.__charging_power = value
        else:
            raise Exception("充电功率超过范围")

bc = Car("奔驰", 220)
print(bc)

am = ElectricCars("艾玛", 180, 10000, 220)
print(am)
