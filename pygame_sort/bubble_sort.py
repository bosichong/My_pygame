#codeing=utf-8
# @Time    : 2017-10-15
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 用Pygame编写游戏（1）
# @Url     : http://www.17python.com/blog/44
# @Details : 用Pygame编写游戏（1）
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# 用Pygame编写游戏（3）
###################################

import pygame, os, sys, random
from pygame.locals import * #导入游戏常量

#导入自定义游戏包
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取当前文件上级目录的绝对地址
sys.path.append(BASE_DIR)#添加一个模块搜索目录，方便找到自己的建的模块
from PY_RPG.util import *



# def bubble_sort(lists):
#     # 冒泡排序
#     count = len(lists)
#     for i in range(0, count):
#         for j in range(i + 1, count):
#             if lists[i] > lists[j]:
#                 lists[i], lists[j] = lists[j], lists[i]
#     return lists



FPS = 30
fpsClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("bubble_sort")

gametime = pygame.time.get_ticks()
lx = []
ly = []
rects = []
for i in range(50):
    x = random.randrange(0,500,2)
    if x not in lx:
        lx.append(x)
    y = random.randrange(0,500,2)
    if x not in lx:
        ly.append(y)
    rects.append([x,y,10,10])


random.shuffle(rects)
print(rects)


##这里是算法实现区，通过排序算法动态修改坐标
for i in range(0,len(rects)):
    for j in range(i+1,len(rects)):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,0))#背景色


        if rects[i][0] > rects[j][0]:
                rects[i][0], rects[j][0] = rects[j][0], rects[i][0]
        if rects[i][1] > rects[j][1]:
                rects[i][1], rects[j][1] = rects[j][1], rects[i][1]
        for rect in rects :
            pygame.draw.rect(screen, BLUE, rect,)
            
        # print(pygame.time.get_ticks())
        pygame.display.update()
        fpsClock.tick(FPS)#设置帧速率


while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
    screen.fill((0,0,0))#背景色
    for rect in rects :
        pygame.draw.rect(screen, BLUE, rect,)
    # print(pygame.time.get_ticks())
    pygame.display.update()
    fpsClock.tick(FPS)#设置帧速率