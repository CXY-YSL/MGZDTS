def displayMenu():
    print("-"*30)
    print("   名片管理系统   v8.8")
    print("1. 添加名片")
    print("2. 删除名片")
    print("3. 修改名片")
    print("4. 查询名片")
    print("5. 获取所有名片信息")
    print("6. 退出系统")
    print("-"*30)
i = 0
# while i < 1:
    # 打印菜单
displayMenu()
# 获取用户输入的信息
def getChoice():
    selectedKey = input("请输入选择的序号：")
    return int(selectedKey)
# 等待用户选择
key = getChoice()
if key == 1:
    pass
elif key == 2:
    pass
elif key == 3:
    pass
elif key == 4:
    pass
elif key == 5:
    pass
elif key == 6:
    pass
else:
    print("输入有误，请重新输入...")


# 查看所有名片的信息
def printAllInfo(tempList):
    print("=" * 30)
    for info in tempList:
        print(info)
    print("=" * 30)