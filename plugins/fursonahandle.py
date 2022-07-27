import json
import base64
import urllib.request 
def AddFursona(fursonaName: str,sender: int,desc: str,img):
 return CreateJson(fursonaName,{"Owner": sender,"Desc": desc,"Img": img})
def RetSomebodyFursonaProfile(fursonaName: str):
 return ReadJson(fursonaName)
def ReadJson(n: str):
 try:
  with open(r".\plugins\database\%s.json" % base64.b64encode(n.encode()).decode(),'r') as load_f:
   load_dict = json.load(load_f)
  return load_dict
 except:
  return None
def CreateJson(n: str,data: dict):
 try:
  with open(r'.\plugins\database\%s.json' % base64.b64encode(n.encode()).decode(), 'w') as f:
   json.dump(data, f)
  return True
 except:
  return False
def SaveImg(url: str,n: str,id: str):
 try:
   suffix=id[id.rfind("."):]
   urllib.request.urlretrieve(url, r'.\plugins\database\%s%s' %(base64.b64encode(n.encode()).decode(),suffix))
   return (base64.b64encode(n.encode()).decode()+suffix)
 except:
   return None
