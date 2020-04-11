# 计算1~num的累积和
def calculateNum(num):
    result = 0
    i = 1
    while i <= num:
        result = result + i
        i += 1
    return result
result = calculateNum(100)
print('1~100的累积和为:', result)