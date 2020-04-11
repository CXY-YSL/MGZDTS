try:
    num1 = input("请输入第1个数：")
    num2 = input("请输入第2个数：")
    print(int(num1)/int(num2))
except ZeroDivisionError:
    print("第2个数不能为0")
except ValueError:
    print("只能输入数字")
