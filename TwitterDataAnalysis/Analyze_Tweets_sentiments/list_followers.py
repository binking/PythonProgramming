import json, tweepy
from api import api

def list_followers():
    for friend in tweepy.Cursor(api.friends).items():
        print json.dumps(friend._json, indent=4)

list_followers()
