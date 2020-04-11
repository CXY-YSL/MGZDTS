f = open('itheima.txt', 'r')
content = f.readlines()
i = 1
for temp in content:
     print("%d:%s" % (i, temp))
     i += 1
f.close()