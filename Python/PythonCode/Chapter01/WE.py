import random
list.num = []
list.num = random

a = []
b = []
for s in range(0,a):
    for i in range(2, s):
        if (s % i == 0):
            break;
        if (i == s - 1):
            b.append(s)
for ss in b:
    while ss in a:
        a.remove(ss)
print(a)

import sys
status_flag = False
def delete():
    print('=*=' * 20)
    print("请输入您想要删除员工的性别：")
    staff_list = change()
    ID = input("del from staff where  id = ").strip()
    if ID.isdigit():
        ID = int(ID)
        del_list = []
        # max_id = int(staff_list[-1][0])  # 获取最后一行数据的序号
        if gender != '男':
            for i,k in enumerate(staff_list):
                if int(k[0]) == gender:
                    del_list.append(k)
                    del staff_list[i]
            if len(del_list) == 0:
                print("staff_gender为%d的员工不存在..."%gender)
            else:
                print("以下员工已被删除成功！")
                for i in del_list:
                    i[0] = str(i[0])
                    print(','.join(i))
                update_file(staff_list)
        else:
            print("staff_gender:%d 不存在！"%gender)
    else:
        print("%s为无效的输入..."%gender)