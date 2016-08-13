import tweepy, json
from api import api

def read_timeline(items=10):
    for status in tweepy.Cursor(api.home_timeline).items(items):
        print json.dumps(status._json, indent=4)
def read_all_tweets():
    for tweet in tweepy.Cursor(api.user_timeline).items():
        print tweet.text

read_timeline(10)
read_all_tweets()
