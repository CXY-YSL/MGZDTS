import time
try:
    f = open('test.txt',"w+")
    while True:
        content = f.read()
        if len(content) == 0:
            break
        time.sleep(2)
        print(content)
finally:
    f.close()
    print('关闭文件')
