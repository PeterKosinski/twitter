import json

results = []

tweets_file = open('tweet_mining.json',"r")
for tweet_line in tweets_file:
    try:
        status = json.loads(tweet_line)
        results.append(status)
    except:
        continue

new_ht = set()

for tweet in results:
    hashtags = tweet['entities']['hashtags']
    print(hashtags)
    for ht in hashtags:
        print(ht["text"])

