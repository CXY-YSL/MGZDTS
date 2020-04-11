# 定义类
class Dog:
    def __init__(self, newColor):
        self.color = newColor
    def printColor(self):
        print("颜色为：%s"%self.color)
dog1 =  Dog("白色")
dog1.printColor()
dog2 = Dog("黑色")
dog2.printColor()