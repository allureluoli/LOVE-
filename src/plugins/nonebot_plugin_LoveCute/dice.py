from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event

courtesy = on_command(cmd='丢', priority=50)  # 好累喔，下次开心的时候再写吧~~~


@courtesy.handle()
async def handle_func(event: Event):
    message = str(event.get_message()).replace('丢','')
    match message:
        case '一面骰子':
            message = "世界上哪有这种的骰子啊！"
        case '二面骰子':
            message = ""
        case '三面骰子':
            message = "晚安~~好梦哦~~"

