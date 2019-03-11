from sense_hat import SenseHat
import requests
from random import randint
from time import sleep
import json

sense = SenseHat()
response = requests.get("https://randomuser.me/api/")
sense.clear()

# data = json.loads(response)
# namen = data['first']



def like():
	sense.set_pixel(0,0, [0,255,0])
def dislike():
	sense.set_pixel(0,0, [255,0,0])
def show_name():
    sense.show_message('test')

while True:
    try:
        sense.stick.direction_right = like
        sense.stick.direction_left = dislike
        sense.stick.direction_up = show_name
        
    except KeyboardInterrupt:
        sense.clear()
        quit()


