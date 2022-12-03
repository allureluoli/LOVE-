from nonebot.rule import to_me
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event, GroupMessageEvent, event
from nonebot.adapters.onebot.v11.bot import Bot



introduce_2 = on_fullmatch([''], rule=to_me(),priority=50)
@introduce_2.handle()
async def handle_func(bot: Bot, event: Event):


    await introduce.finish('呐呐~我是love酱哒，一个为铁锈战争群聊提供服务的虚拟少女~试试对我说： love酱功能 吧！')

introduce = on_fullmatch(['自我介绍', 'LOVE酱介绍', '@LOVE酱','maa'], priority=50)

@introduce.handle()
async def handle_func(bot: Bot, event: Event):


    await introduce.finish('呐呐~我是love酱哒，一个为铁锈战争群聊提供服务的虚拟少女~试试对我说： love酱功能 吧！')

function1 = on_fullmatch(['love酱功能', 'LOVE酱功能'], priority=50)

@function1.handle()
async def handle_func(bot: Bot, event: Event):
    await function1.finish(
        '群聊代宣请加群\nLOVE酱的家：827472569\n[新增]铁锈抓兔机 战队抓兔机[含战队要素]\n[新增]获取房间列表\n[新增]FGO十连  [新增]英灵召唤\n查询命令：群聊查询、教程查询、单位查询（制作中）、地图查询（制作中）、模组查询（制作中）\n教程命令：LOVE酱铁锈教程\n联系作者：3345483363')

