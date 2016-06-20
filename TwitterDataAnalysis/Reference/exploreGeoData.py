import json

lines = open('1000_tweets_2.json', 'r').readlines()
for line in lines:
    tweet = json.loads(line)
    place = tweet.get('place', None)
    if place:
        print place['name']