"""
    练习1：不改变插入函数与删除函数代码，为其增加验证权限的功能
    def verify_permissions(func):
    print("验证权限")

    def insert():
        print("插入")
    def delete():
        print("删除")

    insert()
    delete()
"""


def verify_permissions(func):
    def wrapper():
        print("验证权限")
        func()
    return wrapper

def insert():
    print("插入")

@verify_permissions # delete = verify_permissions(delete)
def delete():
    print("删除")

# insert = verify_permissions + insert
insert = verify_permissions(insert)

insert()
delete()