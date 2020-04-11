class Person:
    def __init__(self, name, age):
        self.name = name # 姓名
        self.__age = age # 年龄
    # 给私有属性赋值
    def setNewAge(self, newAge):
        # 判断传入的参数是否符合要求
        if newAge>0 and newAge<=120:
            self.__age = newAge
    # 获取私有属性的值
    def getAge(self):
        return self.__age
# 创建对象
laowang = Person("老王", 30)
print(laowang.__age)