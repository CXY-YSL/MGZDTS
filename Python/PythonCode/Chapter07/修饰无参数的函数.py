from time import ctime
# 装饰器函数
def timefun(func):
    def wrappedfunc():
        # 调用函数的时间
        print("%s called at %s"%(func.__name__, ctime()))
        return func()
    return wrappedfunc
@timefun # 标注装饰器
def foo():
    print("I am foo")
foo()
