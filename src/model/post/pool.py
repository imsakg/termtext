from model.item import Item


class Pool(Item):
    def __init__(self, RAW_DATA: dict):
        super(Pool, self).__init__(RAW_DATA)

    @property
    def kids(self) -> list:
        if "kids" in self.RAW_DATA.keys():
            return self.RAW_DATA["kids"]
        return []

    @property
    def score(self) -> int:
        return self.RAW_DATA["score"]

    @property
    def text(self) -> str:
        return self.RAW_DATA["text"]

    @property
    def title(self) -> str:
        return self.RAW_DATA["title"]

    @property
    def parts(self) -> list:
        if "parts" in self.RAW_DATA.keys():
            return self.RAW_DATA["parts"]
        return []

    @property
    def descendants(self) -> int:
        return self.RAW_DATA["descendants"]

    def __str__(self):
        return "Pool: {}".format(self.text)


"""
{
    "by" : "pg",
    "descendants" : 54,
    "id" : 126809,
    "kids" : [ 126822, 126823, 126993, 126824, 126934, 127411, 126888, 127681, 126818, 126816, 126854, 127095, 126861, 127313, 127299, 126859, 126852, 126882, 126832, 127072, 127217, 126889, 127535, 126917, 126875 ],
    "parts" : [ 126810, 126811, 126812 ],
    "score" : 46,
    "text" : "",
    "time" : 1204403652,
    "title" : "Poll: What would happen if News.YC had explicit support for polls?",
    "type" : "poll"
}
"""
