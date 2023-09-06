from urllib import request, error, parse
from bs4 import BeautifulSoup


def HomeList():
    """获取铁锈战争房间列表"""

    url = "http://www.corrodinggames.com/serverlist"  # noqa
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
    }

    dict = {
        "name": "Germey"
    }
    data = bytes(parse.urlencode(dict), encoding="utf8")

    try:
        req = request.Request(url=url, data=data, headers=headers, method="POST")
        response = request.urlopen(req)
        zfc1 = response.read()
        soup = BeautifulSoup(zfc1, "html.parser")

        soup_4 = soup.find_all("tr")
        Soup_4 = BeautifulSoup(str(soup_4), "html.parser")
        list_1 = Soup_4.get_text().replace('battleroom', '【联机房】').replace('Public', ' V:').replace('Private',  # noqa
                                                                                                      ' V:')  # noqa
        wtm = list_1.split(",")
        Self = ""
        for i in wtm[1:40]:
            Self += i + "\n"

        return Self

    except error.HTTPError as e:
        print(e.code, '\n', e.reason, '\n', e.headers)
