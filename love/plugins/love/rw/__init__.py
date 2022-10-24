import os
from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
#
check = on_keyword(['群聊查询'], priority=50)

# 使用handle装饰器
@check.handle()
async def handle_func(bot: Bot, event: Event):
    await check.finish(
        "群聊查询命令有：战队群查询、模组群查询、地图群查询、闲聊群查询...\n【铁锈交流】：494437701\n【光辉战队】：827472569\n【广告位招租】")


Battalion1 = on_keyword(['战队群查询'], priority=50)

@Battalion1.handle()
async def handle_func(bot: Bot, event: Event):
    wot1 = open(str(FilePath(r'\rw\Battalion.txt')), encoding='UTF-8')
    load_1 = wot1.read()
    await Battalion1.finish(load_1)

mods = on_keyword(['模组群查询'], priority=50)
@mods.handle()
async def handle_func(bot: Bot, event: Event):
    wot2 = open(str(FilePath(r'\rw\mods.txt')), encoding='UTF-8')
    load_2 = wot2.read()
    await mods.finish(load_2)

maps = on_keyword(['地图群查询'], priority=50)
@maps.handle()
async def handle_func(bot: Bot, event: Event):
    wot3 = open(str(FilePath(r'\rw\maps.txt')), encoding='UTF-8')
    load_3 = wot3.read()
    await mods.finish(load_3)

gossip = on_keyword(['普通群查询'], priority=50)
@gossip.handle()
async def handle_func(bot: Bot, event: Event):
    wot4 = open(str(FilePath(r'\rw\gossip.txt')), encoding='UTF-8')
    load_4 = wot4.read()
    await mods.finish(load_4)


#ceshi1 = on_keyword(['战队群查询'], priority=50)
#
#@ceshi1.handle()
#async def handle_func(bot: Bot, event: Event):
#    wot1 = open(str(FilePath(r'\rw\Battalion.txt')), encoding='UTF-8')#在这里填写相对路径即可
#    load_1 = wot1.read()
#    await ceshi1.finish(str(load_1))

# 获得根路径，生成绝对路径
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