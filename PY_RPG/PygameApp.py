#codeing=utf-8
# @Time    : 2017-12-28
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : “编学编玩”用Pygame编写游戏（6）PY_RPG 一个pygame的简单封装。
# @Url     : http://www.17python.com/blog/49
# @Details : “编学编玩”用Pygame编写游戏（6）PY_RPG 一个pygame的简单封装。
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            PyCharm
###################################
# “编学编玩”用Pygame编写游戏（6）PY_RPG 一个pygame的简单封装。
###################################

'''
## 为什么要封装？

pygame写起游戏都是函数式编写，对于一些简单的小游戏或许可以应付，随着游戏内容的增加，我们不可能只在一个.py文件中写下所有的游戏代码，
这个时候，我们应该考虑对游戏中组件及对象进行封装，用面向对象的方式来进行游戏代码的编写。

## 一些具体的封装内容

游戏中的关键词，假设游戏没有条件判断，那么游戏从头运行到尾就是一部电影。
这样的话，我们定义一些游戏的基本对象：
渲染器（APP）--只负责渲染游戏场景中存在的游戏片段，属性有：一个游戏片段容器及一些游戏窗口常用设置，并初始化游戏设置。
游戏片段(scene)--可能是游戏中的一个片段，一个情节，一节过场，片头，片尾等，游戏片段中包含一个开关属性，用来控制是否可以渲染此游戏片段。
游戏逻辑判断器--游戏中的裁判，负责判断修改游戏中的执行条件。
精灵--游戏中的角色，他可以是游戏中的场景，主角，配角，怪物，子弹，文字对白。
工具类包括：场景中文字渲染工具，游戏中的素材目录的定制，方便调用。一些其它可能需要重复使用的工具。



## 定义渲染器

渲染器定义为一个游戏的APP，他应该是这个游戏的最外层，可以定义他的，分辨率，标题，刷新频率。
如果游戏中有精灵贯穿全局（比如RPG游戏中的主要角色），这种精灵角色他不属于某个游戏片段，这样他应该存在于这个游戏app中。


## 定义游戏片段

一个gameApp中，至少得有一个游戏片段，游戏片段包括三个主要方法：

    draw() update() handle_event()

这三个方法分别对应，渲染场景，更新数据，事件处理。当我们继承新建游戏片段类的时候，需要根据自己的需求重写这三个方法。

## 如何使用PY_RPG？

    app = GameApp()#创建游戏
    appscreen = app.screen#获取渲染器
    app.scenes.append(MainScene(appscreen))#创建游戏菜单
    app.scenes.append(TestScene(appscreen))#创建游戏内容
    app.scenes.append(GameOverScene(appscreen))#游戏结束画面
    app.run() #游戏开始

根据需要创建并重写上边的三个类，然后创建游戏就可以了，现在这样看来，游戏的创建是不是很有层次了？

这个框架还没有封装完毕，我还会继续的，之后的游戏制作都要从这个框架上弄起了，初步还要写几个完整的小游戏例子。



'''
import pygame, sys
from pygame.locals import * #导入游戏常量

class GameApp:
    '''
    渲染器（APP）--只负责渲染游戏场景中存在的游戏片段，属性有：一个游戏片段容器及一些游戏窗口常用设置，并初始化游戏设置。
    '''
    def __init__(self,title='游戏窗口',resolution=(640,480),update_rate=24):
        '''
        :param title: 游戏标题
        :param resolution: 场景尺寸(640，480)
        :param update_rate: 刷频率默认24
        '''
        pygame.init()
        pygame.key.set_repeat(10)  # 重复响应一个按键
        self.title = title#游戏标题
        self.resolution = resolution#分辨率
        self.update_rate = update_rate#刷新频率
        self.scenes = []#所有游戏的片段list
        # self.mySprites  = [] #这里可以定义很多贯穿于多个片段中的游戏角色，比如：主角。
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.title)
        pygame.key.set_repeat(10)#设置键盘连续响应
        

    def run(self):
        '''
        游戏开始。
        '''
        print('游戏开始！')

        while True:
            for scene in self.scenes:
                #如果当前片段可以开始，则开始渲染
                if scene.start:
                    #传递相关参数，用来在scene中使用。
                    scene.screen = self.screen #渲染器
                    scene.update_rate = self.update_rate #刷新频率
                    scene.clock = self.clock #刷新频率设置对象
                    scene.scenes = self.scenes#获得当前所有游戏片段
                    scene.resolution = self.resolution#分辨率，用来获得场景的宽高
                    scene.run()


class Scene:
    '''
    游戏片段(scene)--可能是游戏中的一个片段，一个情节，一节过场，片头，片尾等，游戏片段中包含一个开关属性，用来控制是否可以渲染此游戏片段。
    '''
    def __init__(self, screen):
        '''

        :param screen:游戏中唯一的渲染器
        '''
        self.screen = screen
        self.update_rate = 24
        self.scenes = []#所有游戏的片段list
        self.id = ''
        self.start = False #每个场景都有一个开关标识，用来控制当前场景是否要开始渲染
        self.pause = False  # 游戏暂停控制



    def draw(self):
        '''此方法需要重写，用来绘制游戏中所有场景及角色'''
        pass
    def update(self):
        '''此方法需要重写，此方法用来更新游戏中精灵的属性，处理场景切换。'''
        pass
    def handle_event(self, event):
        '''可以重写此方法来获得事件处理触发'''

        
    def run(self):
        if self.start:
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        print('游戏已退出！')
                        pygame.quit()
                        sys.exit()
                    self.handle_event(event)
                self.draw()
                self.update()
                pygame.display.flip()
                self.clock.tick(self.update_rate)#设置帧速率
                if not self.start:
                    print(self.id,'已结束并退出')
                    break