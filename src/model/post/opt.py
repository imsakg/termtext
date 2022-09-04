from model.item import Item


class Opt(Item):
    def __init__(self, RAW_DATA: dict):
        super(Opt, self).__init__(RAW_DATA)

    @property
    def parent(self) -> int:
        return self.RAW_DATA["pool"]

    @property
    def score(self) -> int:
        return self.RAW_DATA["score"]

    @property
    def text(self) -> str:
        return self.RAW_DATA["text"]

    def __str__(self):
        return "Opt: {}".format(self.text)


"""
{
    "by": "pg",
    "id": 160705,
    "poll": 160704,
    "score": 335,
    "text": "Yes, ban them; I'm tired of seeing Valleywag stories on News.YC.",
    "time": 1207886576,
    "type": "pollopt",
}
"""
