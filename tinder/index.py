from sense_hat import SenseHat
import requests
from random import randint
from time import sleep
import json

sense = SenseHat()
sense.clear()
response = requests.get("https://randomuser.me/api/")

title = 't'
first_name = 'f'
last_name = 'l'

jsonn = response.json()

def like():
	sense.set_pixel(0,0, [0,255,0])
def dislike():
	sense.set_pixel(0,0, [255,0,0])
def show_name():
    sense.show_message('test')

def get_user():
    global response
    global title
    global first_name
    global last_name

    response = requests.get("https://randomuser.me/api/")

    title = jsonn['results'][0]['name']['title']
    first_name = jsonn['results'][0]['name']['first']
    last_name = jsonn['results'][0]['name']['last']


while True:
    try:
        sense.show_message('1')
        get_user()

        # sense.stick.direction_right = like
        # sense.stick.direction_left = dislike
        sense.show_message(title + ' ' + first_name + ' ' + last_name)
        sense.show_message('2')
        get_user()
        sense.show_message(title + ' ' + first_name + ' ' + last_name)

    except KeyboardInterrupt:
        sense.clear()
        quit()

