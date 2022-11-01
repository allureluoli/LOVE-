import os
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Bot, Event

course=on_fullmatch(['LOVE酱铁锈教程','教程查询'],priority=50)
@course.handle()
async def handle_func(bot: Bot,event :Event):
    await course.finish('呐呐！LOVE酱的教程命令：\n联机教程\n导入教程\n铁锈操作教程\n制作教程\n房间指令教程')

course=on_fullmatch(['导入教程'],priority=50)
@course.handle()
async def handle_func(bot: Bot,event :Event):
    await course.finish('呐呐！LOVE酱的教程命令：\n模组导入教程\n地图导入教程\n回放导入教程')



course_1=on_fullmatch(['开房教程','联机教程'],priority=50)
@course_1.handle()
async def handle_func(bot: Bot,event :Event):
    await course_1.finish('目前仅提供RCN官方开服教程'+r'https://www.yuque.com/derdct/rcn/main')

course_2=on_fullmatch(['模组导入教程'],priority=50)
@course_2.handle()
async def handle_func(bot: Bot, event: Event):
    wot2 = open(str(FilePath(r'\rustedwarfare\help\mod_course.txt')), encoding='UTF-8')
    load_2 = wot2.read()
    await course_5.finish(load_2)

course_3=on_fullmatch(['地图导入教程'],priority=50)
@course_3.handle()
async def handle_func(bot: Bot,event :Event):
    wot3 = open(str(FilePath(r'\rustedwarfare\help\map_course.txt')), encoding='UTF-8')
    load_3 = wot3.read()
    await course_3.finish(load_3)

course_4 = on_fullmatch(['回放导入教程'], priority=50)

@course_4.handle()
async def handle_func(bot: Bot, event: Event):
    wot4 = open(str(FilePath(r'\rustedwarfare\help\replay_course.txt')), encoding='UTF-8')
    load_4 = wot4.read()
    await course_4.finish(load_4)

course_5 = on_fullmatch(['房间指令查询','房间指令教程'], priority=50)
@course_5.handle()
async def handle_func(bot: Bot, event: Event):
    wot5 = open(str(FilePath(r'\rustedwarfare\help\server_instruct.txt')), encoding='UTF-8')
    load_5 = wot5.read()
    await course_5.finish(load_5)

course_2=on_fullmatch(['模组导入教程'],priority=50)
@course_2.handle()
async def handle_func(bot: Bot, event: Event):
    wot2 = open(str(FilePath(r'\rustedwarfare\help\mod_course.txt')), encoding='UTF-8')
    load_2 = wot2.read()
    await course_5.finish(load_2)

def getRootPath():
    # 获取文件目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 获取项目根路径，内容为当前项目的名字
    rootPath = curPath[:curPath.find('love2') + len('love2')]
    return rootPath

FilePath_1=str(getRootPath())

print(FilePath_1)
def FilePath(FilePath_2):#拼接捏
    FilePath_2=FilePath_1+FilePath_2
    return FilePath_2

