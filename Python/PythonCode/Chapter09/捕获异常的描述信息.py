try:
    num1 = input("请输入第1个数：")
    num2 = input("请输入第2个数：")
    print(int(num1)/int(num2))
# 获取描述信息
except (ZeroDivisionError, ValueError) as result:
    print("捕捉到异常:%s"%result)
