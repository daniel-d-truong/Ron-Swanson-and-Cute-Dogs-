import tweepy as tp
import time
import os
import requests
import urllib, json
import getDogPics
import shutil
import pause
import getRonQuotes
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

# iterates over lists and tweets quote and picture
while (True):
    for dog_image in os.listdir('.'):
        # api.update_status(str(ron_quotes_list[ron_index]))
        # upload = api.media_upload(filename=dog_image)
        string = getRonQuotes.ron_quotes_list[ron_index] + hashtag
        api.update_with_media(dog_image, status=(string))
        ron_index+=1
        print ("Script Success!")
        pause.hours(12)
    print ("Reached end of list")
    os.chdir("..")
    print ("Moved back to project directory")
    shutil.rmtree("./dogs")
    print ("Removed dogs folder")
    reload(getDogPics)
    print ("Reloaded on new dog pics")
    reload(getRonQuotes)
    print ("Reloaded getRonQuotes")
    print (getRonQuotes.ron_quotes_list)
    ron_index = 0
