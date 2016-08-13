from api import auth
import json
from tweepy import Stream
from tweepy.streaming import StreamListener

class BrexitListener(StreamListener):
    def on_data(self, data):
        try:
            with open("brexit_tweets.json", 'a') as f:
                f.write(data)
        except BaseException as e:
            print "Error on_data(): %s " % str(e)
            return True
    def on_error(self, status):
        print(status)
        return True

brexit_listener = Stream(auth, BrexitListener())
brexit_listener.filter(track=['Brexit'])
