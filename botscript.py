import tweepy as tp
import time
import os
import requests
import urllib, json
import getDogPics
import shutil
from getRonQuotes import ron_quotes_list
from hiddenkey import API_KEYS

PATH = "/home/daniel/csProjects/twitBotRonDogs"
# credentials to login to twitter api
consumer_key = API_KEYS["consumer_key"]
consumer_secret = API_KEYS["consumer_secret"]
access_token = API_KEYS["access_token"]
access_secret = API_KEYS["access_secret"]

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

print (os.getcwd())
print (os.listdir('.'))

# iterates over pictures in models folder
ron_index = 0
hashtag = " #ronswansonquotes"
api.update_with_media("dog-0.jpg", status=ron_quotes_list[ron_index])

# iterates over lists and tweets quote and picture
for dog_image in os.listdir('.'):
    # api.update_status(str(ron_quotes_list[ron_index]))
    # upload = api.media_upload(filename=dog_image)
    string = ron_quotes_list[ron_index] + hashtag
    api.update_with_media(dog_image, status=(string))
    ron_index+=1
    time.sleep(30)

print ("Script Success!")

os.chdir("..")
print (os.listdir('.'))
shutil.rmtree("./dogs")
print (os.listdir('.'))
