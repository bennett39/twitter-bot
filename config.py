from dotenv import load_dotenv
import os
import tweepy

load_dotenv()
auth = tweepy.OAuthHandler(
        os.getenv('CONSUMER_KEY'),
        os.getenv('CONSUMER_SECRET')
    )
auth.set_access_token(
        os.getenv('ACCESS_TOKEN'),
        os.getenv('ACCESS_TOKEN_SECRET')
    )
api = tweepy.API(auth)
