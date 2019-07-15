import tweepy
from textblob import TextBlob
import csv 
import unicodedata

# Step 1 - Authenticate
consumer_key= 'a6OANIAaWDrYYnKSh8EhjKqKa'
consumer_secret= 'KrLHDb4vspTfavBBgBdtR9sVQu9UDUJcZccu9z0uWPxtxgBRKg'

access_token='1144280360290643968-x1e0Dogngl6jLsVnFeRrusG9pVCKy7'
access_token_secret='w4F24CJeJP3eAwOvmqXCY1xlFhEN8OvYy1m7OhuofgHZg'

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

