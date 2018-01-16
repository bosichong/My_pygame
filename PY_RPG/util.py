#codeing=utf-8
# @Time    : 2017-10-26
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : 游戏制作辅助工具
# @Url     : http://www.17python.com
# @Details : 包括一些游戏素材目录的定制，颜色常量，文字打印工具函数
'''
游戏工具助手类

'''
import os
import pygame, os, sys
import random
from pygame.locals import * #导入游戏常量
#设置常用目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取当前文件上级目录的绝对地址
FONT_DIR = os.path.join(BASE_DIR,'font')
# print(FONT_DIR)

pygame.init()

#颜色常量
BLACK = (0,0,0)
WHITE = (255,255,255,)
RED = (255,0,0)
GREEN  = (0,255,0)
BLUE = (0,0,255)
LGHTGRAY = (192,192,192)
COLOR_Gainsboro = (220, 220, 220,)
COLOR_Snow = (255, 250, 250)
COLOR_AntiqueWhite = (250, 235, 215)
COLOR_PeachPuff =(255, 218, 185)

COLOR_Salmon=(250, 128, 114)
COLOR_LightSkyBlue=(135, 206, 250)
COLOR_Khaki1 =(255, 246, 143)
COLOR_OliveDrab1 =(192, 255, 62)
COLOR_Orchid=(218, 112, 214)
COLOR_Orange2 =(238, 154, 0)

## 有关场景中一些文字打印的常用设置
title_h3 = pygame.font.Font(os.path.join(FONT_DIR,'msyh.ttf'), 28)
title_h2 = pygame.font.Font(os.path.join(FONT_DIR,'msyh.ttf'), 20)
title_plain = pygame.font.Font(os.path.join(FONT_DIR,'msyh.ttf'), 16)


def getFont(size):
    '''获取一个可控制文字大小的字体对象'''
    return pygame.font.Font(os.path.join(FONT_DIR, 'msyh.ttf'), size)

# 使用示例
# print_text(self.screen, title_h2, 30, 340, 'Tetromino俄罗斯方块', color=BLACK)
def print_text(screen,font, x, y, text, color=(255,255,255)):
    '''一个游戏中绘制游戏中文字的函数方法'''
    imgText = font.render(text, True, color,)
    screen.blit(imgText,(x,y))