import tweepy as tp
import time
import os
from hidden-api-key import API_KEYS

# credentials to login to twitter api
consumer_key = API_KEYS["consumer_key"]
consumer_secret = API_KEYS["consumer_secret"]
access_token = API_KEYS["access_token"]
access_secret = API_KEYS["access_secret"]

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('models')

# iterates over pictures in models folder
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(3)
