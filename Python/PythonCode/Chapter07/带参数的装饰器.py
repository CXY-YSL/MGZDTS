# 导入time模块的函数
from time import ctime
# 带有参数的装饰器
def timefun_arg(pre="hello"):
    def timefun(func):
        def wrappedfunc():
            print("%s called at %s %s"%(func.__name__, ctime(), pre))
            return func()
        return wrappedfunc
    return timefun
# 让装饰器生效
@timefun_arg("itheima")
def foo():
    print("I am foo")
foo()
