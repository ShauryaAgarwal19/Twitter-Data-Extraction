import tweepy
import csv
import pandas as pd

consumer_key = ".............................."
consumer_secret = ".............................."
access_token = ".............................."
access_token_secret = ".............................."

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

csvFile = open('mycsv.csv', 'a')

csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#AirIndia",count=100,
                           lang="en",since="2020-06-13").items():
    print (tweet.id_str,tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.id_str,tweet.created_at, tweet.text.encode('utf-8')])

csvFile.close()