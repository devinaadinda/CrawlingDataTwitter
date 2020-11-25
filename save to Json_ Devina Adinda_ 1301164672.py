# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 13:21:48 2020

@author: Devina Adinda
"""
import tweepy
import json

ACCESS_TOKEN = '1068590870-4nv1EcA30dRbUILW6As5PZ8sKgcSjVSNyCyndNN'
ACCESS_SECRET = 'mXVcAPNlNaqCpWovhQGvteQFnvXFADku33Mu0omCbPZAs'
CONSUMER_KEY = 'kNEzMee6eNIETdBVocz8oqHDO'
CONSUMER_SECRET = 'gXewmHLdRyTgy4uY7WRyXA3fLF8C1er0Mw8RbZUiWzqj1lfpRC'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

class MyListener(tweepy.StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    def on_error(self, status):
        print(status)
        return True

twitter_stream = tweepy.Stream(auth, MyListener())
twitter_stream.filter(track=['#CoronaVirusUpdates'])