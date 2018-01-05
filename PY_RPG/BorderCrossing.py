#codeing=utf-8
# @Time    : 2017-10-15
# @Author  : J.sky
# @Mail    : bosichong@qq.com
# @Site    : www.17python.com
'''一个精灵边界碰撞检测工具类'''
class BorderCrossing:
    '''一个边界碰撞检测类'''
    def __init__(self,xstart,ystart,width,height):
        '''

        :param xstart: 场景X起点
        :param ystart: 场景Y起点
        :param width:  场景宽
        :param height: 场景高
        '''
        self.sprite = None#需要检测的对象
        #场景坐标起点及宽高。
        self.xstart = xstart
        self.ystart = ystart
        self.width = width
        self.height = height

    def isLeftBorderCrossing(self):
        '''是否碰撞左边'''
        if self.sprite.x <= self.xstart:
            print('碰撞左边碰撞左边')
            return True
        else:
            return False 
    def isTopBorderCrossing(self):
        '''是否碰撞上边'''
        if self.sprite.y <= self.ystart:
            print('碰撞上边碰撞上边')
            return True
        else:
            return False
    def isRightBorderCrossing(self):
        '''是否碰撞右边'''
        if self.sprite.x + self.sprite.width >= self.xstart + self.width:
            # print('{0}||||||||{1}'.format(self.sprite.x + self.sprite.width,self.xstart + self.width))
            print('碰撞右边碰撞右边')
            return True
        else:
            return False 
    def isBottomBorderCrossing(self):
        '''是否碰撞下边'''
        if self.sprite.y + self.sprite.height >= self.ystart + self.height:
            print('碰撞下边碰撞下边')
            return True
        else:
            return False

    def isBorder(self):
        '''边界碰撞检测，只要碰到边了就返回true'''
        if(self.isLeftBorderCrossing() or self.isTopBorderCrossing() or self.isRightBorderCrossing() or self.isBottomBorderCrossing()):
            return True
        else:
            return False

def main():
    pass

if __name__ == '__main__':
    main()
