import tweepy
import csv
  
consumer_key = ".............................."
consumer_secret = ".............................."
access_key = ".............................."
access_secret = ".............................."
  
def get_tweets(username,n):
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    alltweets = []  
    
    new_tweets = api.user_timeline(screen_name = username,count=200)
    
    alltweets.extend(new_tweets)
    
    oldest = alltweets[-1].id - 1
    
    i=0
    
    while i < n-1:
        print(f"getting tweets before {oldest}")
        i+=1
        new_tweets = api.user_timeline(screen_name = username,count=200,max_id=oldest)
        
        alltweets.extend(new_tweets)
        
        oldest = alltweets[-1].id - 1
        
        print(f"...{len(alltweets)} tweets downloaded so far")
    
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]
    
    with open(f'new_{username}_tweets.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)
    
    pass

      
if __name__ == '__main__': 
    
    n = 3
    get_tweets("@AmitShah",n)  