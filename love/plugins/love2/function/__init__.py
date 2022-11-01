from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event
from nonebot.adapters.onebot.v11.bot import Bot

class Dialogue:
    x=''
    m=''
    #dialogue_1=''
    def __init__(self,x,m):
        #使用面向对线，创建类，对类中的对象赋值
        self.x = x
        self.m = m
        #self.dialogue_1 =dialogue_1
    def speak(self):
        dialogue_1 = on_fullmatch([self.x], priority=50)
        @dialogue_1.handle() #出错
        async def handle_func(bot: Bot, event: Event):
            await dialogue_1.send(self.m)

miss_1 = Dialogue('测试','测试成功')
miss_1.speak()

miss_2 =Dialogue('测试2','测试2成功')
miss_2.speak()

'''
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

# 实例化类
p = people('runoob',10,30)
p.speak()




'''
'''
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'

# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())
'''