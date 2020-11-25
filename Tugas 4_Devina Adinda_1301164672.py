# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 23:19:45 2020

@author: Devina Adinda
"""

import tweepy
#variables that contains the credentials to access TWitter API
ACCESS_TOKEN = '1068590870-4nv1EcA30dRbUILW6As5PZ8sKgcSjVSNyCyndNN'
ACCESS_SECRET = 'mXVcAPNlNaqCpWovhQGvteQFnvXFADku33Mu0omCbPZAs'
CONSUMER_KEY = 'kNEzMee6eNIETdBVocz8oqHDO'
CONSUMER_SECRET = 'gXewmHLdRyTgy4uY7WRyXA3fLF8C1er0Mw8RbZUiWzqj1lfpRC'

#setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

#create API object
api = connect_to_twitter_OAuth()

#tweets from my stream
def tweetStream():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

#status dari twitter sendiri
def myStatus():
    for status in tweepy.Cursor(api.home_timeline).items(10):
        print(status.text)

#daftar pertemanan
def myFriends():
    for friend in tweepy.Cursor(api.friends).items(10):
        print(friend.name)

#tweet dari aku twitter sendiri
def myTweets():
    for tweet in tweepy.Cursor(api.user_timeline).items(10):
        print(tweet.text)

#tweet dari akun twitter lain
def someoneTweets():
    tweets= api.user_timeline('dinidecil')
    for tweet in tweets:
        print(tweet.text)
        
import json
def statusUseJson():
    for status in tweepy.Cursor(api.home_timeline).items(10):
        print(json.dumps(status._json))
        
def process_or_store(tweet):
    print(json.dumps(tweet))
    for status in tweepy.Cursor(api.home_timeline).items(10):
        process_or_store(status._json)
    
#tweetStream()
#myStatus()
#myFriends()
#myTweets()
#someoneTweets()        
statusUseJson()
#process_or_store()