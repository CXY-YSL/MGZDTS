import pygame
import time
import random
from pygame.locals import *

class HeroPlane(object):

    def __init__(self,screen):
        #设置飞机默认的位置
        self.x = 160
        self.y = 500
        #设置要显示内容的窗口
        self.screen = screen
        #用来保存英雄飞机需要的图片名字
        self.imageName = "./feiji/hero.gif"
        #根据名字生成飞机图片
        self.image = pygame.image.load(self.imageName).convert()
        # 用来存储英雄飞机发射的所有子弹
        self.bulletList = []

    def display(self):
        # 更新飞机的位置
        self.screen.blit(self.image, (self.x, self.y))
        # 用来存放需要删除的对象信息
        needDelItemList = []
        # 保存需要删除的对象
        for i in self.bulletList:
            if i.judge():
                needDelItemList.append(i)
        # 删除self.bulletList中需要删除的对象
        for i in needDelItemList:
            self.bulletList.remove(i)

        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

    def sheBullet(self):
        newBullet = Bullet(self.x, self.y, self.screen)
        self.bulletList.append(newBullet)

    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10


class EnemyPlane(object):
    def __init__(self,screen):
        #设置飞机默认的位置
        self.x = 0
        self.y = 0
        #设置要显示内容的窗口
        self.screen = screen
        self.imageName = "./feiji/enemy-1.gif"
        self.image = pygame.image.load(self.imageName).convert()
        #用来存储敌人飞机发射的所有子弹
        self.bulletList = []
        self.direction = "right"

    def move(self):
        # 如果碰到了右边的边界，那么就往左走，如果碰到了左边的边界，那么就往右走
        if self.direction == "right":
            self.x += 2
        elif self.direction == "left":
            self.x -= 2
        if self.x > 430 - 50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def display(self):
        # 更新飞机的位置
        self.screen.blit(self.image, (self.x, self.y))

        # 存放需要删除的对象信息
        needDelItemList = []

        for i in self.bulletList:
            if i.judge():
                needDelItemList.append(i)

        for i in needDelItemList:
            self.bulletList.remove(i)

        # 更新及这架飞机发射出的所有子弹的位置
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

    def sheBullet(self):
        num = random.randint(1, 100)
        if num == 88:
            newBullet = EnemyBullet(self.x, self.y, self.screen)
            self.bulletList.append(newBullet)

class Bullet(object):
    def __init__(self,x,y,screen):
        self.x = x+40
        self.y = y-20
        self.screen = screen
        self.image = pygame.image.load("./feiji/bullet-3.gif").convert()

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y -= 2

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

class EnemyBullet(object):
    def __init__(self,x,y,screen):
        self.x = x+22
        self.y = y+30
        self.screen = screen
        self.image = pygame.image.load("./feiji/bullet-1.gif").convert()

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y += 20

    def judge(self):
        if self.y>750:
            return True
        else:
            return False

if __name__ == "__main__":
    #1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((430,750),0,32)

    #2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png").convert()

    #3. 创建一个飞机对象
    heroPlane = HeroPlane(screen)

    # 4. 创建一个敌人飞机
    enemyPlane = EnemyPlane(screen)

    #4. 把背景图片放到窗口中显示
    while True:
        screen.blit(background,(0,0))
        heroPlane.display()
        enemyPlane.display()
        enemyPlane.move()
        enemyPlane.sheBullet()

        #判断是否是点击了退出按钮
        for event in pygame.event.get():
            # print(event.type)
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:

                if event.key == K_a or event.key == K_LEFT:
                    # print('left')
                    #控制飞机让其向左移动
                    heroPlane.moveLeft()
                elif event.key == K_d or event.key == K_RIGHT:
                    # print('right')
                    heroPlane.moveRight()
                elif event.key == K_SPACE:
                    heroPlane.sheBullet()

        # 通过延时的方式，来降低这个while循环的循环速度，从而降低了cpu占用率
        time.sleep(0.05)
        pygame.display.update()