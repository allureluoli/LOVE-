from importlib import reload
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from .Demo import home_list
reload(Demo)




introduce = on_command("获取房间列表")

@introduce.handle()
async def handle_func(bot: Bot, event: Event):

   game_list=""
   print(home_list(game_list))
   await introduce.finish(home_list(game_list))

#去进行一次爬虫，将返回的房间列表发送出来

#将列表拼成文章







