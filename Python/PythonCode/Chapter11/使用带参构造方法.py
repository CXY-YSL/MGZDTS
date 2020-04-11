# 定义类
class Car:
    # 带参构造方法
    def __init__(self, color):
        self.color = color
    # 鸣笛
    def toot(self):
        print("%s颜色的车在鸣笛..."%self.color)
# 创建一个对象，并用变量bmw保存它的引用
bmw = Car("雪山白")
# 创建一个对象，并用变量ferrari保存它的引用
ferrari = Car("红")
# 汽车鸣笛
bmw.toot()
ferrari.toot()