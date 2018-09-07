# model scraping for themodelbot

import requests
import os
import urllib, json

# website with model images
# url = 'https://dog.ceo/api/breeds/image/random/5', old dog API
url = "https://api.thedogapi.co.uk/v2/dog.php?limit=5"

# download page for parsing
page = requests.get(url)
json_temp = json.loads(page.text)
list_of_objects = json_temp.get("data")
list_photos_urls = []

for item in list_of_objects:
    list_photos_urls.append(item.get("url"))

print list_photos_urls

# create directory for model images
if not os.path.exists('dogs'):
    os.makedirs('dogs')

# move to new directory
os.chdir('dogs')

# image file name variable
x = 0

# writing images
for img_url in list_photos_urls:
    try:
        urllib.urlretrieve(img_url, "dog-"+str(x)+".jpg")

        # response = requests.get(url)
        # if response.status_code == 200: #if there is a response from that url
        #     with open('dog-' + str(x) + '.jpg', 'wb') as f:
        #         f.write(requests.get(url).content)
        #         f.close()
        #         x += 1
    except:
        pass
    x+=1
