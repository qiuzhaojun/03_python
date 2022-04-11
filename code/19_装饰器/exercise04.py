"""
    为上一个练习完善返回值与参数
"""

def verify_permissions(func):
    def wrapper(*args, **kwargs):
        print("验证权限")
        return func(*args, **kwargs)

    return wrapper


@verify_permissions
def insert(id, name, age):
    print("插入", id, name, age)
    return "ok"


@verify_permissions
def delete(id):
    print("删除", id)
    return "no"


print(insert(1001, "悟空", age=26))
print(delete(1002))
