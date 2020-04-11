# list = ['北京市','上海市','广州市','深圳市']
# city = input("输入需要查询的城市：")
# for i in range(0,len(list)):
#     if city == list:
#         new = input("输入需要修改的城市：")
#         list[i] = new
#         break
#     elif i == len(list)-1:
#         print("不存在")
# print(list)

import random
class Locker(object):
    def __init__(self):
        self._cell_num = 100
        self._use = 0
        self._surplus = self._cell_num
        self.cell = [0] * 100
    def show_cell_detail(self):
        print(f"总存包格数：总{self._cell_num}格,已用{self._use}格,剩余{self._surplus}格")
    def get_surplus(self):
            return self._surplus
    def check_cell(self):
        for i in range(0, 100):
            if self.cell[i] == 0:
                return i
        return -1
    def save_goods(self):
        self.passwd = random.randint(100000, 999999)
        self.cell_save = self.check_cell()
        self.cell[self.cell_save] = self.passwd
        self._use += 1
        self._surplus = self._cell_num - self._use
        print(f"{self.cell_save + 1}号箱门已打开，您的密码是{self.cell[self.cell_save]}")
    def get_goods_out(self, password):
        for i in range(100):
            if self.cell[i] == password:
                self.cell[i] = 0
                self._surplus += 1
                self._use = self._cell_num - self._surplus
                return i
        return -1
lock = Locker()
while True:
    lock.show_cell_detail()
    surplus = lock.get_surplus()
    operation = input("1-存放\n2-取出\n请输入对应操作：")
    if operation == "1":
        if surplus != 0:
            lock.save_goods()
        else:
            print("箱已存满，谢谢使用")
            break
    elif operation == "2":
        while True:
            password = input("请输入取件开箱码：")
            password = int(password)
            out_result = lock.get_goods_out(password)
            if out_result != -1:
                print(f"{out_result + 1}号箱门已打开，开箱码已失效，请取出物品，关好箱门")
                break
            else:
                print("开箱码错误或开箱码不存在，请核对后再输入！")
    else:
        print("请输入正确的操作！")
        continue