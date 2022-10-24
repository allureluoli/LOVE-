from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event

introduce=on_keyword(['自我介绍','LOVE酱介绍'],priority=50)
@introduce.handle()
async def handle_func(bot: Bot,event :Event):
    await introduce.finish('呐呐~我是love酱哒，一个为铁锈战争群聊提供服务的虚拟少女~试试对我说：【love酱功能】吧！')

function1=on_keyword(['love酱功能','LOVE酱功能'],priority=50)
@function1.handle()
async def handle_func(bot: Bot,event :Event):
    await function1.finish('LOVE酱帮助群：827472569\n查询命令：群聊查询、教程查询（制作中）、单位查询（制作中）、地图查询（制作中）、模组查询（制作中）\n教程命令：LOVE酱铁锈教程\n联系作者：3345483363')