# 定义类
class Car:
    # 移动
    def move(self):
        print("车在奔跑...")
    # 鸣笛
    def toot(self):
        print("车在鸣笛...嘟嘟...")
# 创建一个对象，并用变量BMW保存它的引用
BMW = Car()
# 添加表示颜色的属性
BMW.color = "黑色"
# 调用方法
BMW.move()
BMW.toot()
# 访问属性
print(BMW.color)