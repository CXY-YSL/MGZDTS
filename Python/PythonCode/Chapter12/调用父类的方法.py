# 定义父类Animal
class Animal(object):
    def __init__(self, legNum):
        # 腿的数量
        self.legNum = legNum
# 定义Bird类继承自Animal
class Bird(Animal):
    # 重写了父类的init方法
    def __init__(self, legNum):
        # 增加特有的属性
        self.plume = "白色"
        # 调用父类的init方法
        super().__init__(legNum)
bird = Bird(2)
print("有一只%s条腿%s羽毛的鸟儿站在树上唱歌！！"%(bird.legNum,bird.plume))