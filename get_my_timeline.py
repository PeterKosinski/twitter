import tweepy
import json
from auth import get_api  

api = get_api()

def get_by_search(query, count):
    return tweepy.Cursor(api.search, q=query).items(count)

def get_my_timeline(count):
    return tweepy.Cursor(api.home_timeline).items(count)


def get_my_timeline(count):
    return tweepy.Cursor(api.home_timeline).items(count)

for status in get_my_timeline(1):
    print(status)