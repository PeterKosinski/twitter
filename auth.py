import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'LB991zGxgIC69h1dyTMBGcWLJ'
CONSUMER_SECRET = 'o8P0sd5p0MNmEZvrNedaDE0eRpOeKYShPJlhYRxvILxyMrC248'
OAUTH_TOKEN = '1066599367-DMrl7TCxfYQn3W0JmwIqUQmP9Y4lSLSRB99UWJ3'
OAUTH_TOKEN_SECRET = 'F47Ezops7TAzDgzHXvMe8o19w16nHQoZl07oEANDnGkEY'
MONGODB_URI ="mongodb://root:password@ds127375.mlab.com:27375/tweets"

def get_auth():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return auth

def get_api():
    auth = get_auth()
    return tweepy.API(auth)