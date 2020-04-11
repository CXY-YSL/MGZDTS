class Test(object):
    @staticmethod # 静态方法
    def printTest():
        print("我是静态方法")
Test.printTest()
test = Test()
test.printTest()
