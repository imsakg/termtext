import requests
import json


class Parser(object):
    def __init__(self, *args):
        super(Parser, self).__init__(*args)

        self.URL_BASE = "https://hacker-news.firebaseio.com/v0/"
        self.URL_TOPSTORIES = self.URL_BASE + "topstories.json"
        self.URL_BESTSTORIES = self.URL_BASE + "beststories.json"
        self.URL_NEWSTORIES = self.URL_BASE + "newstories.json"
        self.URL_ASKSTORIES = self.URL_BASE + "askstories.json"
        self.URL_SHOWSTORIES = self.URL_BASE + "showstories.json"
        self.URL_JOBSTORIES = self.URL_BASE + "jobstories.json"
        self.URL_UPDATES = self.URL_BASE + "updates.json"
        self.URL_MAXITEM = self.URL_BASE + "maxitem.json"

        self.HN_MAX_ITEM = self.max_itemID

    def URL_ITEM(self, item_id):
        return self.URL_BASE + "/item/" + str(item_id) + ".json"

    def URL_USER(self, user_id):
        return self.URL_BASE + "/user/" + str(user_id) + ".json"

    def get_topstories(self):
        RESPONSE = requests.get(self.URL_TOPSTORIES)
        return RESPONSE.json()

    def get_beststories(self):
        RESPONSE = requests.get(self.URL_BESTSTORIES)
        return RESPONSE.json()

    def get_newstories(self):
        RESPONSE = requests.get(self.URL_NEWSTORIES)
        return RESPONSE.json()

    def get_askstories(self):
        RESPONSE = requests.get(self.URL_ASKSTORIES)
        return RESPONSE.json()

    def get_showstories(self):
        RESPONSE = requests.get(self.URL_SHOWSTORIES)
        return RESPONSE.json()

    def get_jobstories(self):
        RESPONSE = requests.get(self.URL_JOBSTORIES)
        return RESPONSE.json()

    def get_updates(self):
        RESPONSE = requests.get(self.URL_UPDATES)
        return RESPONSE.json()

    @property
    def max_itemID(self):
        RESPONSE = requests.get(self.URL_MAXITEM)
        return int(RESPONSE.text)

    def get_item(self, item_id):
        RESPONSE = requests.get(self.URL_ITEM(item_id))
        return RESPONSE.json()

    def get_user(self, user_id):
        RESPONSE = requests.get(self.URL_USER(user_id))
        return RESPONSE.json()

    def get_item_comments(self, item_id):
        item = self.get_item(item_id)
        if "kids" in item:
            for kid in item["kids"]:
                yield self.get_item(kid)
        else:
            return None

    def get_user_comments(self, user_name):
        user = self.get_user(user_name)
        if "submitted" in user:
            for item_id in user["submitted"]:
                for comment in self.get_item_comments(item_id):
                    yield comment
        else:
            return None

        # return list(map(lambda item_id: self.URL_ITEM(self, item_id), RESPONSE.json()))
