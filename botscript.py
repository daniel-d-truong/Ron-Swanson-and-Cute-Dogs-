import tweepy as tp
import time
import os
import requests
import urllib, json
from hiddenkey import API_KEYS

# credentials to login to twitter api
consumer_key = API_KEYS["consumer_key"]
consumer_secret = API_KEYS["consumer_secret"]
access_token = API_KEYS["access_token"]
access_secret = API_KEYS["access_secret"]

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# getting ron quotes as json
ron_url = 'http://ron-swanson-quotes.herokuapp.com/v2/quotes/50'
ron_quotes_list = []

def GetRonQuotes():
    page = requests.get(ron_url)
    ron_quotes_list = json.loads(page.text)
    # print (page.json())
    print ron_quotes_list

GetRonQuotes()
