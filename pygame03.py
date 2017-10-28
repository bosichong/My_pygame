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

import pygame, sys
from pygame.locals import * #导入游戏常量
from PY_RPG.BorderCrossing import *
import random


###############
#一些游戏资源加载及设置
FPS = 30#帧速率
SCREEN_WIDTH=640
SCREEN_HEIGHT=480
WHITE = (255,255,255,)
pygame.display.set_caption("Hello World!")#窗口标题


BLACK = (0,0,0)
WHITE = (255,255,255,)
RED = (255,0,0,0)
GREEN  = (0,255,0)
BLUE = (0,0,255)
####加载图片资源


######################



    

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()#游戏初始化
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))#设置游戏场景游戏大小

    #####游戏循环
    while True:
        runGame()

def runGame():
    '''游戏核心方法，渲染游戏场景，游戏逻辑判断等'''
    ms = MyRectSprite(DISPLAYSURF)
    mi = MyImgSprite(DISPLAYSURF)
    # group = pygame.sprite.Group()
    #精灵组目前只能添加处理图片类形的精灵，纯图形类的建议用list。
    #因为group.draw方法只能绘制图片使用blit()
    # group.add(mi)
    clock = pygame.time.Clock()
    #游戏时间



    
    #######游戏引擎设置：判断游戏结束，更新游戏，刷新帧速率设置
    while True:
         
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                down = pygame.mouse.get_pressed()
                if down[0] == 1:
                    print(pygame.mouse.get_pos())#鼠标坐标
                    print(pygame.mouse.get_pressed())#鼠标按下状态

        
        ############
        # pygame.time.wait(1000)#时间暂停一秒
        # print(pygame.time.get_ticks())#游戏运行初始化开始计时
        drawbackground()#绘制场景背景颜色
        ms.draw()
        ms.update()
        mi.draw()
        mi.update()

        ##############
        pygame.display.update()#刷新游戏场景
        FPSCLOCK.tick(FPS)#设置帧速率s

def drawbackground():
    '''绘制游戏背景'''
    DISPLAYSURF.fill(BLACK)#游戏窗口背景色

        

def game(rects,bc):
    pass


class MyRectSprite(pygame.sprite.Sprite):
    '''形状精灵类'''
    def __init__(self, display):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       self.display = display#渲染器
       self.rect = pygame.Rect((500,110,40,40))#精灵的形状
       self.speed = 3
       self.last_update = pygame.time.get_ticks()#游戏开始时的计时

    
    def draw(self):
        '''绘制精灵'''
        pygame.draw.ellipse(self.display, RED, self.rect, 1)
    def update(self):
        now = pygame.time.get_ticks()
        # print(self.speed)
        if now - self.last_update > 1000:
            if self.speed > 0 :
                self.speed = self.speed - 1 
                self.last_update = now
            elif self.speed < 0 :
                self.speed = self.speed + 1 
                self.last_update = now
            else :
                self.speed = 10
                self.last_update = now

        if self.rect.y + self.rect.height >= SCREEN_HEIGHT:
            self.speed = -self.speed
        if self.rect.y  <= 0:
            self.speed = -self.speed
        self.rect.y += self.speed

class MyImgSprite(pygame.sprite.Sprite):
    '''图片精灵类'''
    def __init__(self, display):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       self.display = display
       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.image.load('./images/bosi.png')

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.topleft = (200,200)
       self.last_update = pygame.time.get_ticks()
       self.speed = 20
    
    def draw(self):
        self.display.blit(self.image,self.rect)

    def update(self):
        now = pygame.time.get_ticks()
        print(self.speed)
        if now - self.last_update > 1000:
            if self.speed > 0 :
                self.speed = self.speed - 4
                self.last_update = now
            elif self.speed < 0 :
                self.speed = self.speed + 4
                self.last_update = now
            else :
                self.speed = 20
                self.last_update = now

        if self.rect.y + self.rect.height >= SCREEN_HEIGHT:
            self.speed = -self.speed
        if self.rect.y  <= 0:
            self.speed = -self.speed

        self.rect.y += self.speed
if __name__ == '__main__':
    main()
