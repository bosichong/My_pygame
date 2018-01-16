# codeing=utf-8
# @Time    : 2018-01-13
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : “编学编玩”用Pygame编写游戏（10）pygame实现一个黑客帝国矩阵(Matrix)
# @Url     : http://www.17python.com/blog/77
# @Details : “编学编玩”用Pygame编写游戏（10）pygame实现一个黑客帝国矩阵(Matrix)
# @Other   : OS X 10.11.6
#            Python 3.6.1
#            PyCharm
###################################
# “编学编玩”用Pygame编写游戏（10）pygame实现一个黑客帝国矩阵(Matrix)
###################################

'''

当年电脑黑客帝国中下落的字符矩阵大家应该都会有很深的印象，即使今天重温一遍这部经典之作，仍然会觉这种电脑特效做的真帅啊，什么时候我也能做出这种效果来？
想做就做，既然人家能做出来我们也能，好吧，先上图，最近不是流行什么开局一张图么？

## Matrix的构思

我们把Matrix设计成矩阵下落的字符数组，整矩阵中有几十或上百条Matrix在下落，你可以想像一条条数组从天而降。。。。Matrix就是这其中的一条数组。
Matrix中有很多属性，用来控制自己的字符组成，下落速度，颜色深浅，间隔距离等,通过这些，控制自己在场景中下落，当然你的参数控制的越详细，可变数越多。

## Matrix代码编写调试过程

刚开始的时候总觉得满屏的字符，应该从何处下手呢？，不妨先从场景中打印一组字符开始吧，新建一个场景，然后创建一个Matrix对象，在场景中打印出来，
当然这组字符是如何生成的呢？还要随机生成，好的，如果你想到这些了，那么你就去动手实践，随数机，字符，添加到数组。

    c = random.randint(33, 127)
    chr(c)

对，字符就是这样生成的，有关char的基础理论，大家不太了解的可以自己去复习一下。把随机生成的字符在场景中竖排打印出来，你就成功了一半了。

## 让Matrix动起来

场景中已经打印出来一组Matrix了，接下来我们就可以在Matrix.update()中控制修改他的下落，这里我把Matrix设置成了一个比较自由的类，生成的对象自控度还是很高的。
add()方法就是生成一个完整的自身，然后通过draw(）方法在场景中渲染，update()中判断整组字符下落超屏外，即重新生成一组新的字符串继续下落，即可达成循环动画了。

## Matrix代码缩写总结

感觉Matrix的编写是一次对编程基础的复习，其中涉及了大量的编程基础操作，是Python及Pygame学习中不可多得的教材，最主要是最终结果很帅哈。

本文源码下载

请git clone My_pygame下所有代码，以免造成游戏跑不起来的情况。 本例源文件：PY_RPG.demo.Matrix.py

'''


from pygame.sprite import Sprite

from PY_RPG.PygameApp import *
from PY_RPG.util import *  # 导入辅助工具函数及一些常量

RESOLUTION = ((640, 480))  # 游戏场景大小


class MatrixScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.id = "Matrix"
        self.start = True
        self.slist = list()
        for i in range(100):
            self.slist.append(Matrix(self.screen))
            print(self.slist[i].x)

    def draw(self):
        self.screen.fill(BLACK)  # 背景色
        for s in self.slist:
            s.draw()

    def update(self):
        for s in self.slist:
            s.update()

    def handle_event(self, event):
        # 控制游戏暂停
        if event.type == KEYUP:
            if event.key == K_SPACE:
                if self.pause:
                    self.pause = False
                elif not self.pause:
                    self.pause = True


class Matrix(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.strlist = list() # 一组矩阵下落字符串
        self.last_update = pygame.time.get_ticks()  # 获取一个游戏中开始时间点
        #定义一些下落矩阵字符数组中的数值
        self.downspeed = 4 #下落速度
        self.down_y =500#起始坐标
        self.cs = 25 #下落矩阵字符数个数设定
        self.y = 0
        self.x =0
        self.speed=0#速度
        self.color = 255
        self.fontsize = 15#字符大小


        self.strlist = list()
        self.add()
        # print(self.strlist)

    def add(self):
        '''重新生成一个list'''
        self.y = -(random.randint(self.down_y, self.down_y * 2))
        self.x = random.randint(0, RESOLUTION[0])
        self.speed = random.randint(self.downspeed, self.downspeed*3)
        self.fontsize = random.randint(10,20)
        self.tt = getFont(self.fontsize)
        #每组下落字符的数设置
        for i in range(self.cs,self.cs*2):
            c = random.randint(33, 127)
            if i >25:
                self.color -=10
            #数组中包括了：字符内容，起始坐标y，递减的颜色，
            self.strlist.append([chr(c),self.y,self.color])
            self.y += 20#设置起始坐标
        self.color = 255

    def draw(self):
        for i in range(len(self.strlist)):
            print_text(self.screen, self.tt, self.x, self.strlist[i][1], self.strlist[i][0], color=Color(0,self.strlist[i][2],0))

    def update(self):
        now = pygame.time.get_ticks()
        if (now - self.last_update) > self.speed:
            for i in range(len(self.strlist)):
                self.strlist[i][1]+=self.speed
            self.last_update = now

        if self.strlist[0][1] > RESOLUTION[1]:
            #当前矩阵下落超出屏幕范围Y之后，重新生成一个下落的矩阵字符串
            self.strlist.clear()#清空list
            self.add()#重新生成一组新的矩阵字符


def main():
    app = GameApp(title='Matrix', resolution=RESOLUTION)  # 创建游戏
    appscreen = app.screen  # 获取渲染器
    app.scenes.append(MatrixScene(appscreen))
    app.run()


if __name__ == '__main__':
    main()
