while True:
    try:
        x = int(input('请输入第一个数：'))
        y = int(input('请输入第二个数：'))
        assert x>1 and y>1, "a和b的值必须大于1"   # 断言
        a = x
        b = y
        if a<b:
            a,b = b,a     # a与b的值互换
        while b!=0:       # 使用辗转相除法求最大公约数
            temp = a%b
            a = b
            b = temp
        else:
            print('%s和%s的最大公约数为：%s'%(x,y,a))
            break
    except Exception as result:
        print('捕捉到异常：\n',result)
