from nonebot import  on_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
import os

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


tyt_1 = open(str(FilePath(r'\rustedwarfare\rw\group_id.txt')), encoding='UTF-8')
tyt_2 =tyt_1.readlines()
hang=0
for x in range(len(tyt_2)):
    hang=hang+1

# 发送图片MessageSegment(pathlib.Path(fp))


pvp = on_command(cmd='跨群约战-', priority=50)
# 使用handle装饰器
# 约战系统重置
@pvp.handle()
async def handle_func(bot: Bot, event: GroupMessageEvent):
    txet_5 = str(event.get_session_id()).split('_', 2)
    txet_7 = txet_5[2]  # 获取QQ号
    qq_1 = open(FilePath(r'\rustedwarfare\PVP\_qq.txt'))
    #在这里开始检查
    #将文件中的QQ导出为一个列表
    #在列表中进行遍历对证
    hang_2 = 0  #跑出列表有几个元素，然后根据元素数量确定循环次数
    list_1=qq_1.readlines()
    print(list_1)
    qq_1.close()
    for x in range(len(list_1)):
        hang_2 = hang_2 + 1
        return hang_2
    print(hang_2)
    #这里可以试试使用对象
    qq_2=0
    while hang_2>0:
        hang_2 = hang_2 -1
        while(qq_2):
            if list_1[hang_2] != txet_7:
                return 1
            if list_1[hang_2] == txet_7:
                return 0
    if qq_2 == 0:
        await pvp.finish("你已经进行过约战了哦~")
    #发现已经进行过约战-直接跳出循环
    #使用with打开文件试试？
    qq_1=open(FilePath(r'\rustedwarfare\PVP\_qq.txt'),mode = '+')
    qq_1.write(str(txet_7))
    qq_1.close()
    ##提前检查其中是否有QQ号
    #QQ号写入文件，然后定时删除QQ
    gossip_text = open(str(FilePath(r'\rustedwarfare\rw\group_id.txt')), encoding='UTF-8')
    tyt_2 = gossip_text.readlines()
    hang = 0
    for x in range(len(tyt_2)):
        hang = hang + 1
    gossip_text.close()
    while hang > 0:
            hang = hang - 1
            text_1=str(event.get_message())
            txet_2=text_1.split('-',1)#将消息分割成一个列表的两个元素
            txet_4=txet_2[1]
    #这里txet_4就是房间号
    #循环执行语句,在检测到空的时候退出循环
    #获得用户QQ号，昵称，
            txet_5=str(event.get_session_id()).split('_',2)#回复的QQ群和QQ号
            txet_6=txet_5[1]#获取群号
            txet_7=txet_5[2]#获取QQ号
            str_1 =str("来自QQ群："+str(txet_6))
            str_2=str("QQ为："+str(txet_7))
            str_3=str(" 的用户发起了对战邀请。\n房间号："+str(txet_4))
            text_8=str(str_1+str_2+str_3)
                #后期再加昵称吧
            gossip_text = open(str(FilePath(r'\rustedwarfare\rw\gossip.txt')), encoding='UTF-8')
            a1=gossip_text.readline()
            tyt_1 = open(str(FilePath(r'\rustedwarfare\rw\group_id.txt')), encoding='UTF-8')
            tyt_2 = tyt_1.readlines()
            s=hang-1
            group_id = tyt_2[s] #群的id
                #将群号保存到一个列表中，读取的时候进行遍历
                # 逐行读取，遍历发送
            await pvp.send_group_msg(group_id=int(group_id), message=text_8, auto_escape=False)
            #转发功能的制作


