import json

def extract_id_from_json(file_handle):
    tweets_ids = []
    for line in file_handle.readlines():
        tweet_info = json.loads(line)
        if len(tweet_info) == 1:
            tweets_ids.append(tweet_info['delete']['status']['id'])
        else:
            tweets_ids.append(tweet_info['id'])
    return tweets_ids

def compareDifference(ids_1, ids_2):
    ids_set_1 = set(ids_1)
    ids_set_2 = set(ids_2)
    # Intersection means common ids
    print("In first ids set, ", len(ids_set_1))
    print("In second ids set, ", len(ids_set_2))
    print("There are %d common elements" % len(ids_set_1 & ids_set_2))

def main():
    ids_1 = extract_id_from_json(open('1000_tweets_1.json', 'r'))
    ids_2 = extract_id_from_json(open('1000_tweets_2.json', 'r'))
    print("In first ids list, ", len(ids_1))
    print("In second ids list, ", len(ids_2))
    compareDifference(ids_1, ids_2)

if __name__=='__main__':
    main()