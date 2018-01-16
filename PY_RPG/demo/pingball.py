#codeing=utf-8
# @Time    : 2017-12-29
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : “编学编玩”用Pygame编写游戏（7）Pingball弹球小游戏
# @Url     : http://www.17python.com/blog/71
# @Details : “编学编玩”用Pygame编写游戏（7）Pingball弹球小游戏
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm
###################################
# “编学编玩”用Pygame编写游戏（7）Pingball弹球小游戏
###################################

'''
以前学java的时候用java做了一个简单弹球小游戏，觉得还是蛮有意思的，这次用`pygame`重写一下试试，以前觉得游戏编程很简单，可能是考虑的太简单了，
游戏的编写是步步为营，逻辑紧扣，错一点游戏都无法运行的，所以学习用面向对象方式编写游戏，是对python编程学习的强化练习，大家可以多试试。

## Pingball游戏的设计

游戏很小，场景中的精灵有两个：球拍和一个小球。游戏的顺序包括：游戏开始画面，游戏主场景，游戏结束画面。
游戏逻辑：判断小球的Y坐标低于球拍的Y坐标值即为游戏结束，球拍和小球都有自己的运动逻辑。这么简单的游戏我们从哪里入手呢？
肯定是先创建一个游戏窗口啦：）

## 设定一些游戏的基本数据

游戏包括的主要数据有：

+ 游戏场景（宽+高）
+ 球拍，（宽，高，位置，移动速度）
+ 小球，（宽，高，位置，移动速度）
+ 游戏逻辑，判断游戏是否结束，暂停游戏，重新开始游戏，及一些文字的打印。

有了这些构思，我们一样一样的通过我们之前封装的PY_RPG及pygame提供的一些功能来实现这个小游戏。

## 创建场景

一共有三个场景，分别为游戏开始画面`MainScene`游戏主场景`Pingball`游戏结束画面`GameOverScene`

先创建三个场景的类，通过继承`PY_RPG.Scene`，会很方便的创建出三个类，分别修改三个场景的一些参数，然后设置键盘判断，进行游戏场景的跳转。
因为`Scene`中的三个方法分工非常明确，我们可以很好的控制游戏场景，这样我们可以先把三个场景制作出来，然后进行测试，虽然游戏主场景没有任何精灵，
但游戏场景整体是可以切换的。

## 创建球拍与球

`Racket`和`Ball`分别进行一些属性设置，其中`Racket`相对来说比较简单，只需要左右移动，做一个场景边界判断即可。
`Ball`的属性多了一些，需要有移动速度，需要通过`update`方法进移动的控制。

## 游戏逻辑判断

在游戏主场景中的`Pingball.update`方法中进行了一些游戏逻辑判断，包括：球遇到边界反弹，小球遇到球拍反弹后增加速度，和游戏结束的判断。
这个方法中还需要添加球与球拍自己的`update`方法,用来更新自己的坐标变化。

## 游戏结束

游戏结束后，还可以通过按键重新开始，在`Pingball`中有个`replay`的函数，是用来控制重新开始后球体的位置.

## 功能扩展

这个弹球游戏只完成了最最最基本的功能，扩展性很强，比如添加关卡，打印得分，增加一些特效，只要你想修改，弹球也一样可以玩的很嗨。
'''



import random

from PY_RPG.PygameApp import *
from PY_RPG.util import * #导入辅助工具函数及一些常量
from PY_RPG.BorderCrossing import *

######一些游戏常量

RESOLUTION = ((300,400))#游戏场景大小

class MainScene(Scene):
    '''游戏开始画面，按回车后游戏开始'''
    def __init__(self, screen):
        super().__init__(screen)
        self.id = 'main_scene'
        self.start = True

    def draw(self):
        self.screen.fill((0,0,0))
        print_text(self.screen,title_h2,30,340,'Pinball')
        print_text(self.screen, title_plain, 30, 360, '准备游戏，按回车键开始')

    def update(self):
        pass

    def handle_event(self,event):
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_RETURN:
                for scene in self.scenes:
                    if scene.id == 'pingball':
                        scene.start = True
                    else:
                        scene.start = False

class Pingball(Scene):
    '''游戏主场景，左右移动方块，遇一小球反弹'''
    def __init__(self,screen):
        super().__init__(screen)
        self.id = 'pingball'#片段id
        self.racket = Racket(self.screen)#定义球拍
        self.ball = Ball(self.screen)
        # 创建一个边界碰撞检对象
        self.bc = BorderCrossing(5, 5, RESOLUTION[0] - 10, RESOLUTION[1] - 10)

    def replay(self):
        '''游戏重新开始'''
        self.ball.rect.x = random.randint(100,200)
        self.ball.rect.y = random.randint(100,200)


    def draw(self):
        self.screen.fill((0, 0, 0))
        self.racket.draw()
        self.ball.draw()

    def update(self):
        self.racket.update()#更新球拍
        self.ball.update()#更新球
        self.bc.sprite = self.ball.rect#传递需要检测的对象
        ######################
        #检测球碰到边界时反弹
        if self.bc.isTopBorderCrossing() or self.bc.isBottomBorderCrossing():
            self.ball.speed_y = -self.ball.speed_y
        if self.bc.isLeftBorderCrossing() or self.bc.isRightBorderCrossing():
            self.ball.speed_x = -self.ball.speed_x
        ######################
        # 检测球与球拍的碰撞
        if (pygame.sprite.collide_rect(self.ball,self.racket)) :
            #小球反弹
            self.ball.speed_y = -self.ball.speed_y
            #控制每弹一次，速度增加2
            if self.ball.speed_y > 0:
                self.ball.speed_y += 2
            elif self.ball.speed_y <0:
                self.ball.speed_y -= 2
        # 检测球超出球拍，游戏结束判断。
        if self.ball.rect.y + self.ball.rect.height > self.racket.rect.y+10 :
            for scene in self.scenes:
                if scene.id == 'gameover':
                    scene.start = True
                else:
                    scene.start = False


    def handle_event(self, event):

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.racket.rect.left -= 5
            elif event.key == K_RIGHT:
                self.racket.rect.right += 5

class GameOverScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.id = 'gameover'

    def draw(self):
        self.screen.fill(BLACK)
        print_text(self.screen, title_plain, 2, 190, '游戏结束，按R键重新开始，按ESC键退出')

    def handle_event(self, event):
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_r:
                for scene in self.scenes:
                    if scene.id == 'pingball':
                        scene.start = True
                        scene.replay()
                    else:
                        scene.start = False

class Racket(pygame.sprite.Sprite):
    '''定义球拍'''
    def __init__(self, display):
        pygame.sprite.Sprite.__init__(self)
        self.display = display  # 渲染器
        self.rect = pygame.Rect((200, 340, 60, 20))#创建Rect对象
        self.speed = 3
        self.last_update = pygame.time.get_ticks()  # 游戏开始时的计时

    def draw(self):
        pygame.draw.rect(self.display, LGHTGRAY, self.rect, )

    def update(self):
        if self.rect.left <= 2 :
            self.rect.left = 2
        if self.rect.left >= RESOLUTION[0]-self.rect.width -2:
            self.rect.left = RESOLUTION[0]-self.rect.width - 2

class Ball(pygame.sprite.Sprite):
    def __init__(self,display):
        pygame.sprite.Sprite.__init__(self)
        self.display = display  # 渲染器
        self.rect = pygame.Rect((random.randint(100,200),random.randint(100,200),20,20))#创建球体
        # 移动速度
        self.speed_x = random.randint(3, 5)
        self.speed_y = random.randint(3, 5)
        self.last_update = pygame.time.get_ticks()  # 游戏开始时的计时

    def draw(self):
        pygame.draw.ellipse(self.display, LGHTGRAY, self.rect)

    def update(self):
        '''更新自己的坐标，如果放在精灵组中，调用组的update()函数，会自动调用本函数'''
        now = pygame.time.get_ticks()
        if now - self.last_update >1:#通过这个时间差来做一些动画
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.last_update = now


def main():

    app = GameApp(title='Pingball Game', resolution=RESOLUTION)#创建游戏
    appscreen = app.screen#获取渲染器
    app.scenes.append(MainScene(appscreen))#创建游戏菜单
    app.scenes.append(Pingball(appscreen))#创建游戏内容
    app.scenes.append(GameOverScene(appscreen))#游戏结束画面
    app.run() #游戏开始

if __name__ == '__main__':
    main()

