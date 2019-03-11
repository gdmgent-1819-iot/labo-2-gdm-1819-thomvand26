from sense_hat import SenseHat
import requests
import json
from random import randint
from time import sleep
import json
import sys

sense = SenseHat()
sense.clear()

def load_data():
    with open('data.json') as json_data:
        global data_file
        data_file = json.load(json_data)

def save(name, choice):
    global data_file
    if(choice == 'like'):
        data_file['liked'].append(name)
    else:
        data_file['disliked'].append(name)
    with open('data.json', 'w') as outfile:
        json.dump(data_file, outfile)
    
def get_user():
    global name

    response = requests.get("https://randomuser.me/api/")
    jsonn = response.json()

    title = jsonn['results'][0]['name']['title']
    first_name = jsonn['results'][0]['name']['first']
    last_name = jsonn['results'][0]['name']['last']

    name = title + ' ' + first_name + ' ' + last_name



while True:
    try:
        load_data()
        get_user()
        events = sense.stick.get_events()

        sense.show_message(name)

        current_event = sense.stick.wait_for_event()
        
        if(current_event.direction == 'right'):
            choice = 'like'
            sense.clear(0, 255, 0)
        else:
            choice = 'dislike'
            sense.clear(255, 0, 0)

        sleep(1)

        save(name, choice)

    except KeyboardInterrupt:
        sense.clear()
        sys.exit(0)

