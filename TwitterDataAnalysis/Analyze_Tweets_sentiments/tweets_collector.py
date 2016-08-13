from api import auth
import json, sys
from tweepy import Stream
from tweepy.streaming import StreamListener
KEY_WORD = u"Rio"
class BrexitListener(StreamListener):
    def on_data(self, data):
        try:
            with open("json_file/%s_tweets.json" % u"Rio", 'w+') as f:
                f.write(data)
        except BaseException as e:
            print "Error on_data(): %s " % str(e)
            return True
    def on_error(self, status):
        print(status)
        return True

def collect_tweets_by_word(word):
    brexit_listener = Stream(auth, BrexitListener())
    brexit_listener.filter(track=[word])

def main():
    print "Collect tweets according to %s ....." % KEY_WORD
    try_times = 0
    RETRY_TIME = 5
    while True:
        try:
            try_times += 1
            if try_times > 5:
                break
            collect_tweets_by_word(KEY_WORD)
        except:
            print "Error, try more %d times" % (RETRY_TIME - try_times)


if __name__=="__main__":
    main()
