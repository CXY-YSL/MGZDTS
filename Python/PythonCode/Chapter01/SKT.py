# # import calendar
# # print(calendar.calendar(2019,w=2,l=1,c=6))

# def showInfo():
#     print("1.添加学生\n2.删除学生\n3.修改学生\n4.显示所有学生信息\n5.退出系统\n")
# students=[]
# while True:
#     showInfo()
#     key = int(input("请选择功能（序号）："))
#     if key == 1:
#         print("您选择了添加学生信息功能")
#         stuName = input("请输入学生姓名：")
#         stuId = input("请输入学生学号(学号不可重复)：")
#         stuAge = input("请输入学生年龄:")
#         i = 0
#         leap = 0
#         for stu in students:
#             if stu['stuId'] == stuId:
#                 leap = 1
#                 break
#             else:
#                 i = i + 1
#         if leap == 1:
#             print("输入学生学号重复，添加失败！")
#         else:
#             stuInfo = {}
#             stuInfo['stuName'] = stuName
#             stuInfo['stuId'] = stuId
#             stuInfo['stuAge'] = stuAge
#             students.append(stuInfo)
#             print("添加成功！")
#     elif key == 2:
#         print("您选择了删除学生功能")
#         delId = input("请输入要删除的学生学号:")
#         i = 0
#         leap = 0
#         for stu in students:
#             if stu['stuId'] == delId:
#                 leap = 1
#                 break
#             else:
#                 i = i + 1
#         if leap == 0:
#             print("没有此学生学号，删除失败！")
#         else:
#             del students[i]
#             print("删除成功！")
#     elif key == 3:
#         print("您选择了修改学生信息功能")
#         alterId=input("请输入你要修改学生的学号:")
#         i = 0
#         leap = 0
#         for stu in students:
#             if stu['stuId'] == alterId:
#                 leap = 1
#                 break
#             else:
#                 i = i + 1
#         if leap == 1:
#             while True:
#                 alterNum=int(input(" 1.修改学号\n 2.修改姓名 \n 3.修改年龄 \n 4.退出修改\n"))
#                 if alterNum == 1:
#                     newId=input("输入更改后的学号:")
#                     i = 0
#                     leap1 = 0
#                     for stu1 in students:
#                         if stu1['stuId'] == newId:
#                             leap1 = 1
#                             break
#                         else:
#                             i = i + 1
#                     if leap1 == 1:
#                         print("输入学号不可重复，修改失败！")
#                     else:
#                         stu['stuId']=newId
#                         print("学号修改成功")
#                 elif alterNum == 2:
#                     newName=input("输入更改后的姓名:")
#                     stu['stuName'] = newName
#                     print("姓名修改成功")
#                 elif alterNum == 3:
#                     newAge=input("输入更改后的年龄:")
#                     stu['stuAge'] = newAge
#                     print("年龄修改成功")
#                 elif alterNum == 4:
#                     break
#                 else:
#                     print("输入错误请重新输入")
#         else:
#             print("没有此学号，修改失败！")
#     elif key == 4:
#         print("您选择了查询学生信息功能")
#         searchID=input("请输入你要查询学生的学号:")
#         i = 0
#         leap = 0
#         for stu in students:
#             if stu['stuId'] == searchID:
#                 leap = 1
#                 break
#             else:
#                 i = i + 1
#         if leap == 0:
#             print("没有此学生学号，查询失败！")
#         else:
#             print("找到此学生，信息如下：")
#             print("学号：%s\n姓名：%s\n年龄：%s\n"%(stu['stuId'],stu['stuName'],stu['stuAge']))
#     elif key == 5:
#         quitconfirm = input("亲，真的要退出么 （yes或者no）??~~(>_<)~~??")
#         if quitconfirm == 'yes':
#             print("欢迎使用本系统，谢谢")
#             break;
#     else:
#         print("您输入有误，请重新输入")

def showInfo():
    print("----------学生管理系统---------")
    print("1.添加学生\n2.删除学生\n3.修改学生\n4.显示所有学生信息\n5.退出系统\n")
    print('*' * 30)
students = []
def addStudent():
    print('*' * 30)
    stuName = input("请输入学生姓名：")
    stuId = input("请输入学生学号(学号不可重复)：")
    stuAge = input("请输入学生年龄:")
    i = 0
    leap = 0
    for stu in students:
        if stu['stuId'] == stuId:
            leap = 1
            break
        else:
            i += 1
    if leap == 1:
        print("学生学号重复，添加失败！")
    else:
        stuInfo = {}
        stuInfo['stuName'] = stuName
        stuInfo['stuId'] = stuId
        stuInfo['stuAge'] = stuAge
        students.append(stuInfo)
        print("添加成功！")
    print('*' * 30)
def deleteStudent():
    print('*' * 30)
    print("您选择了删除学生功能")
    delId=input("请输入要删除的学生学号:")
    i = 0
    leap = 0
    for stu in students:
        if stu['stuId'] == delId:
            leap = 1
            break
        else:
            i=i+1
    if leap == 0:
        print("学生学号不存在，删除失败！")
    else:
        del students[i]
        print("删除成功！")
    print('*' * 30)
def updateStudent():
    print('*' * 30)
    print("您选择了修改学生信息功能")
    alterId=input("请输入你要修改学生的学号:")
    i = 0
    leap = 0
    for stu in students:
        if stu['stuId'] == alterId:
            leap = 1
            break
        else:
            i = i + 1
    if leap == 1:
        updateOperate()
    else:
        print("学号不存在，修改失败！")
    print('*' * 30)
def updateOperate():
    print('*' * 30)
    while True:
        alterNum=int(input(" 1.修改学号\n 2.修改姓名 \n 3.修改年龄 \n 4.退出修改\n"))
        if alterNum == 1:
            newId=input("输入更改后的学号:")
            i = 0
            leap1 = 0
            for stu1 in students:
                if stu1['stuId'] == newId:
                    leap1 = 1
                    break
                else:
                    i = i + 1
            if leap1 == 1:
                print("输入学号不可重复，修改失败！")
            else:
                stu['stuId']=newId
                print("学号修改成功")
        elif alterNum == 2:
            newName=input("输入更改后的姓名:")
            stu['stuName'] = newName
            print("姓名修改成功")
        elif alterNum == 3:
            newAge=input("输入更改后的年龄:")
            stu['stuAge'] = newAge
            print("年龄修改成功")
        elif alterNum == 4:
            break
        else:
            print("输入错误请重新输入")
    print('*' * 30)
def getAllStudent():
    print('*'*30)
    print("所有学生信息...")
    print("stuId\t\t\t\t\t姓名\t\t\t\t年龄",chr(12288))
    for stu in students:
        print("%s\t\t\t%s\t\t\t\t%s"%(stu['stuId'],stu['stuName'],stu['stuAge']),chr(12288))
    print("*"*30)
def main():
    while True:
        showInfo()
        key = int(input("请选择功能（序号）："))
        if key == 1:
            addStudent()
        elif key == 2:
            deleteStudent()
        elif key == 3:
            updateStudent()
        elif key == 4:
            getAllStudent()
        elif key == 5:
            quitconfirm = input("确定退出？（N or F）")
            if quitconfirm == 'N':
                print("欢迎使用本系统，谢谢")
                break;
        else:
            print("您输入有误，请重新输入")
main()