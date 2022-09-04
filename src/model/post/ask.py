from model.item import Item


class Ask(Item):
    def __init__(self, RAW_DATA: dict):
        super(Ask, self).__init__(RAW_DATA)

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

    def __str__(self):
        return "Ask: {}".format(self.text)


"""
{
    "by": "tel",
    "descendants": 16,
    "id": 121003,
    "kids": [121016, 121109, 121168],
    "score": 25,
    "text": "<i>or</i> HN: the Next Iteration<p>I get the impression that with Arc being released a lot of people who never had time for HN before are suddenly dropping in more often. (PG: what are the numbers on this? I'm envisioning a spike.)<p>Not to say that isn't great, but I'm wary of Diggification. Between links comparing programming to sex and a flurry of gratuitous, ostentatious  adjectives in the headlines it's a bit concerning.<p>80% of the stuff that makes the front page is still pretty awesome, but what's in place to keep the signal/noise ratio high? Does the HN model still work as the community scales? What's in store for (++ HN)?",
    "time": 1203647620,
    "title": "Ask HN: The Arc Effect",
    "type": "story",
}
"""
