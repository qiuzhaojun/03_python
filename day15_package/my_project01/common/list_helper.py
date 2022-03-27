class ListHelper:
    @classmethod
    def func03(cls):
        print("ListHelper类的func03方法执行了")


import sys

# 列表中存储的是导入模块搜索的顺序
# 主模块所在文件夹,就是根目录.
# sys.path列表第一个是根目录
print(sys.path)
