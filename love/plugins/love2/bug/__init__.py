import os
from pathlib import Path
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event, MessageSegment
from nonebot.adapters.onebot.v11.bot import send, Bot

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



tu3=on_fullmatch(['测试-加文字'],priority=50)
@tu3.handle()
async def handle_func(bot: Bot, event: Event):
    #把图片路径构造成一个列表
    j = 5
    while j > 0:
        j = j - 1
        list_2 = [r'\image\3.gif',r'\image\2.jpg', r'\image\3.jpg', '这是第二关文字', '这是个文字']
        list_3=['3.gif','2.jpg','3.jpg','null','null']
        if j > 2:
            await tu3.send(list_2[j])
        else:
            path = Path(FilePath(list_2[j])).parent / list_3[j]
            image = MessageSegment.image(path)
            await tu3.send(image)


        #构造图片消息段





'''
weather = on_command(cmd="weather", aliases={"傻逼", "天气预报"}, priority=5)


@weather.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("city", args)  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想查询哪个城市的傻逼呢？")
async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
    if city_name not in ["淄博", "魔法少女"]:  # 如果参数不符合要求，则提示用户重新输入
        # 可以使用平台的 Message 类直接构造模板消息
        await weather.reject(city.template("你想查询的傻逼 {city} 暂不支持，请重新输入！"))

    city_weather = await get_weather(city_name)
    await weather.finish(city_weather)

# 在这里编写获取天气信息的函数
async def get_weather(city: str) -> str:
    return f"{city}的傻逼是老琪"
'''
