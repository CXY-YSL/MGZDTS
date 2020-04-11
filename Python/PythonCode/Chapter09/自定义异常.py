class ShortInputException(Exception):
    '''自定义异常类'''
    def __init__(self, length, atleast):
        self.length = length     # 输入长度
        self.atleast = atleast   # 至少的长度
try:
    text = input("请输入密码：")
    if len(text) < 3:
        # raise引发一个刚刚定义的异常
        raise ShortInputException(len(text), 3)
except EOFError:
    print("你输入了一个结束标记")
except ShortInputException as result:
    print("ShortInputException：输入的长度是%d，"
          "长度至少应是%d"%(result.length, result.atleast))
else:
    print("没有异常发生")
