import sys
import tweepy
from secrets import consumer_key, consumer_secret, access_token, \
    access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

urls = ["url:ed8d13397c9c", "url:443940b8ef9f"]

for url in urls:
    search = url
    numberOfTweets = 100
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.favorite()
            print('Favorited a tweet')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break