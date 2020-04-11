try:
    num1 = input("请输入第1个数：")
    num2 = input("请输入第2个数：")
    print(int(num1)/int(num2))
except Exception as result:
    print("捕捉到异常:%s"%result)
else:
    print("程序正常运行，没有捕捉到异常")
