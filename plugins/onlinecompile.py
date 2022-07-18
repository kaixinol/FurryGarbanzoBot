import pydoodle
def Compile(script: str,lang: str):
    c = pydoodle.Compiler(clientId="*",
                      clientSecret="*")
    result = c.execute(script, lang)
    return result.output