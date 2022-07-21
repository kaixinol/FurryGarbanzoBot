import re
import os

def WarnMember(group: str,qq: str,who: str,reason: str):
 with open(".\\plugins\\log\\"+group+".log", 'a+') as f:
      f.write("\nWARN|"+who+"|"+qq+"|"+reason+"\n")
def NumberOfWarnings(group: str,qq: str):
 if os.path.exists(".\\plugins\\log\\"+group+".log")==False:
    return "没有记录！"
 else:
  with open(".\\plugins\\log\\"+group+".log", 'r') as f:
      data=f.read()
  warn_list=[data.start() for data in re.finditer(qq, data)]
  if warn_list==[]:
   return "没有记录！"
  line_list=[data.start() for data in re.finditer("\n", data)]
  ret=""
  count=1
  for i in range(len(warn_list)):
   for ii in range(len(line_list)):
    if ii+1>len(line_list):
     msg=data[line_list[ii]].split("|")
     ret+="第"+str(count)+"次警告，"+"执行人为"+msg[1]+"，理由为"+msg[3]+"\n"
     count+=1
    if line_list[ii]<warn_list[i] and line_list[ii+1]>warn_list[i]:
     msg=data[line_list[ii]:line_list[ii+1]].split("|")
     ret+="第"+str(count)+"次警告，"+"执行人为"+msg[1]+"，理由为"+msg[3]+"\n"
     count+=1
  return ret
