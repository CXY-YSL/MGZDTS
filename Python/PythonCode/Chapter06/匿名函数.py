# sum = lambda arg1, arg2: arg1 + arg2
# # 调用sum函数
# print("运行结果：", sum(10, 20))
# print("运行结果：", sum(20, 20))

# def fun(a,b,opt):
#    	print("a=%d"%a)
#    	print("b=%d" %b)
#    	print("result=",opt(a,b))
# fun(11,22,lambda x,y:x+y)
# print("-------------------")
# fun(11,22,lambda x,y:x-y)

stus = [
    {"name":"zhangsan", "age":18},
    {"name":"lisi", "age":19},
    {"name":"wangwu", "age":17}
]
#按name排序：
stus.sort(key = lambda x:x['name'])
print("按name排序后的结果为：",stus)
#按age排序
stus.sort(key = lambda x:x['age'])
print("按age排序后的结果为：",stus)