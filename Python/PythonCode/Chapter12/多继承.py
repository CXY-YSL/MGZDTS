# 定义表示鸟的类
class Bird(object):
    # 飞
    def fly(self):
        print("--鸟儿在天空飞翔--")
# 定义表示鱼的类
class Fish(object):
    # 游
    def swim(self):
        print("--鱼儿在水中遨游--")
# 定义表示飞鱼的类
class Volador(Bird, Fish):
    pass
vola = Volador()
vola.fly()
vola.swim()
