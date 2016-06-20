# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = "4567647824-zUOChj4BWkDNia3Rd0fIgrHbLGnM0rai1C2ITzy" # 'YOUR ACCESS TOKEN"'
ACCESS_SECRET = "HQhI0oVRymS5dr1waI3Fnr3GK7hsrsFU2li12q7ORmaUb" # 'YOUR ACCESS TOKEN SECRET'
CONSUMER_KEY = "B1uB90Z0CpcaFmzkeJ9NHqOYh"
CONSUMER_SECRET = "2eCI6Y3pPwt3ObPBYpru08VvWgJndLqQx7Y96i3EYt5O551Lid" # 'ENTER YOUR API SECRET'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)
# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()
# Print each tweet in the stream to the screen
# Here we set it to stop after getting 1000 tweets.
# You don't have to set it to stop, but can continue running
# the Twitter API to collect data for days or even longer.
tweet_count = 1000
fr = open('1000_tweets_2.json', 'w')
#print type(iterator) # <type 'generator'>
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print tweet_count
    fr.write(json.dumps(tweet) + '\n')
    #print json.dumps(tweet)
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
    if tweet_count <= 0:
        break
