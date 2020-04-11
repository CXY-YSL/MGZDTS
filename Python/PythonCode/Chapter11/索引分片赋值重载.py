# 定义类
class Demo:
    # 定义构造方法
    def __init__(self, obj):
        self.data = obj[:]
    # 重载索引、分片赋值运算方法
    def __setitem__(self, index, value):
        self.data[index] = value
# 创建实例对象，并用列表初始化
x = Demo([1,2,3,4,5])
# 显示对象属性中的列表
print(x.data)
x[0] = 'abc'                # 修改列表第一个元素
print(x.data )               # 显示修改后的列表
x[1:3] = ['a','b','c']    # 把列表中的分片[1:3]替换为列表[‘a’,‘b’,‘c’]
print(x.data)                # 显示修改后的列表