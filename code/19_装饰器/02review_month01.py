"""
    Python核心总复习(2)
        四、语句
            1.真值表达式:判断数据是否具有值
            2.条件表达式:有选择性的为变量赋值
            3. while: 根据条件循环
            4. for :根据次数循环
                  for i in range(10):#0~9
                  for i in range(9,-1,-1): # 9~0
            5. 跳转语句
                break : 跳出循环
                continue：跳过循环
        五、容器
            字符串：存储字符编码,不可变,序列
            列表：存储变量,可变,序列
            元组：存储变量,不可变,序列
            字典：存储键值对,可变,散列
            集合：存储键,可变,散列
            不可变(本质)：为了不"损人利己",所以创建数据后不能改变
            可变(方便)：预留空间 + 自动扩容
            序列：有顺序(索引/切片),内存连续(省地)
            散列：无顺序(键),分散存储(占地)

"""
# 真值表达式:判断数据是否具有值
if []:
    print("ok")  # 不执行

if [1]:
    print("ok")  # 执行

# 条件表达式:有选择性的为变量赋值
data = 1 if 1 == "1" else 2
print(data)  # 2

# 基础操作
# 1. 创建
list01 = [10, 20, 30]
dict01 = {"a": "A", "b": "B"}
list02 = list(dict01.items())
print(list02)
# 要求：转换为字典时的数据格式必须能够一分为二
dict02 = dict(list02)
print(dict02)
# 2. 添加
list01.append(30)
list01.insert(0, 40)
dict02["c"] = "C"
# 3. 定位
print(list01[0])
# 通过切片读取数据,会创建新容器
print(list01[:3])
# 通过切片修改数据,遍历右侧可迭代对象,依次存入左侧.
list01[-2:] = ["a", "b"]

dict01["a"] = "AA"
# 4. 删除
# 内部会遍历列表元素
list01.remove(10)
# 直接删除定位的元素(快)
del list01[-1]

# 5. 遍历
for item in list01:
    print(item)

for i in range(len(list01) - 1, -1, -1):
    print(list01[i])

for i, item in enumerate(list01):
    print(i, item)

for key in dict01:
    print(key)

for value in dict01.values():
    print(value)

for key, vlaue in dict01.items():
    print(key, value)
