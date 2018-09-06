import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = '5DsRRz0Z0bQAmVU8YvM7yibMm'
consumer_secret = 'JDky8oUEu8BJNh9pekEzf8JUI8FQXA05sjh59e5eDCKvTGMTj0'
access_token = '1014279877-EecPLuxeJohvAJy2hENT3ecl1KMs42RYwut2XxT'
access_secret = 'EaRzXaSc2coNMJsgI7rEv6dPw6mJ8xgY75dp2pbzpbfnx'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('models')

# iterates over pictures in models folder
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(3)
