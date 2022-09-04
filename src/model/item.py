from peewee import *


class Item(Model):
    def __init__(self, RAW_DATA: dict):
        super(Item, self).__init__()
        self.RAW_DATA = RAW_DATA

    @property
    def id(self) -> int:
        return self.RAW_DATA["id"]

    @property
    def by(self) -> str:
        return self.RAW_DATA["by"]

    @property
    def time(self) -> int:
        return self.RAW_DATA["time"]

    @property
    def type(self) -> str:
        return self.RAW_DATA["type"]
