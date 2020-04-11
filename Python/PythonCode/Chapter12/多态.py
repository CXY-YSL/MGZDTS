# 定义一个表示动物的类
class Animal(object):
    def shout(self): # 叫的方法
        print("--Animal--shout--")
# 定义一个表示狗的类，继承自动物类
class Dog(Animal):
    def shout(self):  # 重写父类的方法
        print("--汪汪--")
# 定义一个表示猫的类，继承自动物类
class Cat(Animal):
    def shout(self): # 重写父类的方法
        print("--喵喵--")
# 定义一个函数
def func(temp):
    temp.shout()
dog = Dog()
func(dog)
cat = Cat()
func(cat)
