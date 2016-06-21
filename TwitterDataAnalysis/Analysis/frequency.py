import re, json, sys

def loadTweets(fp):
    all_tweets = []
    for line in fp.readlines():
        try:
            tweet = json.loads(line)['text']
            all_tweets.append(tweet)
        except KeyError:
            pass
    return all_tweets

def getVocal(tweets):
    vocalburary = set()
    re_exp = r'http://t\.co/[a-zA-Z0-9]+|[\@#&][a-zA-Z]+|\s+'
    for tweet in tweets:
        seg_list = set(filter(None, re.split(re_exp, tweet)))
        vocalburary = vocalburary | seg_list
    return vocalburary

def calcFreq(tweets):
    terms_freq_pairs = {}
    re_exp = r'http://t\.co/[a-zA-Z0-9]+|[\@#&][a-zA-Z]+|\s+'
    for tweet in tweets:
        seg_list = filter(None, re.split(re_exp, tweet))
        for term in seg_list:
            terms_freq_pairs[term] = terms_freq_pairs.get(term, 0) + seg_list.count(term)
    all_occurences = sum(terms_freq_pairs.values())
    for key in terms_freq_pairs:
        terms_freq_pairs[key] = terms_freq_pairs[key]*1.0/all_occurences
    return terms_freq_pairs

def main():
    tweet_file = open(sys.argv[1], 'r')
    tweets = loadTweets(tweet_file)
    terms_frequency_pairs = calcFreq(tweets)
    for key in terms_frequency_pairs.keys():
        print key, terms_frequency_pairs[key]

if __name__=='__main__':
    main()
