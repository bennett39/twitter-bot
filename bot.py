# A program to favorite and reply to tweets that mention certain URLs
# Tutorial: https://bit.ly/2s2dtvS
# Tweepy docs: http://docs.tweepy.org/en/3.7.0/

import sys
import tweepy
import random

from secrets import consumer_key, consumer_secret, access_token, \
    access_token_secret

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Change these Twitter URL ids to whatever you want to search for
    urls = ["url:ed8d13397c9c", "url:443940b8ef9f"]
    search_urls(api, urls)


def search_urls(api, urls):
    for url in urls:
        number_of_tweets = 3
        for tweet in tweepy.Cursor(api.search, url).items(number_of_tweets):
            try:
                tweet.favorite()
                thank(api, tweet)
                print("Favorited and thanked " + tweet.user.screen_name)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break


def thank(api, tweet):
    t = ["Thanks for sharing my article!", \
            "Glad you liked the article!", \
            "Thanks for the tweet of my article!", \
            "Glad to hear you enjoyed my article!", \
            "I'm happy you liked the article enough to tweet it!", \
            "Thanks for the share! Glad you liked it!", \
            "I appreciate the tweet -- glad you enjoyed my article!",
            "Glad you liked the article enough to share it!", \
            "Appreciate you sharing my article!"]
    thanks = random.choice(t)

    reply = "@" + tweet.user.screen_name + " " + thanks
    api.update_status(reply, tweet.id)


if __name__ == "__main__":
    main()
