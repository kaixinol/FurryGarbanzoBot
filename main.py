import miraicle
import os
import json
from handleins import handle_ins
global ConfigData
global load_dict

@miraicle.Mirai.receiver('GroupMessage')
def get_ins(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    if msg.plain=="帮助" or msg.plain=="？帮助":
     bot.send_group_msg(msg.group, msg=[miraicle.Plain('项目文档地址:https://github.com/kaixinol/FurryGarbanzoBot/docs')])
     return
    if msg.plain[:1]=='？' and len(msg.plain.strip('？'))!=0:
        argv=msg.plain.splitlines()[0].split(' ',2)
        ins=msg.plain.split(' ',1)[0][1:]
        del argv[0]
        if ins=="在线编译" :
         argv.append(msg.plain[msg.plain.find('\n')+1:])
        handle_ins(ins,argv,bot,msg,ConfigData,load_dict)
                                                 

qq = 2634732881              # 你登录的机器人 QQ 号
verify_key = 'ServiceVerifyKey'     # 你在 setting.yml 中设置的 verifyKey
port = 8080                 # 你在 setting.yml 中设置的 port (http)


with open(r"config\config.json", encoding='utf-8') as file_obj:
 ConfigData = json.loads(file_obj.read())
with open(r"config\group_setting.json", encoding='utf-8') as file_o:
 load_dict = json.loads(file_o.read())
bot = miraicle.Mirai(qq=qq, verify_key=verify_key, port=port)
bot.run()

