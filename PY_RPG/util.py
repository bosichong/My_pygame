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
from pygame.locals import * #导入游戏常量
#设置常用目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取当前文件上级目录的绝对地址
FONT_DIR = os.path.join(BASE_DIR,'font')
# print(FONT_DIR)

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255,)
RED = (255,0,0)
GREEN  = (0,255,0)
BLUE = (0,0,255)
LIGHTGRAY = (192,192,192)

## 有关场景中一些文字打印的常用设置
title_h3 = pygame.font.Font(os.path.join(FONT_DIR,'msyh.ttf'), 28)
title_h2 = pygame.font.Font(os.path.join(FONT_DIR,'msyh.ttf'), 20)
title_plain = pygame.font.Font(os.path.join(FONT_DIR,'msyh.ttf'), 16)
def print_text(screen,font, x, y, text, color=(255,255,255)):
    '''一个游戏中绘制游戏中文字的函数方法'''
    imgText = font.render(text, True, color,)
    screen.blit(imgText,(x,y))