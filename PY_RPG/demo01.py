#codeing=utf-8
# @Time    : 2017-10-26
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : “编学编玩”用Pygame编写游戏（5）PY_RPG 一个pygame的简单封装。
# @Url     : http://www.17python.com/blog/49
# @Details : “编学编玩”用Pygame编写游戏（5）PY_RPG 一个pygame的简单封装。
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# “编学编玩”用Pygame编写游戏（5）PY_RPG 一个pygame的简单封装。
###################################
import pygame, os, sys
from pygame.locals import * #导入游戏常量

from PygameApp import Scene, GameApp
from util import * #导入辅助工具函数及一些常量


class MainScene(Scene):
    def __init__(self):
        super().__init__()
        self.id = 'main_scene'
        self.start = True

    def draw(self):
        self.screen.fill((0,0,0))
        print_text(self.screen,title_h3,250,250,'请按回车键切换到下一屏。')
    def updae(self):
        pass

    def handle_event(self,event):
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_RETURN:
                for scene in self.scenes:
                    if scene.id == 'test':
                        scene.start = True
                    else:
                        scene.start = False 
class TestScene(Scene):
    def __init__(self,):
        super().__init__()
        self.id = 'test'
    
    def draw(self):
        self.screen.fill((255,0,0))
        pygame.draw.rect(self.screen, (255,255,255), (100,100,100,100),)
        print_text(self.screen,title_h3,300,300,'hello world请按回车继续',)
        
    def updae(self):
        pass
    def handle_event(self,event):
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_RETURN:
                for scene in self.scenes:
                    if scene.id == 'gameover':
                        scene.start = True
                    else:
                        scene.start = False 
class GameOverScene(Scene):
    def __init__(self):
        super().__init__()
        self.id = 'gameover'
    
    def draw(self):
        self.screen.fill((255,0,255))
        print_text(self.screen,title_h3,250,250,'game over!请按ESC退出')

    def handle_event(self,event):
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
def main():
    app = GameApp("gameapp test",(640,480),24)#创建游戏
    app.scenes.append(MainScene())#创建游戏菜单
    app.scenes.append(TestScene())#创建游戏内容
    app.scenes.append(GameOverScene())#游戏结束画面
    app.run() #游戏开始
if __name__ == '__main__':
    main()
