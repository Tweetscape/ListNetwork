# Import packages for scraping Twitter data
import tweepy
import time

# Import relevant authorization information
import config

def config_auth():
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.key, config.secret)
    api = tweepy.API(auth)
    return api

def get_members(api, slug, owner):
    lst = api.list_members(slug = slug, owner_screen_name = owner, count = 100)
    ids_ = []
    names = []
    screen_names = []

    for member in lst:
        ids_.append(member.id)
        names.append(member.name)
        screen_names.append(member.screen_name)

    members = zip(ids_, names, screen_names)

    return list(members)

def check_friendships(api, users):
    friendships = []
    for i in range(0, len(users)):
        for j in range(i + 1, len(users)):
            try:
                friendship = api.show_friendship(source_screen_name = users[i],
                                                 target_screen_name = users[j])
                friendships.append([users[i], users[j],
                                    friendship[0].followed_by, # i followed by j 
                                    friendship[0].following])  # i following j
                print(i, j)
                time.sleep(5) # 5 second timer because 180 calls per 15 minutes = 12 calls/minute
            except:
                print("Waiting 15 minutes for API limit to reset.")
                time.sleep(900) # wait for 15 minutes

    return friendships
