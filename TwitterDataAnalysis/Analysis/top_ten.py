import json, sys#, operator

def loadHashTags(fp):
    hashTags = []
    for line in fp.readlines():
        try:
            tag_dicts = json.loads(line)['entities']['hashtags']
            for tag in tag_dicts:
                hashTags.append(tag['text'])
        except KeyError: 
            pass # Ignore deleted tweets, because they contributed nothing to count new term score
    return hashTags

def top_ten_hashtags(hashtags):
    pairs = {}
    for tag in set(hashtags):
        pairs[tag] = hashtags.count(tag)
    #top_10_tags = sorted(pairs, key=lambda key:pairs[key], reverse=True)[:10]
    #print top_10_tags
    #return {k:pairs[k] for k in top_10_tags}
    top_10_tags = sorted(pairs.items(), key=lambda x:x[1], reverse=True)[:10]
    #print top_10_tags
    #top_10_tags = sorted(pairs.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]
    #print top_10_tags
    return top_10_tags

def main():
    tweet_file = open(sys.argv[1], 'r')
    hashtags = loadHashTags(tweet_file)
    top_ten = top_ten_hashtags(hashtags)
    for tag in top_ten:
        print tag[0], tag[1]

if __name__=='__main__':
    main()
