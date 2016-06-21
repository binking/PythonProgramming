import sys, json
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

def loadTermScorePairs(fp):
    #fr = open(filename, 'r')
    pairs = {}
    for line in fp.readlines():
        term, score = line.split('\t')
        pairs[term] = int(score)
    #print(pairs.items())
    return pairs

def loadTweets(fp):
    #fr = open(filename, 'r')
    all_tweets = []
    for i, line in enumerate(fp.readlines()):  # Ignore first line whose key is delete
        try:
            tweet = json.loads(line)['text']
            #print(i, tweet)
            #seg_list = tweet.split('\t')
            all_tweets.append(tweet)
        except KeyError, e:
            all_tweets.append('') # The tweet was deleted
    return all_tweets

def countScores(tweets, pairs):
    # pairs is a dict, tweets is list of string; res is list of score
    res = []
    for tweet in tweets:
        score_of_this_tweet = 0
        seg = tweet.split() # only analyze sentiment of English
        for key in pairs.keys():
            if key in seg:
                score_of_this_tweet += pairs[key]
        print score_of_this_tweet
        res.append(score_of_this_tweet)
        # for s in seg:
        #     score_of_this_tweet += pairs.get(s, 0)
    return res

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1], 'r')
    tweet_file = open(sys.argv[2], 'r')
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    #sent_file.seek(0); tweet_file.seek(0) # Let the file handler back to beginning
    term_score_pairs = loadTermScorePairs(sent_file)
    tweets = loadTweets(tweet_file)
    scores_of_tweets = countScores(tweets, term_score_pairs)
    #print(len(scores_of_tweets))
    #print(scores_of_tweets[:50])
    #print("There are so many tweets : ", len(tweets))

if __name__ == '__main__':
    main()
