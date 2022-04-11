# 因为主模块不会自动生成PYC文件
# 所以主模块代码应该最少
from usl import StudentView

if __name__ == '__main__':
    # 全局异常处理
    view = StudentView()
    view.main()
