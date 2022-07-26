import base64
from pysondb import db
import os
import requests

def AddFursona(img: list,desc: str,owner: int,fursonaName: str):

def DelFursona(fursonaName: str,owner: int):

def RetMyAllFursonaProfile(sender: int):
  buffer=""
  for i in range(0,len(data)):
   buffer+=":star:"+data[i]+":star:"+"\n"
  return "你已有"+str(len(data))+'个崽子！\n'+buffer

def RetSomebodyFursonaProfile(fursonaName: str):

 return {"IsErr": False,"Desc": data["Desc"],"Img": data["Img"],"Owner": data["Owner"]}

AddFursona(["xxccv","gg","fgh"],"师",233,"落雾")
print(RetSomebodyFursonaProfile("落雾"))
AddFursona(["xxccv","dfgg","fgfgh"],"测小师",233,"落雾2")
AddFursona(["xxccv","dfgg","dsfdfg"],"师",233,"落雾3")
print(RetMyAllFursonaProfile(233))

DelFursona("落雾",233)
def DownloadImg(url: str,save: str):
 response = requests.get(URL)
 open(save, "wb").write(response.content)

def WriteJson(name: str,)