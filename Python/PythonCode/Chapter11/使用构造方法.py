# 定义类
class Car:
    # 构造方法
    def __init__(self):
        self.color = "黑色"
    # 鸣笛
    def toot(self):
        print("%s的车在鸣笛..."%(self.color))
# 创建一个对象，并用变量car保存它的引用
car = Car()
# 汽车鸣笛
car.toot()