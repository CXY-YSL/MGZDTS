# 定义类
class Demo:
    data1 = 100
    # 定义为属性data2赋值的方法
    def set(self, num):
        self.data2 = num
    # 重载方法
    def __str__(self):
        # 返回自定义的字符串
        return 'data1=%s; data2=%s'%(self.data1,self.data2)
# 创建实例对象
demo = Demo()
# 调用方法给属性赋值，并创建属性
demo.set(200)
print(demo)         # 调用__str__方法进行转换
print(str(demo))   # 调用repr函数，结果显示没有进行转换
print(repr(demo))  # 调用__str__方法进行转换