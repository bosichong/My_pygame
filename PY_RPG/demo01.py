#codeing=utf-8
# @Time    : 2017-12-28
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : “编学编玩”用Pygame编写游戏（6）PY_RPG 一个pygame的简单封装。
# @Url     : http://www.17python.com/blog/70
# @Details : “编学编玩”用Pygame编写游戏（6）PY_RPG 一个pygame的简单封装。
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            PyCharm
###################################
# “编学编玩”用Pygame编写游戏（6）PY_RPG 一个pygame的简单封装。
###################################
import random

from PY_RPG.PygameApp import *
from PY_RPG.util import * #导入辅助工具函数及一些常量
from PY_RPG.BorderCrossing import *


class MainScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.id = 'main_scene'
        self.start = True

    def draw(self):
        self.screen.fill((0,0,0))
        print_text(self.screen,title_h3,250,250,'请按回车键切换到下一屏。')

    def update(self):
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
    def __init__(self, screen):
        super().__init__(screen)
        self.id = 'test'
        self.resolution = (640,480)
        self.t_x = 300
        self.t_y = 300
        self.last_update = pygame.time.get_ticks()  # 游戏开始时的计时
        self.ms = Myrs(self.screen,self.resolution)
        self.myimgs = pygame.sprite.Group()
        # 创建一个边界碰撞检对象
        self.bc = BorderCrossing(5, 5, self.resolution[0] - 10, self.resolution[1] - 10)
        for i in range(7):
            self.myimgs.add(MyImgSprite())
    
    def draw(self):
        self.screen.fill((255,0,0))
        pygame.draw.rect(self.screen, (255,255,255), (100,100,100,100),)

        self.ms.draw()
        self.myimgs.draw(self.screen)
        print_text(self.screen, title_h3, self.t_x, self.t_y, 'hello world请按回车继续', )

    def update(self):
        self.ms.update()
        # 红绿边界碰撞检测
        for sp in self.myimgs:
            self.bc.sprite = sp.rect
            if self.bc.isTopBorderCrossing() or self.bc.isBottomBorderCrossing():
                sp.speed_y = -sp.speed_y
            if self.bc.isLeftBorderCrossing() or self.bc.isRightBorderCrossing():
                sp.speed_x = -sp.speed_x

        self.myimgs.update()##检测边界碰撞后更新所有组中球的坐标。
        now = pygame.time.get_ticks()
        if now - self.last_update >1000:
            self.t_x = random.randint(100,400)
            self.t_y = random.randint(100,400)
            self.last_update = now


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
    def __init__(self, screen):
        super().__init__(screen)
        self.id = 'gameover'
    
    def draw(self):
        self.screen.fill((255,0,255))
        print_text(self.screen,title_h3,250,250,'game over!请按ESC退出')

    def handle_event(self,event):
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()




class Myrs(pygame.sprite.Sprite):
    '''形状精灵类'''

    def __init__(self, display,resolution):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.display = display  # 渲染器
        self.rect = pygame.Rect((500, 110, 40, 40))  # 精灵的形状
        self.speed = 3
        self.last_update = pygame.time.get_ticks()  # 游戏开始时的计时
        self.resolution = resolution

    def draw(self):
        '''绘制精灵'''
        pygame.draw.ellipse(self.display, BLACK, self.rect, 1)

    def update(self):
        now = pygame.time.get_ticks()
        # print(self.speed)
        if now - self.last_update > 1000:
            if self.speed > 0:
                self.speed = self.speed - 1
                self.last_update = now
            elif self.speed < 0:
                self.speed = self.speed + 1
                self.last_update = now
            else:
                self.speed = 10
                self.last_update = now

        if self.rect.y + self.rect.height >= self.resolution[1]:
            self.speed = -self.speed
        if self.rect.y <= 0:
            self.speed = -self.speed
        self.rect.y += self.speed

class MyImgSprite(pygame.sprite.Sprite):
    '''图片精灵类'''
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load('.././images/a.png') #导入图片
       self.rect = self.image.get_rect() #返回一个rect对象
       self.rect.topleft = (random.randint(40,590),random.randint(40,430))#设置他的坐标
       self.last_update = pygame.time.get_ticks()#获取当前游戏动行的时间，这是一个整数，不明白可以打印看看
       #移动速度
       self.speed_x = random.randint(1,10)
       self.speed_y = random.randint(1,10)

    def update(self):
        '''更新自己的坐标，如果放在精灵组中，调用组的update()函数，会自动调用本函数'''
        now = pygame.time.get_ticks()
        if now - self.last_update >1:#通过这个时间差来做一些动画
            # self.rect.topleft = (random.randint(0,600),random.randint(0,440))#随机变化位置
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.last_update = now

def main():
    app = GameApp()#创建游戏
    appscreen = app.screen#获取渲染器
    app.scenes.append(MainScene(appscreen))#创建游戏菜单
    app.scenes.append(TestScene(appscreen))#创建游戏内容
    app.scenes.append(GameOverScene(appscreen))#游戏结束画面
    app.run() #游戏开始
if __name__ == '__main__':
    main()
