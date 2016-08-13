import json, string
from collections import Counter, defaultdict
from tweets_preprocessor import preprocess

STOP_WORDS_FILE = "stopwords.txt"
TARGET_PERSON_FILE = "./json_file/hillary_tweets.json"
WORD_SCORES_FILE = "score_words.txt"

def load_stop_words():
    word_list = list(string.punctuation) + ["rt", "via", "gt", "lt", "“", "”", "…", "‘", "’"] # ignore quote sign
    # &gt is >; &lt is <
    with open(STOP_WORDS_FILE, "r") as fr:
        for word in fr.readlines():
            word_list.append(word.strip())
    return word_list

def get_word_score():
    word_score = {}
    with open(WORD_SCORES_FILE, "r") as fr:
        for line in fr.readlines():
            line = line.strip()
            word_score[line[:-2].strip()] = int(line[-2:])
    return word_score

def load_word_count(stopword=True):
    tweets_data = {}
    stop_words = load_stop_words()
    hillary = open(TARGET_PERSON_FILE, "r")

    for line in hillary.readlines():
        tweet = json.loads(line.strip())
        tweet_id = tweet["id"]
        tokens = preprocess(tweet["text"], True)

        if tweet["id"] not in hillary:
            if stopword:
                tokens = [token for token in tokens if token not in stop_words]
            tweets_data[tweet_id] =word_count(tokens)

    return tweets_data

def load_tweets():
    tweets_data = {}
    stop_words = load_stop_words()
    hillary = open(TARGET_PERSON_FILE, "r")

    for line in hillary.readlines():
        tweet = json.loads(line.strip())
        tweet_id = tweet["id"]
        text = tweet["text"]

        if tweet["id"] not in hillary:
            tweets_data[tweet_id] = text
    return tweets_data


def word_count(token):
    word_counts = Counter()
    word_counts.update(token)
    return dict(word_counts)

def term_frequency_count(list_of_tokens):
    counter = Counter()
    for tokens in list_of_tokens:
        counter.update(tokens)
    return counter

def calculate_score(tweet):
    # tweet can be string or list
    word_scores = get_word_score()
    score = 0
    if isinstance(tweet, str):
        # Given tweet string, count it's sentiment score
        for word in word_scores:
            if word in tweet:
                score += word_scores[word]
    elif isinstance(tweet, dict):
        for word in tweet:
            score += word_scores.get(word, 0) * tweet[word]
    else:
        print("Unkown type")
    return score

def count_cooccurences(word_count):
    '''
        input: {id: {word: count}}
    '''
    joint_mat = defaultdict(lambda: defaultdict(int))
    for tweet_id in word_count:
        tokens = [token for token in word_count[tweet_id].keys() if not token.startswith(("#", "@"))]
        for i in range(len(tokens)):
            for j in range(i + 1, len(tokens)):
                w1, w2 = sorted((tokens[i], tokens[j]))
                if w1 != w2:
                    joint_mat[w1][w2] += 1
    return joint_mat

def score_count(tweets_data):
    '''
        input: {id: tweet/tokens}
        output: {id: sentiment_score}
    '''
    score_count = {}
    for tweet_id in tweets_data:
        # import ipdb; ipdb.set_trace()
        score = calculate_score(tweets_data[tweet_id])
        score_count[tweet_id] = score
    return score_count

if __name__ == "__main__":
    word_count = load_word_count()
    print("5 most frequent words without stopwords are:")
    print(term_frequency_count(word_count.values()).most_common(10))
    #data_with_st = load_word_count(stopword=False)
    #print "5 most frequent words contains stopwords are:"
    #print term_frequency_count(data_with_st.values()).most_common(10)
    print("*"*20, "5 example tweets", "*"*20)
    for tweet_id in list(word_count.keys())[:5]:
        print(word_count[tweet_id])

    scores_of_words = get_word_score()
    print("\n", "*"*20, "Worst 10 words", "*"*20)
    print(sorted(scores_of_words.items(), key=lambda x:x[1])[:10])
    print("*"*20, "Best 10 words", "*"*20)
    print(sorted(scores_of_words.items(), key=lambda x:x[1])[-10:])

    tweets = load_tweets()
    scores_of_tweets_1 = score_count(tweets)
    scores_of_tweets_2 = score_count(word_count)
    print("\n", "-"*20, "Method 2", "-"*20)
    print("*"*20, "10 Most Best Tweets about Hillary Clinton", "*"*20)
    id_of_sorted_tweets = sorted(scores_of_tweets_2.items(), key=lambda x:x[1])
    for tweet_id, score in id_of_sorted_tweets[-10:]:
        print(tweet_id, score, tweets[tweet_id])
    print("*"*20, "10 Most Worst Tweets about Hillary Clinton","*"*20)
    for tweet_id, score in id_of_sorted_tweets[:10]:
        print(tweet_id, score, tweets[tweet_id])

    print("\n", "-"*20, "Method 2", "-"*20)
    print("*"*20, "10 Most Best Tweets about Hillary Clinton", "*"*20)
    id_of_sorted_tweets = sorted(scores_of_tweets_1.items(), key=lambda x:x[1])
    for tweet_id, score in id_of_sorted_tweets[-10:]:
        print(tweet_id, score, tweets[tweet_id])
    print("*"*20, "10 Most Worst Tweets about Hillary Clinton","*"*20)
    for tweet_id, score in id_of_sorted_tweets[:10]:
        print(tweet_id, score, tweets[tweet_id])

    print("\n\nCalculate cooccurence matrix")
    print(count_cooccurences(word_count))
