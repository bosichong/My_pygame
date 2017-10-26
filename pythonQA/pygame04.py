#codeing=utf-8
# @Time    : 2017-10-22
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
# @Title   : # “编学编玩”用Pygame写游戏（4）一个python问答游戏
# @Url     : http://www.17python.com/blog/47
# @Details : # “编学编玩”用Pygame写游戏（4）一个python问答游戏
# @Other   : OS X 10.11.6 
#            Python 3.6.1
#            VSCode 1.15.1
###################################
# “编学编玩”用Pygame写游戏（4）一个python问答游戏
###################################
'''
好开心，买的书终于到手了，极力推荐《Python游戏编程入门》！非常不错的一本书，另千万别买《Python和Pygame游戏开发指南》，好了，不要问什么，请叫我雷锋！

## 游戏流程

我觉得新手编写游戏的时候最大的难点是先把游戏构思的太细致了，以至于真正上手编程的时候完全不知道从哪里开始，平时构思设计游戏时，脑子里那闪耀的光芒，就觉得只要拿起键盘，一个旷世神作的游戏就要蛋生了！
实际呢？两眼瞪着电脑，我特么从哪开始写呢？，所以你需要一个流程，你可以拿纸笔画，或是找个流程图画一下。可以参考下图：

![]()

有游戏流程后，先不要急于实现游戏的细节功能，先把流程走一下，先搭建游戏骨架`pygame.init()`，嗯，这个你应该很熟了。
然后我们通过面向对象的方法来进行这个小游戏的编写：


    pyqa.game_Start()
    pyqa.show_qt()
    pyqa.game_Over()

这样在循环中你应该很明白游戏的流程，虽然他们都在循环中，但我们可以控制他们在游戏中渲染的逻辑，这样我们就可以考虑好游戏中类的属性了。
这是一个问答游戏，需要有基本的题库数据，我们通过python的流读入数据，因为python可以很方便的读行，这样我们可以定义一些规律，把每一题的问题、选择项，答案都分别占一行。
这样导入数据后可以返回一个list，方便操作。

好了，我们定义一下当前答题类`class Pyqa`的一些属性，首先他需要三个开关，分别代表游戏开始画面，答题画面，游戏结束画面，当然游戏一开始就是开始画面，我们可以设置他为`True`，
这样游戏一旦开始，即可直接进入游戏开始画面，当然我们还需要定义三个函数，分别渲染三个场景，通过`if self.gameStart`判断当前是否要渲染这段场景。
好了，流程说到这里应该了解了吧？如果还是很头疼，建议先打代码试试，游戏内容可以不用填加，就试过场。

## 游戏中的事件

当我们运行游戏的时候，我们发现游戏只停止在游戏开始画面上，并没有继续进和到问答画面，因为我们没有加入游戏的控制，我们通过玩家来按键获取当前的游戏按键事件，
`pygame`中的游戏事件轮询获取相应的事件来响应用户的操作。

    while True:
        for event in pygame.event.get():

当我们通过`event.key == K_RETURN:`在游戏开始画面处获得了回车键的事件，就可以把游戏中的`self.showQuestion`设置`True`，然后开始游戏了，其它响应也是如此，
比如获取游戏中的答案数字，也是通过相应的键值获取，具体可以查看代码了解。

## 答题场景编写

本游戏的核心就是回答问题，导入题库后，通过`def show_qt()`方法来渲染问题及选项。我在游戏中定义了一个函数`def print_text`是专门用来打印游戏中的文字的。
当我们在游戏中选择答案按下数字键1-4的时候，我们会通过`pyqa.handle_input(int)`方法来处理当前游戏中的一些数据，比如回答是否正确，提示正确答案，记录回答正确数等，
当我们再次按下回车键，`def next_question`方法会更新问题题库的索引指针，告诉`def show_qt()`我得渲染下一道题了！

## 游戏结束

当`def next_question`通过`self.current >= len(self.data)`发现已经到达题库最后边了，游戏就要结束了，设置游戏开关相关参数为false，设置游戏结束标识`gameOver`为`true`
进入游戏结束画面，展示游戏数据统计，最后当然还可以让你有重来的机会，具体实现请看代码吧，无非就是一些按键事件触发。

## 写在最后

无论是整个游戏还是中间的答题系统，我们发现在这个游戏中我们必须细致入微的进行设计判断每一步的操作，这就是游戏设计的精髓及乐趣，至少我们可以按着自己的需要来进行设计，当你把游戏设计成功，
代码编写运行无错时，希望你能体会到这其中的乐趣！如果你有时间，可否帮忙丰富一下题？谢啦，记得提git提交给我哦，谢谢了。







'''


import sys, pygame, os
from pygame.locals import *


#导入自定义游戏包
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取当前文件上级目录的绝对地址
sys.path.append(BASE_DIR)#添加一个模块搜索目录，方便找到自己的建的模块
from PY_RPG.util import *

class Pyqa:
    def __init__(self,file):
        #########游戏程控制##############
        self.gameStart = True#游戏开始画面
        self.showQuestion = False #问答开始
        self.gameOver = False #游戏结束
        #########问答游戏相关属性##############
        self.data = [] #游戏数据list
        self.current = 0#数据指针，指向当前数据data的索引
        self.total = 0 #统计行数。
        self.correct = 0#正确答案索引值int
        self.score = 0 #总得分
        self.scored = False#是否回答正确
        self.failed = False #是否回答错误
        self.wronganswer = 0 #当前回答错误时选择的数字。
        self.colors = [white,white,white,white]

        with open(file,mode='r',encoding='utf-8') as f :
            tmpdata = f.readlines()
        for line in tmpdata:
            self.data.append(line.strip())
            self.total += 1
        # print(self.total)
        

    def game_Start(self):
        '''游戏开始画面'''
        if self.gameStart:
            print_text(font1,200,200,"Python知识问答")
            print_text(font2,240,240,"请按Return键开始")
    
    def game_Over(self):          
        if self.gameOver:
            
            msg = ""
            msg_color = white
            kk = len(self.data) // 6 #总题数
            if kk == self.score :
                msg = "你特么太牛逼了！叫你声大佬，求带！"
                msg_color = green
            elif (self.score / kk >= 0.6 ):
                msg = "你很一般般啦，小兄弟你还得努力啊！"
                msg_color = green
            elif self.score / kk < 0.6:
                msg = "福布斯智商榜，你也就是垫底那伙的！"
                msg_color = red
            print_text(font1,100,200,msg,msg_color)
            print_text(font2,190,500-30,"大侠是否想重新来过？请按R键再玩一把！", green)

        
    def game_Restart(self):
        '''游戏选择游戏重新开始，初始化游戏数据'''
        self.gameStart = True#游戏开始画面
        self.showQuestion = False #问答开始
        self.gameOver = False #游戏结束
        self.current = 0#数据指针，指向当前数据data的索引
        self.total = 0 #统计行数。
        self.correct = 0#正确答案索引值int
        self.score = 0 #总得分
        self.scored = False#是否回答正确
        self.failed = False #是否回答错误
        self.wronganswer = 0 #当前回答错误时选择的数字。

    def show_qt(self):
        """显示问题"""
        if self.showQuestion:
            print_text(font1,190,5,"Python知识问答")
            print_text(font2,220,500-30,"请选择1-4来回来问题", purple)
            print_text(font2,540,5,"分数")
            print_text(font2,550,25,str(self.score),purple)

            self.correct = int(self.data[self.current+5])#获得正确答案
            question = self.current // 6 + 1 #判断第几组题。
            print_text(font1,5,80,"问题" + str(question))
            print_text(font2,20, 120,self.data[self.current],yellow)

            if self.scored:
                self.colors = [white,white,white,white]
                self.colors[self.correct-1] = green
                print_text(font1,230,380,"回答正确！", green)
                print_text(font2,240,420,"请按回车继续", green)
            elif self.failed:
                self.colors = [white,white,white,white]
                self.colors[self.wronganswer-1] = red
                self.colors[self.correct-1] = green
                print_text(font1,220,380,"回答错误", red)
                print_text(font2,230,420, "请按回车继续", red)
            #绘制选择答案
            print_text(font1,5,170,"请选择")
            print_text(font2,20,210,"1 - " + self.data[self.current+1],self.colors[0])
            print_text(font2,20,240,"2 - " + self.data[self.current+2],self.colors[1])
            print_text(font2,20,270,"3 - " + self.data[self.current+3],self.colors[2])
            print_text(font2,20,300,"4 - " + self.data[self.current+4],self.colors[3])

    def handle_input(self,number):
        if not self.scored and not self.failed:
            # 如果选择的数字与正确答案符合
            if number == self.correct:
                self.scored = True #设置当前问题回答正确
                self.score +=1 #总得分+1
            else:
                self.failed = True #回答错
                self.wronganswer = number #取得当前回答数值

    def next_question(self):
        if self.scored or self.failed:
            self.scored = False
            self.failed = False
            self.correct = 0
            self.colors = [white,white,white,white]
            self.current += 6
            print(self.current >= len(self.data))
            print(self.current)
            print(len(self.data))
            if self.current >= len(self.data):
                pygame.time.wait(100)    
                self.gameOver = True
                self.showQuestion = False
                self.gameStart = False
    def gametest(self):
        print('游戏开始：',self.gameStart)
        print('问答开始：',self.showQuestion)
        print('游戏结束：',self.gameOver)

def print_text(font, x, y, text, color=(255,255,255)):
    '''本游戏中绘制游戏中文字的函数方法'''
    imgText = font.render(text, True, color,)
    screen.blit(imgText,(x,y))

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Python知识问答")
font1 = pygame.font.Font(os.path.join(FONT_DIR,'msyh.ttf'), 28)
font2 = pygame.font.Font(os.path.join(FONT_DIR,'msyh.ttf'), 16)
white = 255,255,255
cyan = 0,255,255
yellow = 255,255,0
purple = 255,0,255
green = 0,255,0
red = 255,0,0
pyqa = Pyqa(os.path.join(os.path.dirname(__file__),'pyqa.txt'))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                sys.exit()
            elif event.key == K_1:
                pyqa.handle_input(1)
            elif event.key == K_2:
                pyqa.handle_input(2)
            elif event.key == K_3:
                pyqa.handle_input(3)
            elif event.key == K_4:
                pyqa.handle_input(4)
            elif event.key == K_RETURN:
                if pyqa.gameStart == True:
                    pyqa.gameStart = False
                    pyqa.showQuestion = True
                    pyqa.gametest()
                if pyqa.showQuestion == True:
                    pyqa.next_question()
                    pyqa.gametest()
            elif event.key == K_r:
                if pyqa.gameOver == True:
                    pyqa.game_Restart()
                    pyqa.gametest()
                

                    
            

    screen.fill((0,0,200))
    pyqa.game_Start()
    pyqa.show_qt()
    pyqa.game_Over()
    # print_text(font1,100,100,'Holle World',shadow=False)
    
    pygame.display.update()
