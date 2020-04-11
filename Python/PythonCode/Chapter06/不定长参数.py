def test(a, b, *args):
    print(a)
    print(b)
    print(args)
test(11, 22)

class test():


def test(a, b, *args):
    print(a)
    print(b)
    print(args)
test(11, 22, 33, 44, 55, 66, 77, 88, 99)


def test(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
test(11, 22, 33, 44, 55, 66, 77, 88, 99)

def test(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
test(11,22,33,44,55,66,77,m=88,n=99)
