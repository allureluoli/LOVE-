from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event

course=on_keyword(['LOVE酱铁锈教程'],priority=50)
@course.handle()
async def handle_func(bot: Bot,event :Event):
    await course.finish('呐呐！LOVE酱的教程命令：\n联机教程\n导入教程\n铁锈操作教程\n制作教程')

course=on_keyword(['导入教程'],priority=50)
@course.handle()
async def handle_func(bot: Bot,event :Event):
    await course.finish('呐呐！LOVE酱的教程命令：\n模组导入教程\n地图导入教程\n回放导入教程')


course_1=on_keyword(['开房教程','联机教程'],priority=50)
@course_1.handle()
async def handle_func(bot: Bot,event :Event):
    await course_1.finish('目前仅提供RCN官方开服教程'+r'https://www.yuque.com/derdct/rcn/main')

course_2=on_keyword(['模组导入教程'],priority=50)
@course_2.handle()
async def handle_func(bot: Bot,event :Event):
    await course_2.finish('还没做哦')

course_3=on_keyword(['地图导入教程'],priority=50)
@course_3.handle()
async def handle_func(bot: Bot,event :Event):
    await course_3.finish('还没做哦')

course_4 = on_keyword(['回放导入教程'], priority=50)

@course_4.handle()
async def handle_func(bot: Bot, event: Event):
    await course_4.finish('还没做哦')