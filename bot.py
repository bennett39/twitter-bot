# A program to favorite tweets that mention certain URLs
# Tutorial: https://bit.ly/2s2dtvS
# Tweepy docs: http://docs.tweepy.org/en/3.7.0/

import sys
import tweepy
from secrets import consumer_key, consumer_secret, access_token, \
    access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Change these Twitter URL ids to whatever you want to search for
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
