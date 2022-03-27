"""
    字符串字面值
"""

# 1.双引号
name01 = "孙悟空"
# 2.单引号
name02 = '孙悟空'

# 3.三引号:可见即所得
name03 = '''
孙
   悟
空'''
print(name03)
name03 = """孙悟空 """

# 4.
message01 = '我是"孙悟空"。'
message02 = "我是'孙悟空'。"
message03 = '''我是'孙'悟"空"。'''

# 5. 转义字符:改变原始含义的特殊字符
# \"   \\    r""    换行\n  ...
message04 = "我是\"孙悟空\"。"

url = r"C:\arogram Files\breative\nhareDLL"
url = "C:\\arogram Files\\breative\\nhareDLL"

message05 = "我是\n孙悟空。"
print(message05)

# 6. 格式化字符串
# 您输入的主语是:I,谓语是:kiss,宾语是:you
subject = "I"
predicate = "kiss"
object = "you"
# 字符串拼接：需要在固定的格式中插入的变量多,那么代码可读性差
print("您输入的主语是:" + subject + ",谓语是:" + predicate + ",宾语是:" + object)
# 占位符
print("您输入的主语是:%s,谓语是:%s,宾语是:%s" % (subject, predicate, object))

name = "张三"
age = 8
score = 95.128
print("我是%s,今年%.2d岁了,考了%.2f分." %
      (name, age, score))
