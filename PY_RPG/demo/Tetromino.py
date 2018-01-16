# codeing=utf-8
# @Time    : 2018-01-13
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : # “编学编玩”用Pygame编写游戏（9）Tetromino俄罗斯方块游戏
# @Url     : http://www.17python.com/blog/71
# @Details : # “编学编玩”用Pygame编写游戏（9）Tetromino俄罗斯方块游戏
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm
###################################
# “编学编玩”用Pygame编写游戏（9）Tetromino俄罗斯方块游戏
###################################

'''

记得以前用java写过一个tetromino,这么多年了，回头想想，竟然什么都不记得了。。。愿码界的神原谅我的过错，如何用Python来写一个俄罗斯方块游戏呢？
如果你感兴趣， Follow me, please.

无图无真相，先上图：

![]()
![]()
![]()

## Tetromino游戏构思

很多时候，我们编写一个游戏或是软件总是不知道从何入下手没有头绪，感觉思绪一阵乱麻，你没有？确定没有这种感觉吗？好吧，大神求带！！！

Tetromino如果我们从逻辑上拆分，我这里能想到三点：

+ 一个长方形的场景
+ 下落的方块
+ 游戏中的逻辑

当然，你可以更详细的分出更多的逻辑，但我只想把这个游戏简化，这样我们可以有一处可以开始的入手的地方，其实每次编写游戏的时候，你有没有那种感觉？觉得自己就是上帝是神。
游戏就是世界，你可以在游戏里创造出一切，当然你得有这个能力，好吧，万能的神，我们何不先创建一个游戏窗口，绘制好游戏中的场景先？

**友情提示，本系列教程已经进入实例开发，如果你对Pygame,PY_RPG框架不太了解的话，请翻看以前的教程**

## Tetromino中的游戏板

Tetromino类是本游戏的重点及主要场景，除了游戏的开始与结束画面以外，所有的游戏逻辑都集中在这个class中。
首先我们定义一下游戏场景中的尺寸，比如小方块的尺寸，这里我定义为20象素，场景中的游戏板是一个12X22的长方形，
其中上下左右各留出一行或列做为边界，其它10X20做为游戏场景，这样的我们可以先定义出常量，以后就可以方便修改游戏场景属性。
设置Tetromino类中的self.start = True，这样方便调试游戏。

## 绘制board游戏板

        self.board = [[0 for col in range(BOARDHEIGHT)] for row in range(BOARDWIDTH)]  # 场景中的board

通过上边列表推导，我们创建一个二维的list，用来存放游戏场景中的方块数据，方块有三种状态：0无方块，1被占用的方块，2围墙方块。
在游戏开始时，我们初始化这个二维list，然后，在再游戏中修改这个list即可表示出游戏中的场景状态。
有这个list，我们在draw()方法中通过循环迭代绘制游戏的背景色及游戏场景中的方块。当然，现在只能绘制出外围的方块。

## 下落的方块

下落的方块用多维数组的表达方式有很多种，数据结构直接影响到你在游戏中数据调用的方法，我这里采用了一个字典组合多维数组进行表示。
具体的数值及属性你可以在Piece.shapes中找到，Piece表示一组4X4由0和1组成的下落的方块，当新建对象的时候会随机初始化其形状。
Tetromino类中有两个Piece的属性对象，一个用来放置准备下落的方块，一个为当前正在下落的方块，有了方块我们就可以让他在场景中下落了。
这样，我们场景中有了下落的方块了，你可以看到它在慢慢的下落，到些游戏场景中的主要元素我们已经搭建完毕，余下的就是逻辑判断了。

##游戏中的逻辑

这个游戏的核心逻辑个人觉得就是：**判断当前下落方块所处的位置是否合法**，稍后你就会知道，很多逻辑都依靠这个逻辑来进行判断，既然他这么重要，
我们来看看怎么实现它。想想整个游戏场景就是一个二组的数组，那些下落的方块，变动的坐标，你首先要在脑海里形成这种数据模型，至少得有个大概，
一个下落的方块中有16个小方块，通过循环迭代的方法我们就能获得到他们的坐标，并可以兑换成场景中board的索引，如果我们可以比较这两个值，
就可以得到当前下落方块的位置是否合法，这个合法包括：下落到底，碰到已有的方块，遇到边界等。了解了原理，我们就来实现吧
伪代码：


        for a in range(w):
            for b in range(h):
                if (shapes[type][direction][b][a] == 1 and board[x + b][
                    y + a] == 2) or (
                        shapes[type][direction][b][a] == 1 and board[x + b][
                    y + a] == 1):
                    return 0
        return 1


原理：利用当前下落方块中有方块那部分的坐标与索引出来的board的索引值是否有冲突来进行判断，当然在判断时需要超前一步，不然当前已经冲突的话就晚了。
有了这个方法,我们就可以做一些其它判断，比如方块是否到底，添加方块到场景，方块是否可以旋转，消层等。
实现了这些逻辑的判断，我们大体上就完成了游戏的编写，细节就在于你的探索了，加油！


'''




import pygame
from pygame.sprite import Sprite

from PY_RPG.PygameApp import *
from PY_RPG.util import *  # 导入辅助工具函数及一些常量

###############

BOXSIZE = 20  # 游戏板上每个方块的尺寸
BOARDWIDTH = 12  # 游戏板 width 个数
BOARDHEIGHT = 22  # 游戏板 height 个数
RESOLUTION = ((BOXSIZE * 32, BOXSIZE * 24))  # 游戏场景大小


class MainScnen(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.id = 'mainscnen'
        self.start = True
        self.ps = list()
        for i in range(random.randint(10,30)):
            self.ps.append(Piece(self.screen))
        for p in self.ps:
            p.x = random.randint(-5,15)
            p.y = random.randint(1,15)

    def draw(self):
        self.screen.fill(COLOR_Snow)
        for p in self.ps:
            p.draw()
        print_text(self.screen, title_h3, 30, 340, 'Tetromino俄罗斯方块', color= COLOR_Orange2)
        print_text(self.screen, title_plain, 30, 380, '准备游戏，按回车键开始,空格暂停,方向上旋转，左右下控制移动。',
                   color=LGHTGRAY)

    def update(self):
        pass

    def handle_event(self, event):
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_RETURN:
                for scene in self.scenes:
                    if scene.id == 'Tetromino':
                        scene.start = True
                    else:
                        scene.start = False


class Tetromino(Scene):
    '''Tetromino俄罗斯方块游戏游戏主场景'''

    def __init__(self, screen):
        super().__init__(screen)
        # self.start = True
        self.id = 'Tetromino'
        self.last_update = pygame.time.get_ticks()
        self.next = Piece(self.screen)  # 创建下一块需要下落的方块，显示在场景的右边
        self.offset_x = 11  # 展示下一块下落方块X坐标的偏移量
        self.offset_y = 2  # 展示下一块下落方块Y坐标的偏移量
        self.next.x += self.offset_x
        self.next.y += self.offset_y
        self.piece = None
        if self.piece == None:
            self.piece = Piece(self.screen)
        self.board = [[0 for col in range(BOARDHEIGHT)] for row in range(BOARDWIDTH)]  # 场景中的board
        self.score = 0  # 初始化分数
        self.hscore =0
        self.replay()  # 初始化游戏场景中的board
        self.fps = 500 #刷新频率，通过游戏得分来控制这个速度
        self.tempscore =0

    def replay(self):
        '''初始化或重新开始游戏'''
        for i in range(BOARDWIDTH):
            for j in range(BOARDHEIGHT):
                self.board[i][j] = [0,'']

        for i in range(BOARDWIDTH):
            self.board[i][0] = [2,'']
            self.board[i][BOARDHEIGHT - 1] = [2,'']

        for j in range(BOARDHEIGHT):
            self.board[0][j] = [2,'']
            self.board[BOARDWIDTH - 1][j] = [2,'']
        #记录历史最高分
        if self.score > self.hscore:
            self.hscore = self.score
        self.score = 0
        self.fps = 500
        self.tempscore = self.score


    def blow(self, x, y):
        '''判断方块位置是否合法，在所有的方法中些方法最为重要，应该是些游戏的核心逻辑'''
        for a in range(self.piece.template_w):
            for b in range(self.piece.template_h):
                if (self.piece.shapes[self.piece.type][self.piece.direction][b][a] == 1 and self.board[x + b][
                    y + a][0] == 2) or (
                        self.piece.shapes[self.piece.type][self.piece.direction][b][a] == 1 and self.board[x + b][
                    y + a][0] == 1):
                    return 0
        return 1

    def newpiece(self):
        '''切换或生成新的下落方块'''
        self.next.x -= self.offset_x
        self.next.y -= self.offset_y
        self.piece = self.next
        self.next = Piece(self.screen)
        self.next.x += self.offset_x
        self.next.y += self.offset_y

    def isturn(self):
        '''方块是否可以旋转？'''
        temp = self.piece.direction  # 存放当前状态
        if self.piece.direction >= len(self.piece.shapes[self.piece.type]) - 1:
            self.piece.direction = 0  # 超过旋转次数，归0
            self.turn(temp)
        else:
            self.piece.direction += 1
            self.turn(temp)

    def turn(self, temp):
        '''方块旋转操作'''
        if self.blow(self.piece.x, self.piece.y) == 1:  # 如果不可以，不转
            pass
        elif self.blow(self.piece.x, self.piece.y) == 0:
            self.piece.direction = temp
            self.draw()

    def isgameover(self):
        '''判断游戏是否结束'''
        if self.blow(self.piece.x, self.piece.y) == 0:
            for scene in self.scenes:
                if scene.id == 'gameover':
                    scene.start = True
                else:
                    scene.start = False

    def add(self):
        '''添加方块到地图中'''
        for i in range(self.piece.template_w):
            for j in range(self.piece.template_h):
                if self.piece.shapes[self.piece.type][self.piece.direction][i][j] == 1:
                    self.board[self.piece.x + i][self.piece.y + j][0] = \
                        self.piece.shapes[self.piece.type][self.piece.direction][i][j]
                    self.board[self.piece.x + i][self.piece.y + j][1] = self.piece.color



    def delline(self):
        '''消行'''
        c = 0
        for b in range(BOARDHEIGHT):
            for a in range(BOARDWIDTH):
                if self.board[a][b][0] == 1:
                    c += 1
                    if c == BOARDWIDTH - 2:
                        self.score += 10
                        for d in range(b, -1, -1):
                            for e in range(BOARDWIDTH):
                                if self.board[e][d - 1][0] != 2:  # 只要不是外围的墙
                                    self.board[e][d][0] = self.board[e][d - 1][0]  # 都往下落一层
            c = 0  # 清空计数器

    def changelevel(self):
        '''修改游戏速度'''

        if self.score - self.tempscore >=50:
            self.fps -= 100
            self.tempscore = self.score

    def draw(self):
        self.screen.fill(COLOR_Snow)#背景色

        self.piece.draw()  # 绘制游戏中下落的方块
        self.next.draw()  # 绘制下一次准备使用的方块
        # 绘制当前得分
        print_text(self.screen, title_h2, 455, 200, '当前得分：{}'.format(self.score), color=COLOR_Orchid)
        # 历史最高分
        print_text(self.screen, title_h2, 455, 230, '最高得分：{}'.format(self.hscore), color=RED)
        # 历史最高分
        print_text(self.screen, title_h2, 30, 50, '游戏难度：{}'.format(int(abs(self.fps/100-5))), color=RED)
        # 下一个方块
        print_text(self.screen, title_h2, 455, 50, '下一个方块：', color=COLOR_LightSkyBlue)

        # 画四周的墙和方块
        for i in range(BOARDWIDTH):
            for j in range(BOARDHEIGHT):
                if self.board[i][j][0] == 2:  # 画墙
                    pygame.draw.rect(self.screen, COLOR_PeachPuff,
                                     (int(((RESOLUTION[0] - BOARDWIDTH * BOXSIZE) / 2) + i * BOXSIZE),
                                      int((RESOLUTION[1] - BOARDHEIGHT * BOXSIZE) / 2) + j * BOXSIZE, BOXSIZE, BOXSIZE))
                if self.board[i][j][0] == 1:  # 画已经在板中固定的方块
                    pygame.draw.rect(self.screen, self.board[i][j][1],
                                     (int(((RESOLUTION[0] - BOARDWIDTH * BOXSIZE) / 2) + i * BOXSIZE),
                                      int((RESOLUTION[1] - BOARDHEIGHT * BOXSIZE) / 2) + j * BOXSIZE, BOXSIZE, BOXSIZE))

    def update(self):
        # 先判断游戏是否暂停，然后再进行游戏数据更新
        if not self.pause:
            self.isgameover()  # 判断游戏是否结束
            if self.blow(self.piece.x, self.piece.y + 1) == 1:
                now = pygame.time.get_ticks()
                if (now - self.last_update) > self.fps:
                    self.piece.y += 1
                    self.last_update = now

            else:

                self.add()
                self.delline()
                self.newpiece()
                self.changelevel()
                self.board_color1 = random.choice((COLOR_Salmon, COLOR_LightSkyBlue, COLOR_Khaki1, COLOR_OliveDrab1,
                                                   COLOR_Orchid, COLOR_Orange2))


    def handle_event(self, event):
        # 控制游戏暂停
        if event.type == KEYUP:
            if event.key == K_SPACE:
                if self.pause:
                    self.pause = False
                elif not self.pause:
                    self.pause = True

        if event.type == KEYDOWN:
            if event.key == K_UP:  # 按上键转动方块
                # if self.piece.direction >= len(self.piece.shapes[self.piece.type]) - 1:
                #     self.piece.direction = 0
                # else:
                #     self.piece.direction += 1
                self.isturn()

            if event.key == K_LEFT:  # 方块向左移动
                if self.blow(self.piece.x - 1, self.piece.y) == 1:
                    self.piece.x -= 1
                else:
                    self.piece.x -= 0
            if event.key == K_RIGHT:
                if self.blow(self.piece.x + 1, self.piece.y) == 1:
                    self.piece.x += 1
                else:
                    self.piece.x += 0
            if event.key == K_DOWN:
                if self.piece.y + self.piece.template_h <= BOARDHEIGHT - 1:
                    self.piece.y += 1
                else:
                    self.piece.y += 0


class GameOverScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.id = 'gameover'

    def draw(self):
        self.screen.fill(COLOR_Snow)
        print_text(self.screen, title_h3, 75, 200, '游戏结束，按R键重新开始，按ESC键退出', color=COLOR_Orange2)

    def handle_event(self, event):
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_r:
                for scene in self.scenes:
                    if scene.id == 'Tetromino':
                        scene.start = True
                        scene.replay()
                    else:
                        scene.start = False


class Piece(Sprite):
    '''游戏板上下落的砖块'''

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        # 各类下落方块形状。0为空白，1为占用
        # shapes 用来存放各种图形
        self.shapes = {
            'S':  # 倒Z 形状 有四种形态
                [

                    [
                        [0, 1, 1, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [1, 0, 0, 0],
                        [1, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0],
                    ],

                ],
            'Z':
                [
                    [
                        [1, 1, 0, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [0, 1, 0, 0],
                        [1, 1, 0, 0],
                        [1, 0, 0, 0],
                        [0, 0, 0, 0],
                    ],
                ],
            'I':
                [
                    [
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],

                    ],
                    [
                        [0, 0, 0, 0],
                        [1, 1, 1, 1],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],

                    ],

                ],
            'T':
                [
                    [
                        [0, 1, 0, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],

                    ],
                    [
                        [0, 1, 0, 0],
                        [1, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0],

                    ],
                    [
                        [1, 1, 1, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],

                    ],
                    [
                        [0, 1, 0, 0],
                        [0, 1, 1, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0],

                    ],
                ],
            'J':
                [
                    [
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0],

                    ],
                    [
                        [1, 0, 0, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],

                    ],
                    [
                        [1, 1, 0, 0],
                        [1, 0, 0, 0],
                        [1, 0, 0, 0],
                        [0, 0, 0, 0],
                    ],
                    [
                        [1, 1, 1, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                    ],
                ],
            'L':
                [
                    [
                        [1, 0, 0, 0],
                        [1, 0, 0, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0],

                    ],
                    [
                        [1, 1, 1, 0],
                        [1, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],

                    ],
                    [
                        [1, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0],

                    ],
                    [
                        [0, 0, 1, 0],
                        [1, 1, 1, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],

                    ],
                ],
            'O':
                [
                    [
                        [1, 1, 0, 0],
                        [1, 1, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                    ],
                ],

        }
        self.template_w = 4  # piece 的宽度
        self.template_h = 4  # piece 的高度
        # piece 下落块在游戏板上的的坐标，
        self.x = 4
        self.y = 2
        # self.type = random.choice(('I','O'))  # 初始化形状测试使用
        self.type = random.choice(('O', 'L', 'I', 'S', 'Z', 'J', 'T'))  # 初始化形状
        self.direction = random.randint(0, len(self.shapes[self.type]) - 1)  # 初始化下落块的方向
        self.color = random.choice((COLOR_Salmon, COLOR_LightSkyBlue, COLOR_Khaki1,
                                    COLOR_OliveDrab1,COLOR_Orchid,COLOR_Orange2))  # 初始化颜色
        self.last_update = pygame.time.get_ticks()

    def draw(self):
        for i in range(self.template_w):
            for j in range(self.template_h):
                if self.shapes[self.type][self.direction][i][j] == 1:
                    pygame.draw.rect(self.screen, self.color,
                                     (int((RESOLUTION[0] - (BOARDWIDTH) * BOXSIZE) / 2) + (self.x + i) * BOXSIZE,
                                      int((RESOLUTION[1] - (BOARDHEIGHT) * BOXSIZE) / 2) + (self.y + j) * BOXSIZE,
                                      BOXSIZE,
                                      BOXSIZE))


def main():
    app = GameApp(title='Tetromino俄罗斯方块', resolution=RESOLUTION)  # 创建游戏
    appscreen = app.screen  # 获取渲染器
    app.scenes.append(MainScnen(appscreen))
    app.scenes.append(Tetromino(appscreen))
    app.scenes.append((GameOverScene(appscreen)))
    app.run()


if __name__ == '__main__':
    main()
