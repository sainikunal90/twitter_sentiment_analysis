import tweepy
from textblob import TextBlob
import csv 
import unicodedata

# Step 1 - Authenticate
consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
num_of_tweets = 100
api = tweepy.API(auth)


# Open/create a file to append data to
csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

api = tweepy.API(auth)
results = api.search(q='uber', lang='en', count=num_of_tweets, tweet_mode='extended')
for tweet in results:
    print(tweet.created_at, tweet.full_text)
    analysis = TextBlob(tweet.full_text)
    score = analysis.sentiment
    csvWriter.writerow([tweet.created_at, score, tweet.full_text.encode('utf-8')])
    print(tweet.created_at, score, tweet.full_text)
csvFile.close()

