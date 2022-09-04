from tools.parser import Parser
from model.post.story import Story

Parser = Parser()


posts = []
top_items = Parser.get_beststories()

for i, post in enumerate(Parser.get_item(top_items[0])):
    posts.append(Post(post))
    if i > 3:
        break

for post in posts:
    print(post.RAW_DATA)
    print(post.id)
    print(post.by)
    print(post.text)
    print(post.time)
    print(post.parent)
    print(post.type)

    print("\nend\n")
