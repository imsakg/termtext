from tools.parser import Parser

Parser = Parser()
for i in Parser.get_user_comments("theturtletalks"):
    print(i)
