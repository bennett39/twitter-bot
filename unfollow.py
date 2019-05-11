from tqdm import tqdm
import tweepy

from config import api


followers = set(api.followers_ids('bennettgarner'))
friends = api.friends_ids('bennettgarner')
influencers = {
    70345946, 3320010078, 139186916, 1668100142, 21292523, 599755262,
    5676102, 517021184, 14587429, 819717383975739392, 861320851,
    110770469, 35402769, 4462823079, 191225303, 14561327, 17060015,
    3167257102, 40303245, 44196397, 1344951, 1077967285971836928,
    564919357, 310897418
}
unfollowing = [f for f in friends if f not in followers and f not in influencers]
for u in unfollowing:
    prompt = input(f"Unfollow {api.get_user(u).screen_name}? y/n: ")
    if prompt == 'Y' or prompt == 'y':
        api.destroy_friendship(u)
print(f"Unfollowed {len(unfollowing)} users.")
