#codeing=utf-8
# @Time    : 2017-10-15
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : “编学编玩”用Pygame写游戏（2）在场景中绘制图形与动画
# @Url     : http://www.17python.com/blog/45
# @Details : “编学编玩”用Pygame写游戏（2）在场景中绘制图形与动画
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# “编学编玩”用Pygame写游戏（2）在场景中绘制图形与动画
###################################

'''
pygame的框架使用起来很简单，但这个框架功能也还算可以的，虽然网上对pygame评价褒贬不一，但对于其的存在必有其的存在意义，
功能上虽然不能说是十分的完美，但对于新手来说，在使用和学习中还是很有价值的。

## pygame 图形绘制

rect	绘制矩形
polygon	绘制多边形（三个及三个以上的边）
circle	绘制圆
ellipse	绘制椭圆
arc	绘制圆弧
line	绘制线
lines	绘制一系列的线
aaline	绘制一根平滑的线
aalines	绘制一系列平滑的线

上边列举了一些图形绘制的方法，第一结中的代码我们只是给出pygame中最简约的实现代码，我们在上节代码的基础之上继续添加一下，试试画出各种图形。

    pygame.draw.polygon(screen, RED, ((146,0),(290,100),(36,277),(55,200),(0,106)),2)
    pygame.draw.line(screen, BLUE, (11,33), (55,300), 1)
    pygame.draw.circle(screen, GREEN, (300,50), 100, 0)
    pygame.draw.ellipse(screen, RED, (300,250,180,80), 1)
    pygame.draw.rect(screen, RED, (200,150,100,100), 1)

以上为各种图形绘制的方法演示，关于这些方法的参数，我们可以参考官方的文档，其实都是挺简单的。



## 在场景中绘制图片

游戏中的角色不可能只是一些简单的图形，大多数时应该都是一张张图片，我们看下图片的绘制方法

    bosiImg = pygame.image.load('./images/bosi.png')
    screen.blit(bosiImg,(bosix,bosiy))

通过pygame.image.load()加载图片后，在场景中使用screen.blit绘制，两个参数：图片对象和一个坐标元组。

## 在场景中写字

pygame中的文字绘制稍稍有一点麻烦，我们看代码：

    fobj = pygame.font.Font('./font/3.ttf', 40)
    textobj = fobj.render('Hello World', True, GREEN,)
    text = textobj.get_rect()
    text.center = (400, 400)
    screen.blit(textobj, text)#文字显示

看代码行数是五步：

1. 通过pygame.font.Font()加载字体，创建一个font对象，设置文字的大小
2. 通过render('Hello World', True, GREEN,)设置文字的内容，颜色。
3. get_rect()或得一个rect对象，之后就有些象绘制图象了。
4. 设置绘制图像的坐标
5. blit()方法绘制文字到场景

## 让图片动起来

如何在场景中绘制动画？动画其实就是角色坐标值的修改，

    bosix = 100
    bosiy = 100

在代码中我定义了二个变量，然后我在游戏场景的循环输出中，不断的修改角色的坐标值即可达到需要的动画效果了。

'''

import pygame, sys
from pygame.locals import * #导入游戏常量

pygame.init()#游戏初始化
###############

FPS = 30
#帧速率 这个与后边的fpsClock.tick(FPS)方法相对应。
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
    screen.fill(BLACK)#游戏窗口背景色
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