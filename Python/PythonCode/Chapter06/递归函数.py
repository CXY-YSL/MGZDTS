def fn(num):
    if num==1:
        result=1
    else:
        result= fn(num-1)*num
    return  result
n=int(input("请输入一个正整数:"))
print("%d！="%n, fn(n))