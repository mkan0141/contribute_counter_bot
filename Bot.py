from concat import *

if __name__ == '__main__':
    bot = ConCat()
    data = bot.get_contributes()
    bot.todays_contribute(data)
    print(bot.month_contribute(data))
    bot.tweet(data)
