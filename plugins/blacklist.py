# -*- coding:utf-8 -*-
import requests
import html2text


def IsBlacklisted(qq: int):
    keywords = {"qq": qq}
    url = "https://yunhei.qimeng.fun/"
    r = requests.post(url, data=keywords)
    txt = html2text.html2text(r.text)
    return txt[txt.find("请输入账号或群号查询:") + 13 : txt.find("[举报上黑]") - 3]


# print(IsBlacklisted(2460484120))
# print(IsBlacklisted(32411213))
