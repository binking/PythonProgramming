import sys, re, json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def loadTweets(fp):
    all_tweets = []
    for i, line in enumerate(fp.readlines()):
        try:
            tweet = json.loads(line)['text']
            all_tweets.append(tweet)
        except KeyError:
            pass   # Ignore deleted tweets, because they contributed nothing to count new term score
    return all_tweets
def loadTermScorePairs(fp):
    pairs = {}
    for line in fp.readlines():
        term, score = line.split('\t')
        pairs[term] = int(score)
    return pairs

def countNewTermsScore(list_of_tweets, term_score_pairs):
    re_exp = r'http://t\.co/[a-zA-Z0-9]+|[\@#&][a-zA-Z]+|\s+' # Remove url, and those strings starts with [@#&]
    new_terms_scores = {}; old_terms = set(term_score_pairs.keys())
    for tweet in list_of_tweets:
        score_of_this_tweet = 0
        seg_list = set(filter(None, re.split(re_exp, tweet))) # Remove empty string and change type to set for next operations on set
        #print "After parsing, ", seg_list
        new_terms = seg_list - old_terms # Filter new terms not in AFINN-txt
        for key in old_terms:
            if key in seg_list:
                score_of_this_tweet += term_score_pairs[key] # Calculate score of this tweet, and then assume new term's score is also this score
        for term in new_terms:
            new_terms_scores[term] = new_terms_scores.get(term, 0) + score_of_this_tweet  # Happy together. And accumulate scores of frequent terms
        #print score_of_this_tweet
    return new_terms_scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    term_score_pairs = loadTermScorePairs(sent_file)
    tweets = loadTweets(tweet_file)
    scores_of_new_terms = countNewTermsScore(tweets, term_score_pairs) 
    for key in scores_of_new_terms.keys():
        print key, scores_of_new_terms[key]
if __name__ == '__main__':
    main()
