#codeing=utf-8
# @Time    : 2017-10-23
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : “编学编玩”用Pygame编写游戏（5）pygame绘制一个钟表
# @Url     : http://www.17python.com/blog/48
# @Details : “编学编玩”用Pygame编写游戏（5）pygame绘制一个钟表
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            PyCharm
###################################
# “编学编玩”用Pygame编写游戏（5）pygame绘制一个钟表
###################################

'''
游戏中绘制圆及圆形的轨迹需求还是不少的，而且很多地方都需要用到圆及弧度的理论，如果想做些游戏的话，必须熟练掌握这些基本知识。

## 一些知识点

+ radius 圆的半径
+ diameter 圆的直径
+ angle 角度
+ 一个圆的完整的弧度 PI*2=6.28
+ 1弧度的角度值为 360/6.28=57.3248
+ 1度的弧度值为 6.28/360=0.0174
+ math.degrees(x)将角度x从弧度转换为度。
+ math.radians(x)将角度x从度转换为弧度。
+ math.sin(x)返回x弧度的正弦值。
+ math.cos(x)返回x弧度的余弦值。

## 圆周上点的坐标

    x = math.cos(math.radians(angle)) * (radius)
    y = math.sin(math.radians(angle)) * (radius）

如果不想深入了解的话，只需要记住，我们需要角度，即可求得圆周上的坐标值，对就上边的函数解释应该可以理解上边的python语句的含意。

## 实例

没有比绘制一个表盘更贴近实际需求的例子了，通过pythondatetime函数，我们可以很方便的获得时间，然后转换成相关数据。

以下为效果图，建议下载相关代码跑一下，有问题可以留言给我。

'''
import pygame, math, random, random, sys
from pygame.locals import *
from datetime import datetime, date, time



FPS = 30
fpsClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("圆孤的测试")
BLACK = (0,0,0)
WHITE = (255,255,255,)
RED = (255,0,0)
GREEN  = (0,255,0)
BLUE = (0,0,255)
color = (255,255,255)

pos_x = 300#圆中心x坐标
pos_y = 250#圆中心y坐标
angle = 360#角度
radius = 250#圆的半径



l_x = 300#圆中心x坐标
l_y = 250#圆中心y坐标
l_angle = 360#角度
l_radius = 600#圆的半径

lines = []
def wrap_angle(angle):
    return abs(angle % 360)

font1 = pygame.font.Font('./font/msyh.ttf', 16)
def print_text(font, x, y, text, color=(255,255,255)):
    '''本游戏中绘制游戏中文字的函数方法'''
    imgText = font.render(text, True, color,)
    screen.blit(imgText,(x,y))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.QUIT()

    screen.fill((0,0,0))#背景色
    pygame.draw.circle(screen, WHITE, (pos_x, pos_y), 6)#表盘中心点



    l_angle += 1
    if l_angle >=361:
        l_angle = 0
        # lines.clear()
    else:
        r = 0
        g = 0
        b = random.randint(0,255)
        rgb = r,g,b
        lx = math.cos(math.radians(l_angle)) * l_radius
        ly = math.sin(math.radians(l_angle)) * l_radius
        lend_xy = int(pos_x+lx),int(pos_y+ly)
        lines.append((lend_xy,rgb))
    for line in lines:
        pygame.draw.line(screen, line[1], (pos_x,pos_y), line[0], 5)



    #打印表盘上的数字
    for n in range(1,13):
        angle = math.radians(n * (360/12)-90) #求每个钟点数字的弧度，-90度表示从12点位置开始计算
        x = math.cos(angle)*(radius - 20) -10
        y = math.sin(angle)*(radius - 20) -10
        print_text(font1,pos_x+x,pos_y+y,str(n))

    today = datetime.today()
    hours = today.hour % 12
    minutes = today.minute
    seconds = today.second
    #以上为当前时间的小时，分，秒
    microsecond = today.microsecond
    msec = (microsecond//10000) 

    hour_angle = wrap_angle(hours * (360/12)-90)#求时针与12点的角度
    hour_angle = math.radians(hour_angle)#转换成弧度
    hour_x = math.cos(hour_angle) * (radius - 180)
    hour_y = math.sin(hour_angle) * (radius - 180)
    target = (pos_x+hour_x,pos_y+hour_y)#时针线结束点坐标
    pygame.draw.line(screen, WHITE, (pos_x,pos_y), target, 10)

    min_angle = wrap_angle(minutes * (360/60)-90)#求分针与12点的角度
    min_angle = math.radians(min_angle)#转换成弧度
    min_x = math.cos(min_angle) * (radius - 80)
    min_y = math.sin(min_angle) * (radius - 80)
    target = (pos_x+min_x,pos_y+min_y)#分针线结束点坐标
    pygame.draw.line(screen, WHITE, (pos_x,pos_y), target, 10)

    sec_angle = wrap_angle(seconds * (360/60)-90)#求秒针与12点的角度
    sec_angle = math.radians(sec_angle)#转换成弧度
    sec_x = math.cos(sec_angle) * (radius - 80)
    sec_y = math.sin(sec_angle) * (radius - 80)
    target = (pos_x+sec_x,pos_y+sec_y)#秒针线结束点坐标
    pygame.draw.line(screen, WHITE, (pos_x,pos_y), target, 10)


    print_text(font1,pos_x-50,pos_y+50,str(hours)+":"+str(minutes)+":"+str(seconds)+":"+str(msec))


    # pygame.draw.line(screen, color, (400,300), pos, 10)
    pygame.display.update()
    fpsClock.tick(FPS)#设置帧速率