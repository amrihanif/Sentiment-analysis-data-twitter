# coding=utf-8
import tweepy
# from textblob import textblob

consumer_key = '######'
consumer_secret = '####'

access_token = '#####'
access_token_secret = '#####'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.search('Topik')

for tweet in tweets:
    print(tweet.text)