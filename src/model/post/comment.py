from model.item import Item


class Comment(Item):
    def __init__(self, RAW_DATA: dict):
        super(Comment, self).__init__(RAW_DATA)

    @property
    def text(self) -> str:
        return self.RAW_DATA["text"]

    @property
    def parent(self) -> int:
        return self.RAW_DATA["parent"]

    @property
    def kids(self) -> list:
        if "kids" in self.RAW_DATA.keys():
            return self.RAW_DATA["kids"]
        return []

    @property
    def type(self) -> str:
        return self.RAW_DATA["type"]

    def __str__(self):
        return "Comment: {}".format(self.text)


"""
{
    "by": "norvig",
    "id": 2921983,
    "kids": [2922097, 2922429, 2924562, 2922709, 2922573, 2922140, 2922141],
    "parent": 2921506,
    "text": "Aw shucks, guys ... you make me blush with your compliments.<p>Tell you what, Ill make a deal: I'll keep writing if you keep reading. K?",
    "time": 1314211127,
    "type": "comment",
}
"""
