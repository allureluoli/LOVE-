import datetime
from datetime import datetime
import json
import os
import shutil
import time

"""本类主要实现对json数据的处理"""
curPath = str(os.path.abspath(os.path.pardir) + "/LOVE/love/data/LoveLexicon/").replace('db/', '')
curPathTwo = str(os.path.abspath(os.path.pardir) + "/LOVE/love/data/Examine/").replace('db/', '')

'''初始化数组'''

List = ['[空位]', '[空位]', '[空位]', '[空位]', '[空位]', '[空位]', '[空位]', '[空位]', '[空位]', '[空位]']
ListTWO = ['[空位]', '[空位]', '[空位]', '[空位]', '[空位]', '[空位]', '[空位]', '[空位]', '[空位]', '[空位]']
Number = 0


class JsonDB():
    def __init__(self, QQ, send, Reply):
        self.QQ = QQ
        self.send = send
        self.Reply = Reply

    def revive(self):
        os.remove(os.getcwd() + '/love/data/TimeData/hatred/' + self.QQ+'.txt')

    def Save(self):
        now = datetime.now()
        data = {
            "教学人": self.QQ,
            "时间": now.strftime("%Y-%m-%d %H:%M:%S"),
            self.send: self.Reply
        }

        with open(f"{curPathTwo + self.send}.json", "w") as json_file:
            json.dump(data, json_file)

        # 将字典对象保存为JSON文件

    def Load(self):

        try:
            # 从JSON文件中读取数据并解码为Python对象
            with open(f"{curPath + self.send}.json", "r") as json_file:
                data = json.load(json_file)

                return data[f"{self.send}"]

        except:
            return "LOVE酱现在还听不懂哦~可以教我吗？"

    def recall(self):

        try:
            # 从JSON文件中读取数据并解码为Python对象
            with open(f"{curPathTwo + self.send}.json", "r") as json_file:
                data = json.load(json_file)

            if self.QQ == data['教学人']:
                os.remove(curPathTwo + self.send+'.json')
                return '已成功撤回词汇'
            else:
                return '您并不是这个词汇的教学人哦~'
        except:

            return '您并没有提交过这个词汇哦~'

    def ExamineLoad(self):
        """读取待审核文件夹内的文件名"""
        with open(f"{curPathTwo + self.send}", "r") as json_file:
            data = json.load(json_file)

            return data[f"{str(self.send).split('.')[0]}"]  # 将文件名返回

    def MOVE(self):
        """将文件转移实现通过审核"""
        try:
            shutil.move(curPathTwo + self.send, curPath)
        except:
            os.unlink(curPath + self.send)
            shutil.move(curPathTwo + self.send, curPath)  # 发现文件重复则删除文件

    def refuse(self):
        '''删除文件'''
        os.remove(curPathTwo + self.send)

    def TeamGroup(self):
        '''写入战队群储存文件的方法'''
        with open(f"{os.getcwd() + '/love/data/Group/' + 'TeamGroup.txt'}", "a", encoding='gbk') as file:
            file.write(f"{self.send}\n")

    def TeamCheck(self):
        with open(f"{os.getcwd() + '/love/data/Group/' + 'TeamGroup.txt'}", "r", encoding='gbk') as file:
            return file.read()

    def MODGroup(self):

        with open(f"{os.getcwd() + '/love/data/Group/' + 'MODGroup.txt'}", "a", encoding='gbk') as file:
            file.write(f"{self.send}\n")

    def MODCheck(self):
        with open(f"{os.getcwd() + '/love/data/Group/' + 'MODGroup.txt'}", "r", encoding='gbk') as file:
            return file.read()

    def ArderGruop(self):
        with open(f"{os.getcwd() + '/love/data/Group/' + 'ArderGroup.txt'}", "a", encoding='gbk') as file:
            file.write(f"{self.send}\n")

    def ArderCheck(self):
        with open(f"{os.getcwd() + '/love/data/Group/' + 'ArderGroup.txt'}", "r", encoding='gbk') as file:
            return file.read()

    def MatchGrop(self):
        with open(f"{os.getcwd() + '/love/data/Group/' + 'MatchGroup.txt'}", "a", encoding='gbk') as file:
            file.write(f"{self.send}\n")

    def MatchCheck(self):
        with open(f"{os.getcwd() + '/love/data/Group/' + 'MatchGroup.txt'}", "r", encoding='gbk') as file:
            return file.read()

    def TechnologyGrop(self):
        with open(f"{os.getcwd() + '/love/data/Group/' + 'TechnologyGroup.txt'}", "a", encoding='gbk') as file:
            file.write(f"{self.send}\n")

    def TechnologyCheck(self):
        with open(f"{os.getcwd() + '/love/data/Group/' + 'TechnologyGroup.txt'}", "r", encoding='gbk') as file:
            return file.read()

    def LoadText(self):
        '''我TM感觉这多此一举'''
        List = ['map_course.txt', 'mod_course.txt', 'replay_course.txt', 'server_instruct.txt']
        if self.send == 'Map':
            Text = List[0]
        elif self.send == "MOD":
            Text = List[1]
        elif self.send == 'Replay':
            Text = List[2]
        elif self.send == 'Server':
            Text = List[3]

        with open(f"{os.getcwd() + '/love/data/Course/' + Text}", "r", encoding='utf-8') as file:  # noqa
            return file.read()

    def Course(self):
        """我也不清楚我脑子里怎么想出的这段破代码"""
        match self.send:
            case 'Map':
                Text = JsonDB(QQ='', send=self.send, Reply='')
                return Text.LoadText()
            case 'MOD':
                Text = JsonDB(QQ='', send=self.send, Reply='')
                return Text.LoadText()
            case 'Replay':
                Text = JsonDB(QQ='', send=self.send, Reply='')
                return Text.LoadText()
            case 'Server':
                Text = JsonDB(QQ='', send=self.send, Reply='')
                return Text.LoadText()

    def AdvertisementTime(self):
        '''读取之前保存的时间'''
        try:
            with open(f"{os.getcwd() + '/love/data/Advertisement/' + f'{self.QQ}.txt'}", "r") as file:

                return datetime.strptime(file.read(), "%Y-%m-%d %H:%M:%S.%f")

        except:
            return 0
    def idioctoniaTime(self):
        '''读取文件内的时间 如果没有则返回0'''

        try:
            with open(f"{os.getcwd() + '/love/data/TimeData/hatred/' + f'{self.QQ}.txt'}", "r") as file:

                return datetime.strptime(file.read(), "%Y-%m-%d %H:%M:%S.%f")

        except:
            return 0

    def ChatOS(self):
        try:

            if self.Reply=='start':

                with open(f"{os.getcwd() + '/love/data/ChatData/' + f'{self.QQ}.txt'}", "w") as file:
                    file.write(self.QQ)

            elif self.Reply == 'find':
                with open(f"{os.getcwd() + '/love/data/ChatData/' + f'{self.QQ}.txt'}", "r", encoding='gbk') as file:
                    return file.read()
            else:
                 os.remove(f"{os.getcwd() + '/love/data/ChatData/' + f'{self.QQ}.txt'}")

        except:
            return 0
    def idioctonia(self):
        now = datetime.now()
        cdtime = now.strftime("%Y-%m-%d %H:%M:%S.%f")

        #第一次使用写入时间

        with open(f"{os.getcwd() + '/love/data/TimeData/hatred/' + f'{self.QQ}.txt'}", "w") as file:
            file.write(cdtime)

        Text = '似了'
        return Text


    def Advertisement(self):
        """实现了公告栏的方法"""
        now = datetime.now()
        # 写入时间
        cdtime = now.strftime("%Y-%m-%d %H:%M:%S.%f")

        with open(f"{os.getcwd() + '/love/data/Advertisement/' + f'{self.QQ}.txt'}", "w") as file:
            file.write(cdtime)

        with open(f"{os.getcwd() + '/love/data/Advertisement/' + 'log.txt'}", "a") as file:
            file.write(f"QQ:\t{self.send}\n")

        i = 0
        Text = self.send
        while i <= 10:
            global List

            if len(List[i]) == 4:

                List[i] = Text

                global Number
                Number = i
                return "提交成功！"

            else:
                i += 1

        return "告示栏已满！"

    def AdvertisementTWO(self):
        """实现了公告栏的方法"""
        now = datetime.now()
        # 写入时间
        cdtime = now.strftime("%Y-%m-%d %H:%M:%S.%f")

        with open(f"{os.getcwd() + '/love/data/Advertisement/' + f'{self.QQ}.txt'}", "w") as file:
            file.write(cdtime)

        with open(f"{os.getcwd() + '/love/data/Advertisement/' + 'log.txt'}", "a") as file:
            file.write(f"QQ:\t{self.send}\n")

        i = 0
        Text = self.send
        while i <= 10:
            global ListTWO

            if len(ListTWO[i]) == 4:

                ListTWO[i] = Text

                global Number
                Number = i
                return "提交成功！"

            else:
                i += 1

        return "告示栏已满！"

    def CheckAdvertisement(self):
        if self.send != 'Two':
            global List
            Check = ''
            for i in List:
                Check += i + '\n'

            return Check
        else:
            global ListTWO
            Check = ''
            for i in ListTWO:
                Check += i + '\n'

            return Check

    def Config(self):

        with open(f"{os.path.abspath(os.path.pardir)}/LOVE/Config.json") as json_file:
            data = json.load(json_file)
            return int(data['master'])


class Clean():
    def __init__(self, i):
        self.i = i
        '''愚蠢的实现方法'''

    def Clean(self, i):
        time.sleep(600)
        global List
        List[self.i] = '[空位]'

        return "该告示将在十分钟后自动删除.."

    def CleanTWO(self):
        time.sleep(600)
        global ListTWO
        ListTWO[Number] = '[空位]'

    def Cleanall(self):

        global List
        List= ['[空位]', '[空位]', '[空位]', '[空位]', '[空位]', '[空位]', '[空位]', '[空位]', '[空位]', '[空位]']

        return "哦删完事了"
