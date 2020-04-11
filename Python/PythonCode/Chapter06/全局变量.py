# # 定义全局变量
# a = 100
# def test1():
#     print(a)
# def test2():
#     print(a)
# # 调用函数
# test1()
# test2()

# a=50
# def test():
#     a=100
#     print("a=%d"%a)
# #调用函数
# test()

a=50
def test():
    global a
    print("a=%d"%a)
#调用函数
test()