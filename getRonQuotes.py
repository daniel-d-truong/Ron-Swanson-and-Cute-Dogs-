# getting ron quotes as json

import requests
import os
import urllib, json


ron_url = 'http://ron-swanson-quotes.herokuapp.com/v2/quotes/50' #gets 50 quotes
ron_quotes_list = []

page = requests.get(ron_url)
ron_quotes_temp = json.loads(page.text)
ron_quotes_list = ron_quotes_temp
    # print (page.json())
    # print (ron_quotes_list)
    # print (len(ron_quotes_list))
