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
# 用Pygame编写游戏（2）
###################################

import pygame, sys
from pygame.locals import * #导入游戏常量
from utils.BorderCrossing import *


###############
#一些游戏资源加载及设置
FPS = 30#帧速率
SCREEN_WIDTH=640
SCREEN_HEIGHT=480
WHITE = (255,255,255,)
pygame.display.set_caption("Hello World!")#窗口标题


BLACK = (0,0,0)
WHITE = (255,255,255,)
RED = (255,0,0)
GREEN  = (0,255,0)
BLUE = (0,0,255)
####加载图片资源


######################



    

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()#游戏初始化
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),DOUBLEBUF,32)#设置游戏场景游戏大小

    #####游戏循环
    while True:
        runGame()

def runGame():
    '''游戏核心方法，渲染游戏场景，游戏逻辑判断等'''
    myRects = [[pygame.Rect((10,110,40,40)),{'speed_x':15,'speed_y':15}],
               [pygame.Rect((100,400,40,40)),{'speed_x':10,'speed_y':10}],
               [pygame.Rect((270,130,40,40)),{'speed_x':8,'speed_y':8}],
               [pygame.Rect((50,260,40,40)),{'speed_x':5,'speed_y':5}],
    ]
    

    bc = BorderCrossing(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
    
    #######游戏引擎设置：判断游戏结束，更新游戏，刷新帧速率设置
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        ############
        drawbackground()#绘制场景背景颜色
        drawMyRect(myRects)#画一个运动的方块画方块
        game(myRects,bc)#方块运动逻辑判断，负责改写方块坐标。
        ##############
        
        # pygame.display.update()
        pygame.display.flip()
        FPSCLOCK.tick(FPS)#设置帧速率s

def drawbackground():
    '''绘制游戏背景'''
    DISPLAYSURF.fill(BLACK)#游戏窗口背景色
def drawMyRect(rects):
    for rect in rects:
        pygame.draw.ellipse(DISPLAYSURF, RED, rect[0])
    
def game(rects,bc):
    global speed_x,speed_y
    
    for r in rects:
        bc.sprite = r[0]
        if bc.isTopBorderCrossing() or bc.isBottomBorderCrossing():
            r[1]['speed_y'] = -r[1]['speed_y']
        if bc.isLeftBorderCrossing() or bc.isRightBorderCrossing():
            r[1]['speed_x'] = -r[1]['speed_x']
        
        r[0].x += r[1]['speed_x']
        r[0].y += r[1]['speed_y']


if __name__ == '__main__':
    main()
