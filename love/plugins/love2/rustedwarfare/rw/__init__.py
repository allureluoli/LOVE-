from nonebot import  on_fullmatch
from nonebot.adapters.onebot.v11 import Bot, Event
from ..function import FilePath




check = on_fullmatch(['群聊查询'], priority=50)

# 使用handle装饰器
@check.handle()
async def handle_func(bot: Bot, event: Event):
    await check.finish(
        "【铁锈交流】：494437701\t【碳酸地牢】：792402564\n【广告位招租】\t【光辉战队】：827472569\n群聊查询命令有：战队群查询、模组群查询、地图群查询、闲聊群查询...")


Battalion1 = on_fullmatch(['战队群查询'], priority=50)

@Battalion1.handle()
async def handle_func(bot: Bot, event: Event):
    wot1 = open(str(FilePath(r'/rustedwarfare/rw/Battalion.txt')), encoding='UTF-8')
    load_1 = wot1.read()
    await Battalion1.finish(load_1)



mods = on_fullmatch(['模组群查询'], priority=50)
@mods.handle()
async def handle_func(bot: Bot, event: Event):
    wot2 = open(str(FilePath(r'/rustedwarfare/rw/mods.txt')), encoding='UTF-8')
    load_2 = wot2.read()
    await mods.finish(load_2)

maps = on_fullmatch(['地图群查询'], priority=50)
@maps.handle()
async def handle_func(bot: Bot, event: Event):
    wot3 = open(str(FilePath(r'/rustedwarfare/rw/maps.txt')), encoding='UTF-8')
    load_3 = wot3.read()
    await mods.finish(load_3)

gossip = on_fullmatch(['普通群查询'], priority=50)
@gossip.handle()
async def handle_func(bot: Bot, event: Event):
    wot4 = open(str(FilePath(r'/rustedwarfare/rw/gossip.txt')), encoding='UTF-8')
    load_4 = wot4.read()
    await mods.finish(load_4)











