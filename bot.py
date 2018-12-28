PYTHONIOENCODING='utf8'

import sys
import tweepy
from secrets import consumer_key, consumer_secret, access_token, \
    access_token_secret

print(sys.stdout.encoding)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
