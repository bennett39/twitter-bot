from random import choice
from tqdm import tqdm
import tweepy

from config import api, urls

def main():
    """
    A program to favorite and reply to tweets that mention certain URLs
    Tutorial: https://bit.ly/2s2dtvS
    Tweepy docs: http://docs.tweepy.org/en/3.7.0/
    """
    # Change these Twitter URL ids to whatever you want to search for
    urls = [
        "url:ed8d13397c9c",
        "url:443940b8ef9f",
        "url:a1e4012eb859",
        "url:1ee617ed46af",
        "url:fb83ab848c6",
        "url:2247efc1eaac",
    ]
    search_urls(api, urls)
    get_mentions(api)
    follow_back(api)
    unfollow(api)


def search_urls(api, urls):
    """
    Uses Twitter standard search API to fetch tweets that reference a
    given URL. Docs: https://bit.ly/2lALpfQ

    For each tweet in the search, favorite and reply with a thank you.
    """
    users_thanked = []
    errors = 0
    for url in tqdm(urls):
        num_tweets = 30
        for tweet in tqdm(tweepy.Cursor(api.search, url).items(num_tweets)):
            try:
                if tweet.user.screen_name != 'bennettgarner':
                    tweet.favorite()
                    thank(api, tweet)
                    tweet.user.follow()
                    users_thanked.append(tweet.user.screen_name)
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
    thank_you_messages = [
            "Thanks for sharing my article!",
            "Glad you liked the article!",
            "Thanks for the tweet of my article!",
            "Glad to hear you enjoyed my article!",
            "I'm happy you liked the article enough to tweet it!",
            "Thanks for the share! Glad you liked it!",
            "I appreciate the tweet -- glad you enjoyed my article!",
            "Glad you liked the article enough to share it!",
            "Appreciate you sharing my article!",
            "Thanks for tweeting my article!"
        ]
    message = choice(thank_you_messages)
    try:
        reply = "@" + tweet.user.screen_name + " " + message
        api.update_status(reply, tweet.id)
    except tweepy.TweepError as e:
        print(e)


def get_mentions(api):
    """
    Finds mentions of the authenticated user and favorites them if they
    haven't been favorited already. Also follows all mentioners.
    """
    mentioners = []
    errors = 0
    mentions = api.mentions_timeline(count=10)
    for mention in tqdm(mentions):
        try:
            mention.favorite()
            mention.user.follow()
            mentioners.append(mention.user.screen_name)
        except tweepy.TweepError:
            errors += 1
        except StopIteration:
            break
    print(f"Followed mentioners: {mentioners}")
    print(f"{errors} users already followed", end="\n\n")


def follow_back(api):
    """
    Follows back the most recent ## users who follow the authenticated
    user. Change .items(##) to change the number of follow-backs.
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
