# 批量在文件名前加前缀
import os
funFlag = 1 # 1表示添加标志  2表示删除标志
folderName = './'
# 获取指定路径的所有文件名字
dirList = os.listdir(folderName)
# 遍历输出所有文件名字
for name in dirList:
    print(name)
    if funFlag == 1:
        newName = '[黑马程序员]-' + name
    elif funFlag == 2:
       	num = len('[黑马程序员]-')
        newName = name[num:]
    print(newName)
    os.rename(folderName+name, folderName+newName)
