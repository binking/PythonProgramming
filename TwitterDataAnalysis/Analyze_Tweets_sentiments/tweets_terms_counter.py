import operator, json
from collections import Counter
from tweets_processor import preprocess

def load_stop_words():
	word_list = list(string.punctuation) + ["rt", "via"]
	with open("stopwords.txt", "r") as fr:
		for word in fr.readlines():
			word_list.append(word.strip())
	return word_list

def count_terms_frequency(tweets):
	word_bag = Counter()
	stop_words = load_stop_words()
	for tweet in tweets:
		tokens = [term for term in preprocess(tweet, True) if term not in stop_words]
		word_bag.update(tokens)
	print word_bag.most_common(5)
	return dict()

def main():
	filename = "trump_tweets.json"
	with(open(filename, "r")) as fr:
		for line in fr.readlines():
			tweet = json.loads(line.strip())
			tweets.append(tweet["text"])