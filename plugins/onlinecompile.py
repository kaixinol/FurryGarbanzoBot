import pydoodle
def Compile(script: str,lang: str,config: dict):
    c = pydoodle.Compiler(clientId=config["id"],
                      clientSecret=config["secret"])
    result = c.execute(script, lang)
    return result.output