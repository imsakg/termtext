from model.item import Item


class Story(Item):
    def __init__(self, RAW_DATA: dict):
        super(Story, self).__init__(RAW_DATA=RAW_DATA)

    @property
    def title(self) -> str:
        return self.RAW_DATA["title"]

    @property
    def url(self) -> str:
        return self.RAW_DATA["url"]

    @property
    def text(self) -> str:
        return self.RAW_DATA["text"]

    @property
    def kids(self) -> list:
        if "kids" in self.RAW_DATA.keys():
            return self.RAW_DATA["kids"]
        return []

    @property
    def score(self) -> int:
        return self.RAW_DATA["score"]

    @property
    def descendants(self) -> int:
        return self.RAW_DATA["descendants"]

    def __str__(self):
        return "Post: {}".format(self.title)


"""
{
  "by" : "dhouston",
  "descendants" : 71,
  "id" : 8863,
  "kids" : [ 8952, 9224, 8917, 8884, 8887, 8943, 8869, 8958, 9005, 9671, 8940, 9067, 8908, 9055, 8865, 8881, 8872, 8873, 8955, 10403, 8903, 8928, 9125, 8998, 8901, 8902, 8907, 8894, 8878, 8870, 8980, 8934, 8876 ],
  "score" : 111,
  "time" : 1175714200,
  "title" : "My YC app: Dropbox - Throw away your USB drive",
  "type" : "story",
  "url" : "http://www.getdropbox.com/u/2/screencast.html"
}
"""
