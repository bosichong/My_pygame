# codeing=utf-8
# @Time    : 2018-01-05
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : “编学编玩”用Pygame编写游戏（8）GreedSnake贪食蛇小游戏
# @Url     : http://www.17python.com/blog/71
# @Details : “编学编玩”用Pygame编写游戏（8）GreedSnake贪食蛇小游戏
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm
###################################
# “编学编玩”用Pygame编写游戏（8）GreedSnake贪食蛇小游戏
###################################

'''
在编写游戏的时候常常不知道从何处入手，如果真的想不出从哪开始写，不妨从游戏的背景开始^o^.

## GreedSnake贪食蛇设计思路

游戏在设计前，可以使用一些做图软件先进行画面设计，至少需要有一个大体样式，对颜色做一些定义，我用fireworks简单的布局了一下，
这样的好处是我们可以通过绘制先计算出来游戏中需要的一些数值，比如蛇身体及背景方格的大小。

![]()


除去游戏的开始和结束画面，整个游戏的核心逻辑很简单：

+ 游戏的背景渲染
+ 蛇的运动
+ 食物的生成
+ 游戏逻辑判断：蛇吃食物后蛇身的变化及游戏是否结束？

当然可能还会有其它不同事之处，但我们这里讨论的是游戏核心的逻辑，那么，我们现在开始用`PY_RPG+pygame`来实现这个简单的小游戏吧。


## 游戏背景渲染

分别创建三个游戏Scene,分别代表游戏的开始、进行、结束三个场景，然后在游戏进行的场景也就是主场景中进行游戏的内容绘制。
对于`GreedSnake`来说，我们需要有一组是浅色网格组成的背景，
对于游戏背景，我单独创建了一个class `GameBackground`,背景绘制的核心逻辑代码如下：

    self.screen.fill((221, 221, 221))
    for i in range(0, 10):
        for j in range(0,10):
             pygame.draw.rect(self.screen, (238,238,238), (i*40, j*40, 40, 40), 1)

在场景中创建对象后，进行渲染，效果如下：

![]()


## 绘制蛇并让它动起来

默认出场的蛇身体有五个节点，我们先在场景中绘制出这条蛇，而且先不必让蛇动起来。为此我创建了一个SnakeBody类，定义蛇的身体上的一节。
这样我们在游戏场景中创建一个list用来表示蛇的身体：

    self.bodys = []#创建一个精灵组，用来放置蛇的身体
    for i in range(0,4):
        self.bodys.append(SnakeBody(self.screen,3*40,(3+i)*40))

![]()

蛇是出来了，不过没有蛇头哇，如果满屏都是蛇身的话，无法分辨哪个是头啦，所以我们得把头部变成其它颜色加以区分，看来还得加入颜色的参数:

        self.bodys = []  # 创建一个精灵组，用来放置蛇的身体
        for i in range(0, 5):
            if i == 0:
                color = RED
            else:
                color = BLACK
            self.bodys.append(SnakeBody(self.screen, 2 * 40, (6 - i) * 40, color))


![]()

这次蛇身与头区分开来了，接下来，我们让蛇动起来，可以根据键盘上的方向键来控制他的移动方向。
关于蛇的移动逻辑：

+ 蛇身是一个list，每次移动list中最后一个蛇节点坐标修改成前一个即可，第一个通过移动方向来判断他的坐标。在`GreedSnake.update()`中，我们通过判断来更新蛇的位置。
+ `GreedSnake.handle_event()`中，监控键盘事件，修改self.direction的属性值，以做到控制蛇的移动方向

具体代码就不贴了，可以参考源文件代码。

## 生成食物与吃掉食物。

关于生成食物的逻辑主要是有一点，不在能生在蛇身上节点的位置，只要食物和蛇身的坐标没有重叠，那么这个位置即可生成食物。
吃掉食物，先判断蛇的移动方向，然后取蛇身list[0]，根据移动的方向模拟增加一个移动位置，如果正好遇食物重叠，那么增加食物的坐标为当前蛇头的坐标即可，然后记得把之前的蛇头颜色换成蛇身的。

## 游戏结束

游戏结束的逻辑只有两点：蛇移动出场景外了，还有就是蛇头碰到蛇身了。

## 游戏暂停

在游戏场景类中加入了一个`pause`的属性，这样通过键盘监控来修改它的布尔值，然后利用这个布尔值在`update`中控制整个游戏的更新，这样就可以达到控制游戏暂停了。

## 总结

教程中只是重点的介绍了游戏的逻辑设计，这样的话即使你换成别的编程言也一样可以制作出来，另外这个游戏的食物生成与游戏结束的判断上有很多方法，你也可以尝试其它方法。








'''

from pygame.sprite import Sprite

from PY_RPG.PygameApp import *
from PY_RPG.util import *  # 导入辅助工具函数及一些常量
from PY_RPG.BorderCrossing import *

######一些游戏常量
RESOLUTION = ((400, 400))  # 游戏场景大小
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
# 蛇及食物的宽高
SW = 38
SH = 38


class MainScnen(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.id = 'mainscnen'
        self.start = True

    def draw(self):
        self.screen.fill((221, 221, 221))
        print_text(self.screen, title_h2, 30, 340, 'GreedSnake', color=BLACK)
        print_text(self.screen, title_plain, 30, 360, '准备游戏，按回车键开始,空格暂停。', color=BLACK)

    def update(self):
        pass

    def handle_event(self, event):
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_RETURN:
                for scene in self.scenes:
                    if scene.id == 'GreedSnake':
                        scene.start = True
                    else:
                        scene.start = False


class GreedSnake(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.id = 'GreedSnake'  # 场景ID
        self.gamebackground = GameBackground(self.screen)  # 游戏场景背景
        self.bodys = []  # 创建一个精灵组，用来放置蛇的身体
        self.direction = DOWN  # 移动方向
        self.replay()  # 游戏开始
        self.pause = False  # 游戏暂停控制

        self.last_update = pygame.time.get_ticks()  # 游戏开始时的计时
        self.bordercrossing = BorderCrossing(-1, -1, 401, 401)

    def replay(self):
        '''初始化游戏开始数据，重新开始游戏'''
        self.bodys.clear()  # 清空蛇list
        # 默认出场的蛇
        for i in range(5):
            if i == 0:
                color = RED
            else:
                color = BLACK
            self.bodys.append(SnakeBody(self.screen, 2 * 40, (6 - i) * 40, color))
        self.food = Food(self.screen, self.bodys)

    def draw(self):
        self.gamebackground.draw()  # 渲染场景中的背景
        ##渲染蛇
        for body in self.bodys:
            body.draw()
        self.food.draw()  # 渲染食物

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 500:
            if not self.pause:  # 如果游戏没有暂停，则继续更新
                # 蛇吃到食物时，添加食物为蛇头,并修改之前蛇头的颜色
                # 蛇的运动，根据方向判断进行坐标修改，对于身体的坐标修改
                if self.direction == 'down':
                    if self.bodys[0].rect.y + 40 == self.food.rect.y and self.bodys[0].rect.x == self.food.rect.x:
                        self.bodys.insert(0, SnakeBody(self.screen, self.food.rect.x, self.food.rect.y, RED))
                        self.bodys[1].color = BLACK
                        self.food = Food(self.screen, self.bodys)

                    for i in reversed(range(len(self.bodys))):
                        self.bodys[i].rect.x = self.bodys[i - 1].rect.x
                        self.bodys[i].rect.y = self.bodys[i - 1].rect.y
                        if i == 1:
                            break
                    self.bodys[0].rect.y += 40
                    self.last_update = now

                if self.direction == 'up':
                    if self.bodys[0].rect.y - 40 == self.food.rect.y and self.bodys[0].rect.x == self.food.rect.x:
                        self.bodys.insert(0, SnakeBody(self.screen, self.food.rect.x, self.food.rect.y, RED))
                        self.bodys[1].color = BLACK
                        self.food = Food(self.screen, self.bodys)

                    for i in reversed(range(len(self.bodys))):
                        self.bodys[i].rect.x = self.bodys[i - 1].rect.x
                        self.bodys[i].rect.y = self.bodys[i - 1].rect.y
                        if i == 1:
                            break
                    self.bodys[0].rect.y -= 40
                    self.last_update = now

                if self.direction == 'left':
                    if self.bodys[0].rect.x - 40 == self.food.rect.x and self.bodys[0].rect.y == self.food.rect.y:
                        self.bodys.insert(0, SnakeBody(self.screen, self.food.rect.x, self.food.rect.y, RED))
                        self.bodys[1].color = BLACK
                        self.food = Food(self.screen, self.bodys)

                    for i in reversed(range(len(self.bodys))):
                        self.bodys[i].rect.x = self.bodys[i - 1].rect.x
                        self.bodys[i].rect.y = self.bodys[i - 1].rect.y
                        if i == 1:
                            break
                    self.bodys[0].rect.x -= 40
                    self.last_update = now

                if self.direction == 'right':
                    if self.bodys[0].rect.x + 40 == self.food.rect.x and self.bodys[0].rect.y == self.food.rect.y:
                        self.bodys.insert(0, SnakeBody(self.screen, self.food.rect.x, self.food.rect.y, RED))
                        self.bodys[1].color = BLACK
                        self.food = Food(self.screen, self.bodys)

                    for i in reversed(range(len(self.bodys))):
                        self.bodys[i].rect.x = self.bodys[i - 1].rect.x
                        self.bodys[i].rect.y = self.bodys[i - 1].rect.y
                        if i == 1:
                            break
                    self.bodys[0].rect.x += 40
                    self.last_update = now
                # 检测蛇头如果超出场景边界，游戏结束。
                self.bordercrossing.sprite = self.bodys[0].rect
                if self.bordercrossing.isBorder():
                    for scene in self.scenes:
                        if scene.id == 'gameover':
                            scene.start = True
                        else:
                            scene.start = False
                for i in range(1, len(self.bodys)):
                    if self.bodys[0].rect.x == self.bodys[i].rect.x and self.bodys[0].rect.y == self.bodys[i].rect.y:
                        for scene in self.scenes:
                            if scene.id == 'gameover':
                                scene.start = True
                            else:
                                scene.start = False

    def handle_event(self, event):
        #控制游戏暂停
        if event.type == KEYUP:
            if event.key == K_SPACE:
                if self.pause:
                    self.pause = False
                elif not self.pause:
                    self.pause = True
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                self.direction = DOWN
            elif event.key == K_UP:
                self.direction = UP
            elif event.key == K_LEFT:
                self.direction = LEFT
            elif event.key == K_RIGHT:
                self.direction = RIGHT


class GameOverScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.id = 'gameover'

    def draw(self):
        self.screen.fill((221, 221, 221))
        print_text(self.screen, title_plain, 50, 190, '游戏结束，按R键重新开始，按ESC键退出', color=BLACK)

    def handle_event(self, event):
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_r:
                for scene in self.scenes:
                    if scene.id == 'GreedSnake':
                        scene.start = True
                        scene.replay()
                    else:
                        scene.start = False


class GameBackground(Sprite):
    '''游戏背景渲染'''

    def __init__(self, screen):
        Sprite.__init__(self)
        self.screen = screen

    def draw(self):
        '''游戏背景渲染'''
        self.screen.fill((221, 221, 221))
        for i in range(0, 10):
            for j in range(0, 10):
                pygame.draw.rect(self.screen, (238, 238, 238), (i * 40, j * 40, 40, 40), 1)


class SnakeBody(Sprite):
    '''
    定义蛇的身体上的一节
    '''

    def __init__(self, screen, x, y, color):
        '''

        :param display: 渲染器
        :param x: 坐标X
        :param y: 坐标Y
        :param color 蛇身颜色
        '''
        Sprite.__init__(self)
        self.x = x
        self.y = y
        self.color = color
        self.screen = screen  # 渲染器
        self.rect = pygame.Rect((self.x, self.y, SW, SH))  # 创建Rect对象

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Food(Sprite):
    '''食物'''

    def __init__(self, screen, list):
        '''

        :param screen: 渲染器
        :param list: 蛇身体节点list
        '''
        Sprite.__init__(self)
        self.screen = screen  # 渲染器
        while True:
            self.x = random.randint(0, 9) * 40
            self.y = random.randint(0, 9) * 40
            isok = False

            for sb in list:
                if self.x == sb.rect.x and self.y == sb.rect.y:
                    isok = True
            # 判断生成的食物坐标没有与当前的蛇身坐标冲突，如果有继续生成。
            if isok:
                continue
            else:
                break
        self.rect = pygame.Rect(self.x, self.y, SW, SH)

    def draw(self):
        pygame.draw.rect(self.screen, GREEN, self.rect)


def main():
    app = GameApp(title='GreedSnake 贪食蛇', resolution=RESOLUTION)  # 创建游戏
    appscreen = app.screen  # 获取渲染器
    app.scenes.append(MainScnen(appscreen))  # 创建游戏菜单
    app.scenes.append(GreedSnake(appscreen))  # 创建游戏内容
    app.scenes.append(GameOverScene(appscreen))  # 游戏结束画面
    app.run()  # 游戏开始


if __name__ == '__main__':
    main()
