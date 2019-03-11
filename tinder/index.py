from sense_hat import SenseHat
import requests
from random import randint
from time import sleep
import json

sense = SenseHat()
response = requests.get("https://randomuser.me/api/")
sense.clear()

jsonn = response.json()
dictt = json.loads(jsonn)[0]

# title = json[0][1][0]
# first_name = json[0][1][1]
# last_name = json[0][1][2]

# namen = data['first']
title = dictt['results']['name']['title']
first_name = dictt['results']['name']['first']
last_name = dictt['results']['name']['last']



def like():
	sense.set_pixel(0,0, [0,255,0])
def dislike():
	sense.set_pixel(0,0, [255,0,0])
def show_name():
    sense.show_message('test')

while True:
    try:
        # sense.stick.direction_right = like
        # sense.stick.direction_left = dislike
        sense.show_message('${title} ${first_name} ${last_name}')
        
    except KeyboardInterrupt:
        sense.clear()
        quit()


