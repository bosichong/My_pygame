#codeing=utf-8
# @Time    : 2017-10-15
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : “编学编玩”用Pygame写游戏（1）
# @Url     : http://www.17python.com/blog/44
# @Details : “编学编玩”用Pygame写游戏（1）
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# “编学编玩”用Pygame写游戏（1）初识pygame
###################################

'''




rect	绘制矩形
polygon	绘制多边形（三个及三个以上的边）
circle	绘制圆
ellipse	绘制椭圆
arc	绘制圆弧
line	绘制线
lines	绘制一系列的线
aaline	绘制一根平滑的线
aalines	绘制一系列平滑的线

'''

import pygame, sys
from pygame.locals import * #导入游戏常量

pygame.init()#游戏初始化
###############

FPS = 30#帧速率
SCREEN_WIDTH=640
SCREEN_HEIGHT=480
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))#设置游戏场景游戏大小
pygame.display.set_caption("Hello World!")#窗口标题
#######################
BLACK = (0,0,0)
WHITE = (255,255,255,)
RED = (255,0,0)
GREEN  = (0,255,0)
BLUE = (0,0,255)
####加载图片资源
bosiImg = pygame.image.load('./images/bosi.png')
bosix = 100
bosiy = 100
###文字设置
fobj = pygame.font.Font('./font/3.ttf', 40)
textobj = fobj.render('Hello World', True, GREEN,)
text = textobj.get_rect()
text.center = (400, 400)
######################
while True:
    screen.fill(WHITE)#游戏窗口背景色
    ##################
    pygame.draw.polygon(screen, RED, ((146,0),(290,100),(36,277),(55,200),(0,106)),2)
    pygame.draw.line(screen, BLUE, (11,33), (55,300), 1)
    pygame.draw.circle(screen, GREEN, (300,50), 100, 0)
    pygame.draw.ellipse(screen, RED, (300,250,180,80), 1)
    pygame.draw.rect(screen, RED, (200,150,100,100), 1)
    #############
    screen.blit(textobj, text)#文字显示
    bosix += 1
    bosiy += 1
    screen.blit(bosiImg,(bosix,bosiy))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()#刷新游戏场景
    fpsClock.tick(FPS)#设置帧速率