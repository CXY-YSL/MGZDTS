# 定义类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __del__(self):
        print("--------del--------")
laowang = Person("老王", 30)
del laowang
print("---------1---------")