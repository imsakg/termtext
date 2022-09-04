from tools.parser import Parser
from model.post.comment import Comment

Parser = Parser()


comments = []
for i, comment in enumerate(Parser.get_user_comments("theturtletalks")):
    comments.append(Comment(comment))
    if i > 3:
        break

for comment in comments:
    print(comment.RAW_DATA)
    print(comment.id)
    print(comment.by)
    print(comment.text)
    print(comment.time)
    print(comment.parent)
    print(comment.type)
    print(comment.kids)

    print("end\n")
