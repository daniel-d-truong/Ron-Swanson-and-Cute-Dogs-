import tweepy as tp
import time
import os
import requests
import urllib, json
import getDogPics
from getRonQuotes import ron_quotes_list
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

os.chdir('dogs')

# iterates over pictures in models folder
ron_index = 0
for dog_image in os.listdir('.'):
    api.update_status(ron_quotes_list[ron_index])
    api.update_with_media(dog_image)
    ron_index+=1
    time.sleep(3)
