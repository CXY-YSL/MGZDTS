class Foo(object):
    def __init__(self, func):
        super(Foo, self).__init__()
        self._func = func
    def __call__(self):
        print('class decorator')
        self._func()
# 类装饰器
@ Foo
def bar():
    print('I am bar')
bar()
