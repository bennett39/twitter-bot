import random
import sys
from tqdm import tqdm
import tweepy

from secrets import consumer_key, consumer_secret, access_token, \
    access_token_secret

def main():
    """
    A program to favorite and reply to tweets that mention certain URLs
    Tutorial: https://bit.ly/2s2dtvS
    Tweepy docs: http://docs.tweepy.org/en/3.7.0/
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Change these Twitter URL ids to whatever you want to search for
    urls = ["url:ed8d13397c9c", "url:443940b8ef9f"]
    search_urls(api, urls)

    get_mentions(api)
    follow_back(api)


def search_urls(api, urls):
    """
    Uses Twitter standard search API to fetch tweets that reference a
    given URL. Docs: https://bit.ly/2lALpfQ

    For each tweet in the search, favorite and reply with a thank you.
    """
    users_thanked = []
    errors = 0
    for url in urls:
        num_tweets = 10
        for t in tqdm(tweepy.Cursor(api.search, url).items(num_tweets)):
            try:
                t.favorite()
                thank(api, t)
                t.user.follow()
                users_thanked.append(t.user.screen_name)
            except tweepy.TweepError:
                errors += 1
            except StopIteration:
                break

    print(f"Thanked {users_thanked}")
    print(f"{errors} tweets were already favorited", end="\n\n")


def thank(api, tweet):
    """
    Crafts a reply using the screen name and id of a given tweet. Choses
    a random thank you message as the reply.
    """
    t = ["Thanks for sharing my article!", \
            "Glad you liked the article!", \
            "Thanks for the tweet of my article!", \
            "Glad to hear you enjoyed my article!", \
            "I'm happy you liked the article enough to tweet it!", \
            "Thanks for the share! Glad you liked it!", \
            "I appreciate the tweet -- glad you enjoyed my article!",
            "Glad you liked the article enough to share it!", \
            "Appreciate you sharing my article!", \
            "Thanks for tweeting my article!"]
    thanks = random.choice(t)

    reply = "@" + tweet.user.screen_name + " " + thanks
    api.update_status(reply, tweet.id)


def get_mentions(api):
    """
    Finds mentions of the authenticated user and favorites them if they
    haven't been favorited already. Also follows all mentioners.
    """
    mentioners = []
    errors = 0

    mentions = api.mentions_timeline(count=10)
    for m in tqdm(mentions):
        try:
            m.favorite()
            m.user.follow()
            mentioners.append(m.user.screen_name)
        except tweepy.TweepError:
            errors += 1
        except StopIteration:
            break

    print(f"Followed mentioners: {mentioners}")
    print(f"{errors} users already followed", end="\n\n")


def follow_back(api):
    """
    Follows back the most recent ## users who follow the authenticated
    user. Change `.items(##)` to change the number of follow-backs.
    """
    follow_backs = []
    errors = 0

    for follower in tqdm(tweepy.Cursor(api.followers).items(10)):
        try:
            follower.follow()
            follow_backs.append(follower.screen_name)
        except tweepy.TweepError:
            errors += 1
        except StopIteration:
            break
    
    print(f"Followed back: {follow_backs}")
    print(f"{errors} users already followed", end="\n\n")


if __name__ == "__main__":
    main()
