# 定义表示人的类
class Person(object):
    # 打招呼的方法
    def sayHello(self):
        print("--Hello--")
# 定义Chinese类继承自Person类
class Chinese(Person):
	# 中国人打招呼的方法
    def sayHello(self):
        print("吃了吗？")
# 创建Chinese类的对象
chinese = Chinese()
chinese.sayHello()