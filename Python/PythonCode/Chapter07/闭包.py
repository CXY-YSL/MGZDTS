# 外部函数
def outer(start=0):
    count = [start]  # 函数内的变量
    # 内部函数
    def inner():
        count[0] += 1  # 引用外部函数的变量
        return count[0]
    # 返回内部函数的名称
    return inner
out = outer(5)
print(out())
