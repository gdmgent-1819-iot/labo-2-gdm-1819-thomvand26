from sense_hat import SenseHat
import requests
from random import randint
from time import sleep
import json

sense = SenseHat()
response = requests.get("https://randomuser.me/api/")
sense.clear()

data = json.loads(response)
namen = data['first']
sense.show_message(namen)


def like ():
	sense.set_pixel(0,0, [0,255,0])
def dislike ():
	sense.set_pixel(0,0, [255,0,0])

while True:
    try:
        sense.stick.direction_right = like
        sense.stick.direction_left = dislike
        
    except KeyboardInterrupt:
        sense.clear()
        quit()


