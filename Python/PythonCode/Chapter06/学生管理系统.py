#用来保存学生的所有信息
stuInfos=[]
#打印功能提示
def printMenu():
    print("="*30)
    print(" 学生管理系统V1.0 ")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.显示所有学生信息")
    print("0.退出系统")
    print("="*30)
#添加一个学生信息
def addStuInfo():
    # 提示并获取学生的姓名
    newName = input("请输入新学生的名字：")
    # 提示并获取学生的性别
    newSex = input("请输入新学生的性别：(男/女)")
    # 提示并获取学生的手机号码
    newPhone = input("请输入新学生的手机号码：")
    newInfo = {}
    newInfo['name'] = newName
    newInfo['sex'] = newSex
    newInfo['phone'] = newPhone
    stuInfos.append(newInfo)

#修改一个学生的信息
def modifyStuInfo():
     stuId=int(input("请输入要修改的学生的序号："))
     newName = input("请输入新学生的名字：")
     newSex = input("请输入新学生的性别：(男/女)")
     newPhone = input("请输入新学生的手机号码：")
     stuInfos[stuId - 1]['name'] = newName
     stuInfos[stuId - 1]['sex'] = newSex
     stuInfos[stuId - 1]['phone'] = newPhone
# 定义一个用户显示所有学生信息的函数
def showStuInfo():
    print("=" * 30)
    print("学生的信息如下:")
    print("=" * 30)
    print("序号    姓名    性别   手机号码")
    i = 1
    for tempInfo in stuInfos:
        print("%d      %s      %s     %s" % (i, tempInfo['name'],tempInfo['sex'], tempInfo['phone']))
        i += 1

def main():
    while True:
        printMenu()
        key = input("请输入功能对应的数字")
        if key == '1':
            addStuInfo()
        elif key == '3':
            modifyStuInfo()
        elif key == '4':
            showStuInfo()
main()