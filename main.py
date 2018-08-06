import re
import requests
import twitter
import datetime

from config import *

class Bot():
    def __init__(self):
        self.auth = twitter.OAuth(consumer_key=CONSUMER_KEY,
                                consumer_secret=CONSUMER_KEY_SECRET,
                                token=ACCESS_TOKEN,
                                token_secret=ACCESS_TOKEN_SECRET)
        self.twitter = twitter.Twitter(auth=self.auth)
        self.user_id=GITHUB_USER_ID
        self.day = datetime.date.today().day
        self.month = datetime.date.today().month

    def get_contributes(self):
        url = "https://github.com/users/" + self.user_id + "/contributions"
        response = requests.get(url)
        data = response.text.split('\n')
        return [int(re.findall('data-count="([0-9]+)"', x)[0]) for x in data if re.findall('data-count="([0-9]+)"', x)]

    def todays_contribute(self, contributes):
        print(contributes[-1])
        return contributes[-1]

    def month_contribute(self, contributes):
        today = -datetime.date.today().day
        return sum(contributes[today:])

    def tweet(self, contributes):
        tc = self.todays_contribute(contributes)
        mc = self.month_contribute(contributes)
        """
        tweet_text = str(self.month)" + "/" + str(self.day) + "のcontribute数: " + str(tc) + "\n" + \
                str(self.month) + "月の総contribute数: " + str(mc) + "\n"
        """
        tweet_text = "[テスト中]" + '\n' + \
                str(self.month) + "/" + str(self.day) + "のcontribute数: " + str(tc) + "\n" + \
                str(self.month) + "月の総contribute数: " + str(mc) + "\n"
        self.twitter.statuses.update(status=tweet_text)


if __name__ == '__main__':
    bot = Bot()
    data = bot.get_contributes()
    bot.todays_contribute(data)
    print(bot.month_contribute(data))
    bot.tweet(data)

