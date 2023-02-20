import re
from urllib import request, error,parse
from bs4 import BeautifulSoup
from nonebot import on_message, on_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent


class wiki():
    def __init__(self, name):
        self.name = name


    def wiki(self):
        url = f"https://rustedwarfare.org/wiki/{self.name}"
        headers = {
            "Accept": r"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Connection": "keep-alive",
            "Host": "rustedwarfare.org",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
            "accept-encoding":"identity"
        }

        dict = {
            "name": "Germey"
        }
        data = bytes(parse.urlencode(dict), encoding="utf8")

        try:
            #url进行转换
            import string
            from urllib.parse import quote
            url = quote(url, safe=string.printable)


            req = request.Request(url=url, data=data, headers=headers, method="POST",)
            response = request.urlopen(req)
            zfc1=response.read()
            soup = BeautifulSoup(zfc1,"html.parser")

            soup_4=soup.find_all(name='table',attrs='wikitable')
            Soup_4= BeautifulSoup(str(soup_4),"html.parser")

            list_1 =Soup_4.get_text().strip().replace('...','').replace(", ","")
            new_string = re.sub(r'\n\s*\n', '\n', list_1).replace("血量\n","血量：").replace("可攻击单位\n","可攻击单位:").replace("建造用单位\n","建造用单位").replace("移动范围\n","移动范围：").replace("人为建造","【人为建造】：").replace("质量\t","质量：")
            neew_string = new_string.replace("攻击距离\n","攻击距离:").replace("价格\n","价格:").replace("速度\n","速度：").replace("旋转速度\n","旋转速度:").replace("射击延迟\n","射击延迟:").replace("【自动生成","自动生成】：").replace("运输","运输：")
            neeew_string =neew_string.replace("直接伤害（每发子弹）\n","直接伤害（每发子弹）：").replace("制造前提\n","制造前提:").replace("生命值\n","生命值：").replace("科技等级\n","科技等级：").replace("视野","视野：")

            wiki_text=neeew_string

            return wiki_text

        except error.HTTPError as e:
            print(e.code, '\n', e.reason, '\n', e.headers)
            print("出错了")

            aaa= "这不是个有效的单位名嗷~"
            return aaa





a = wiki("坦克")

print(a.wiki())


query = on_command(cmd='单位查询-',aliases={"单位查询-","单位查询—","查询-"},priority=20)


@query.handle()
async def handle_func(bot: Bot, event: GroupMessageEvent, ):

    text = str(event.get_message()).split('-', 1)


    try:
        a = wiki(text[1])

        await query.send(a.wiki())

    except:
        print("不行喵")
