import tweepy
import csv
import sys
import json
from IPython.display import clear_output

consumer_key = ".................................................." 
consumer_secret = ".................................................."
access_token_key = .................................................."
access_token_secret = ".................................................."
  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)
    
def get_tweets(ch):
    
    username = input("Enter user-handle including @ : ")
    n = int(input("Enter number of tweets to be downloaded as a multiple of 100 : "))
    
    if ch == 2:
        x = input("Do you want to give any partticular name to your csv file (y/n) : ")
        if x.lower() == 'y':
            name = input("Enter the name for your csv file : ")
        else:
            name = username
    
    try:
        alltweets = []
        new_tweets = api.user_timeline(screen_name = username,count=100)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        
        for i in range(1,n):
            if ch==1:
                print(f"...getting tweets before {oldest}")
            
            new_tweets = api.user_timeline(screen_name = username,count=100,max_id=oldest)
            alltweets.extend(new_tweets)
            oldest = alltweets[-1].id - 1
    
            if ch==1:
                print(f"...{len(alltweets)} tweets downloaded so far")
        
        outtweets = [[tweet.id_str, tweet.created_at, tweet.source, tweet.text, 
                      tweet.place] for tweet in alltweets]
        
        if ch==1:
            print(*outtweets)    
        if ch==2:
            with open(f'{name}_tweets.csv', 'w', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id","created_at","source","text","place"])
                writer.writerows(outtweets)
    except:
        print("Connection Error")

def hashtags(ch):
    
    try:
        hashtag = input("Enter hashtag including # : ")
        date = input("Enter date after when you want to download the Tweets (yyyy-mm-dd): ")
        if ch==4:
            x = input("Do you want to give any partticular name to your csv file (y/n) : ")
            if x.lower() == 'y':
                name = input("Enter the name for your csv file : ")
            else:
                name = hashtag.strip("#") + ".csv"
                csvFile = open(name, 'a')
                csvWriter = csv.writer(csvFile)
    
        for tweet in tweepy.Cursor(api.search,q=hashtag,count=100,
                               lang="en",since=date).items():
            if ch==3:
                print(tweet.id_str,tweet.created_at, tweet.text)
            if ch==4:
                csvWriter.writerow([tweet.id_str,tweet.created_at, tweet.text.encode('utf-8')])
        if ch==4:
            print("Done")
            csvFile.close()
    except:
        print(".......................Connection Error...............")
        print("..........Plzz have a stable Internet Connection......")

def trends():
        
    # Where On Earth ID for India is 23424848.
    INDIA_WOE_ID = 23424848
    
    try:
        india_trends = api.trends_place(INDIA_WOE_ID)
        trends = json.loads(json.dumps(india_trends, indent=1))
        
        for trend in trends[0]["trends"]:
        	print((trend["name"]))
    except:
        print("Connection Error")
        
def switch():

    print("\nDo have a Stable Internet Connection for Execution")
    print("\n\t\tMenu\n")
    print("1. Print Tweets\n")
    print("2. Store Tweets in a csv file\n")
    print("3. Print Tweets for a given Hashtag\n")
    print("4. Store Tweets for a given Hashtag in a csv file\n")
    print("5. Print Trends of Twitter\n")
    print("6. Exit\n")
    try:
        ch = int(input("Enter Choice : "))
    except:
        print("Typing Error")
        return
    if ch==1:
        get_tweets(ch)
    
    elif ch==2:
        get_tweets(ch)        
    
    elif ch==3:
        hashtags(ch)
        
    elif ch==4:
        hashtags(ch)

    elif ch==5:
        trends()
        
    elif ch==6:
        pass
    else:
        print("\nInvalid Choice")

if __name__ == '__main__': 
    
    switch()
    clear_output()
    cond = True
    while cond:
        again = input("Do you want to execute again (y/n) : ")
        if again.lower() == 'y':
            switch()
            clear_output()
        elif again.lower() == 'n':
            cond = False
        else:
            print("\nInvalid Input")
            cond = False
    print("\nThank You")