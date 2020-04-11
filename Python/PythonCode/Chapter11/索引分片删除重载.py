# 定义类
class Demo:
    # 定义构造方法
    def __init__(self, obj):
        self.data = obj[:]
    # 重载索引、分片删除运算方法
    def __delitem__(self, index):
        del self.data[index]
# 创建实例对象，并用列表初始化
x = Demo([1,2,3,4,5])
# 显示对象属性中的列表
print(x.data)
# 删除列表的第一个元素
del x[0]
# 显示删除元素后的列表
print(x.data)
# 删除分片
del x[1:3]
# 显示删除分片后的列表
print(x.data)