import miraicle
from handleins import handle_ins
@miraicle.Mirai.receiver('GroupMessage')
def get_ins(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    if msg.plain[:1]=='？' and len(msg.plain.strip('？'))!=0:
        argv=msg.plain.splitlines()[0].split(' ',2)
        ins=msg.plain.split(' ',1)[0][1:]
        del argv[0]
        print(argv[0])
        if ins=="在线编译" :
         argv.append(msg.plain[msg.plain.find('\n')+1:])
        handle_ins(ins,argv,bot,msg.group)
                                                 
qq = 2192808879              # 你登录的机器人 QQ 号
verify_key = 'ServiceVerifyKey'     # 你在 setting.yml 中设置的 verifyKey
port = 8080                 # 你在 setting.yml 中设置的 port (http)

bot = miraicle.Mirai(qq=qq, verify_key=verify_key, port=port)
bot.run()

#？warn@xx #offoptic