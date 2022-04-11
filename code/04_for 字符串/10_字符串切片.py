"""
    切片
        定位多个元素



        range(开始,结束,间隔)
"""
message = "我是花果山水帘洞齐天大圣孙悟空"
# range(1,5,1)# 1 2 3 4
# 写法1:容器名[开始:结束:间隔]
# 备注：不包含结束索引位置的元素
print(message[1:5:1])  # 是花果山
# range(1,5)# 1 2 3 4
# 写法2:容器名[开始:结束]
# 备注：间隔默认为1
print(message[1:5])  # 是花果山
# range(5)# 0 1 2 3 4
# 写法3:容器名[:结束]
# 备注：开始默认为头
print(message[:5])  # 我是花果山
# 写法4:容器名[:]
# 备注：结束默认为尾
print(message[:])  # 我是花果山水帘洞齐天大圣孙悟空
print(message[2:])  # 花果山水帘洞齐天大圣孙悟空

# 案例
message = "我是花果山水帘洞齐天大圣孙悟空"
print(message[2:5])  # 花果山
print(message[1:-3])  # 是花果山水帘洞齐天大圣

print(message[1:-3:-1])  # 空
print(message[6:2:-1])  # 帘水山果

# 果山水帘洞齐天大圣
print(message[3: -3])
# 水帘洞
print(message[5: 8])

# 注意：切片不会越界
print(message[1: 100])  # 是花果山水帘洞齐天大圣孙悟空
# 注意：特殊写法 反转
print(message[::-1])# 空悟孙圣大天齐洞帘水山果花是我
