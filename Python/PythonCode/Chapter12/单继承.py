# 定义一个表示猫的类
class Cat(object):
    def __init__(self, color="白色"):
        self.color = color # 颜色
    def run(self): # 定义用于跑的方法
        print("---跑---")
# 定义一个猫的子类波斯猫
class PersianCat(Cat):
    pass
cat = PersianCat("黑色")
cat.run()
print(cat.color)