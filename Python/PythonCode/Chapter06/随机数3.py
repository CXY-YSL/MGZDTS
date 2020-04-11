import random
#生成的随机数n: 12 <= n <= 20
print(random.randint(12,20))
#结果永远是20
print(random.randint(20,20))
#print random.randint(20, 10)   #该语句是错误的。下限必须小于上限。  