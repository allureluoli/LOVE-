from nonebot.adapters.onebot.v11 import Event
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.plugin.on import on_fullmatch

"""本文件主要用于关于LOVE酱帮助功能的实现"""

LOVE = on_fullmatch(('爱!', '爱酱', 'love', 'LOVE酱', 'love酱', '小宝贝'), priority=50)


@LOVE.handle()
async def handle_func(bot: Bot, event: Event):
    await LOVE.finish('呐呐呐？是在叫我嘛~')


Help = on_fullmatch(('help', '帮助', '功能', 'LOVE酱功能'), priority=50)


@Help.handle()
async def handle_func(bot: Bot, event: Event):
    message = """【LOVE酱♥基本功能列表】
【@LOVE 进行教学和聊天捏！】
【LOVE教学】:【约战大厅】
【单位查询】:【今日抽签】
【随机地图】:【群聊查询】
【铁锈教程】:【主人功能】
【为我发电】:【更多功能】"""

    await Help.finish(message)


MapHelp = on_fullmatch('随机地图', priority=50)


@MapHelp.handle()
async def handle_func(bot: Bot, event: Event):
    message = """---随机地图的指令---
        随机单挑图
        随机3P图
        随机4P图
        随机6P图
        随机8P图
        随机10P图"""

    await MapHelp.finish(message)


RWHelp = on_fullmatch('铁锈教程', priority=50)


@RWHelp.handle()
async def handle_func(bot: Bot, event: Event):
    message = """ ---【目前仅支持的教程命令】---
【导入教程】:【更多教程】"""

    await RWHelp.finish(message)


HelpMe = on_fullmatch('为我发电', priority=50)


@HelpMe.handle()
async def handle_func(bot: Bot, event: Event):
    message = """ ---【你的每一份支持都会成为LOVE酱开发的动力!】---
【爱发电网址】:"https://afdian.net/a/allureluoli" """

    await HelpMe.finish(message)


MoreHelp = on_fullmatch('更多功能', priority=50)


@MoreHelp.handle()
async def handle_func(bot: Bot, event: Event):
    message = """---任意随机数---
【LOVE丢-XX】
---看看房间列表---
【获取房间列表】
---抓兔机!---
【战队抓兔机】【铁锈抓兔机】
---召唤英灵吧！---
【英灵召唤】【FGO十连】"""

    await MoreHelp.finish(message)


MasterHelp = on_fullmatch('主人功能', priority=50)


@MasterHelp.handle()
async def handle_func(bot: Bot, event: Event):
    message = "主人功能有：\n【添加XX群-】\n【查看待审核词汇】\n【过审-】\n【拒绝过审-】"

    await MasterHelp.finish(message)


HelpTwo = on_fullmatch('单位查询', priority=50)


@HelpTwo.handle()
async def handle_func(bot: Bot, event: Event):
    message = "请以【查询-单位名】这样的格式输入哦！（数据源自铁锈wiki！）"

    await HelpTwo.finish(message)


Study = on_fullmatch('LOVE教学', priority=50)


@Study.handle()
async def handle_func(bot: Bot, event: Event):
    message = "请@LOVE酱 以 【@LOVE酱 教学-你发送的词=回复词】 的格式进行教学哦！(如果提交错误，请 @LOVE酱 撤回-教学词 的形式进行撤回 ，或者重新进行教学)"

    await Study.finish(message)


Catcher = on_fullmatch('群聊查询', priority=50)


@Catcher.handle()
async def handle_func(bot: Bot, event: Event):
    message = "群聊查询有五种模式：\n【战队群查询】\n【模组群查询】\n【闲聊群查询】\n【技术群查询】\n【赛事群查询】"

    await Catcher.finish(message)


ImportCourse = on_fullmatch('导入教程', priority=50)


@ImportCourse.handle()
async def handle_func(bot: Bot, event: Event):
    message = "导入教程有五种模式：\n【模组导入教程】\n【地图导入教程】\n【回放导入教程】"

    await ImportCourse.finish(message)


MoreCourse = on_fullmatch('更多教程', priority=50)


@MoreCourse.handle()
async def handle_func(bot: Bot, event: Event):
    message = "更多教程有：\n【房间指令教程】\n【RCN联机教程(不可用)】"

    await MoreCourse.finish(message)


WarHome = on_fullmatch('约战大厅', priority=50)


@WarHome.handle()
async def handle_func(bot: Bot, event: Event):
    message = "【欢迎来到约战大厅，在这里你可以看到寻求对局的玩家的房间号，上限10条，每十分钟清理一次。】\n发送【提交告示-房间类型 房间地址】提交告示（符号皆为英文版不要输错哦~）\n发送【查看告示栏】即可查看公告！"

    await WarHome.finish(message)
