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
from PY_RPG.util  import * #导入自己定义的一些工具方法



# def insert_sort(lists):
#     # 插入排序
#     count = len(lists)#数组成员数
#     for i in range(1, count):
#         key = lists[i]#第二个数
#         j = i - 1#取数组中第一数据
#         while j >= 0:
#             if lists[j] > key:
#                 #如果左边大于右边的数据，交换位置
#                 lists[j + 1] = lists[j]
#                 lists[j] = key
#             j -= 1
#     return lists



FPS = 30
fpsClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("insert_sort")

gametime = pygame.time.get_ticks()
lx = []
ly = []
rects = []
for i in range(200):
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
for i in range(1,len(rects)):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))#背景色
    x = rects[i][0]#x
    y = rects[i][1]#x
    j = i - 1#取数组中第一数据
    while j >= 0:
        if rects[j][0] > x:
            #如果左边大于右边的数据，交换位置
            rects[j + 1][0] = rects[j][0]
            rects[j][0] = x
        

        if rects[j][1] > y:
            #如果左边大于右边的数据，交换位置
            rects[j + 1][1] = rects[j][1]
            rects[j][1] = y
        j -= 1

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