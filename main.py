from telegram.ext import Updater
from requests import get
from config import *


class Item:
    def __init__(self, link):
        self.link = link


class Dog(Item):
    def get(self):
        try:
            raw = get(self.link)
        except ConnectionError:
            print("Something gone wrong with the link")
        return raw.json()['message']


def main():
    global post

    post = Dog(SOURCES["dogs"]['link']).get()

    updater = Updater(TG_API, use_context=True)
    updater.start_polling()
    updater.bot.send_photo(chat_id=TG_CHANNEL, photo=post)
    updater.stop()


if __name__ == "__main__":
    main()

