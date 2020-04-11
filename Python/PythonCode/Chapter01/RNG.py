# def add( a = 10 , b = 30 ):
#     print( a + b )
#
#
# def add( a = 10 , b = 30 ):
#     return ( a + b )

import sys
users = [[123456789, 'Mike', '111111', 6000000]]
ID = -1

def check(s):
    if s.isdecimal():
        return True
    return False
def passwordCheck(p):
    if p == '' or p.isdecimal() == False or len(p) != 6:
        return False
    return True
def login():
    account = input('请输入您的账户：')
    if account == '' or account.isdecimal() == False or len(account) < 7:
        print('\n输入不合法，自动返回...')
        return
    else:
        account = int(account)
    password = input('请输入用户密码：')
    if passwordCheck(password) == False:
        print('\n输入不合法，自动返回...')
        return
    for i in range(len(users)):
        if users[i][0] == account and users[i][2] == password:
            print('登录成功！')
            global ID
            ID = i
            break
    if ID == -1:
        print('\n账户不存在或密码错误！ 自动返回...')
    else:
        fun()
def register():
    username = input('请输入用户名：')
    if username == '':
        print('\n输入不合法，自动返回...')
        return
    password = input('请输入用户密码(密码为6位数字组成)：')
    if passwordCheck(password) == False:
        print('\n输入不合法，自动返回...')
        return
    M = 0
    for i in users:
        M = max(M, i[0])
    users.append([M + 1, username, password, 0])
    print('\n注册成功！ 您的账户为：', M + 1)
def main():
    while True:
        print('\n\n      ******************')
        print('       *自动提款机系统*')
        print('      ******************\n')
        print('*********************************')
        print('******   登录-------1  **********')
        print('******   注册-------2  **********')
        print('******   退出-------0  **********')
        print('*********************************\n')
        v = input('请输入对应的数字：')
        if check(v) == False or 2 < int(v) or int(v) < 0:
            print('\n输入不合法，请重新输入！')
            continue
        else:
            v = int(v)
        if v == 2:
            register()
        elif v == 1:
            login()
        elif v == 0:
            sys.exit(0)
def fun():
    while True:
        print('\n***************************************')
        print('********  查询--------1  **********')
        print('********  取款--------2  **********')
        print('********  存款--------3  **********')
        print('********  转账--------4  **********')
        print('********  修改密码----5  **********')
        print('********  返回上一层------6  **********')
        print('********  退出------------0  **********')
        print('***************************************\n')
        v = input('请输入对应的数字：\n')
        if check(v) == False or 6 < int(v) or int(v) < 0:
            print('\n输入不合法，请重新输入！')
            continue
        else:
            v = int(v)
        if v == 1:
            print('您的当前余额为：', users[ID][3])
        elif v == 2:
            money = input('请输入取款金额：')
            if check(money) == False:
                print('\n输入不合法，自动返回...')
                continue
            else:
                money = int(money)
            if money > users[ID][3]:
                print('余额不足，不能取款')
            else:
                users[ID][3] -= money
                print('\n取款成功！ 您的余额还有', users[ID][3], '元')
        elif v == 3:
            money = input('请输入存款金额：')
            if check(money) == False:
                print('\n输入不合法，自动返回...')
                continue
            else:
                money = int(money)
            users[ID][3] += money
            print('\n存款成功！ 您的余额还有', users[ID][3], '元')
        elif v == 4:
            IDD = -1
            account = input('请输入对方账户：')
            if account == '' or check(account) == False:
                print('\n输入不合法，自动返回...')
                continue
            else:
                account = int(account)
            for i in range(len(users)):
                if users[i][0] == account:
                    IDD = i
                    break
            if IDD == -1:
                print('\n该账户不存在，自动返回...')
                continue
            money = input('请输入转账金额：')
            if money == '' or check(money) == False:
                print('\n输入不合法，自动返回...')
                continue
            else:
                money = int(money)
            if money > users[ID][3]:
                print('余额不足，转账失败,自动返回...')
                continue
            else:
                users[ID][3] -= money
                users[IDD][3] += money
                print('转款成功！ 您的余额还有', users[ID][3], '元')
        elif v == 5:
            password = input('请输入旧密码：')
            if password == users[ID][2]:
                password1 = input('请输入用户密码(密码为6位数字组成)：')
                if passwordCheck(password1) == False:
                    print('\n密码输入非法，自动返回...')
                    continue
                password2 = input('请再次输入密码')
                if password1 != password2:
                    print('两次密码输入不一致，请重新输入：')
                else:
                    users[ID][2] = password2
                    print('密码修改成功！')
            else:
                print('\n密码输入错误，自动返回...')
        elif v == 0:
            sys.exit(0)
        elif v == 6:
            main()

