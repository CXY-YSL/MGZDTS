class Test(object):
    # 类属性
    num = 0
    # 类方法
    @classmethod
    def setNum(cls, newNum):
        cls.num = newNum
Test.setNum(300)
print(Test.num)
