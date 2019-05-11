from tqdm import tqdm
import tweepy

from config import api

def main():
    """ Unfollows users who don't follow me. """
    count = 0
    followers = api.followers_ids('bennettgarner')
    friends = api.friends_ids('bennettgarner')
    for friend in tqdm(friends):
        if friend not in followers:
            prompt = input(f"Unfollow {api.get_user(friend).screen_name}? y/n: ")
            if prompt == 'Y' or prompt == 'y':
                count += 1
                api.destroy_friendship(friend)
    print(f"Unfollowed {count} users.")

if __name__ == "__main__":
    main()
