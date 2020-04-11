from time import ctime
# 装饰器函数
def timefun(func):
    def wrappedfunc(a, b): # 接收传递过来的两个参数
        # 调用函数的时间
        print("%s called at %s"%(func.__name__, ctime()))
        return func(a, b)
    return wrappedfunc
# 让装饰器生效
@timefun
# 带有两个参数的函数
def foo(a, b):
    print(a+b)
foo(3,5)
