import sys
import tweepy
import json

consumer_key = ".........."
consumer_secret = ".........."
access_token = ".........."
access_token_secret = ".........."

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Where On Earth ID for India is 23424848.
INDIA_WOE_ID = 23424848

india_trends = api.trends_place(INDIA_WOE_ID)

trends = json.loads(json.dumps(india_trends, indent=1))

for trend in trends[0]["trends"]:
	print((trend["name"]).strip("#"))