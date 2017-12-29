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

import pygame, sys, random
from pygame.locals import * #导入游戏常量
from PY_RPG.util import * #导入自己定义的一些工具方法



# def select_sort(lists):
#     # 选择排序
#     count = len(lists)
#     for i in range(0, count):
#         min = i
#         for j in range(i + 1, count):
#             if lists[min] > lists[j]:
#                 min = j
#         lists[min], lists[i] = lists[i], lists[min]
#     return lists



FPS = 30
fpsClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("select_sort")

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
    min = i
    for j in range(i+1,len(rects)):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,0))#背景色

        if rects[min][0] > rects[j][0]:
            min = j
        rects[min][0], rects[i][0] = rects[i][0], rects[min][0]

        if rects[min][1] > rects[j][1]:
            min = j
        rects[min][1], rects[i][1] = rects[i][1], rects[min][1]
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