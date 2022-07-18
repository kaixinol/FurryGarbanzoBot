import pydoodle
def Compile(script: str,lang: str,config: dict):
    c = pydoodle.Compiler(clientId=config["plugin"]["OnlineCompile"]["id"],
                      clientSecret=config["plugin"]["OnlineCompile"]["secret"])
    result = c.execute(script, lang)
    return result.output