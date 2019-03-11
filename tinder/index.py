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
    data = json.load(json_data)
    return data

def save(name, choice, dataset):
  data = dataset
  if(choice == 'like'):
    data['liked'].append('x')
  else:
    data['disliked'].append('y')
  with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

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
        data = load_data
        get_user()
        events = sense.stick.get_events()

        sense.show_message(name)

        if(len(events) != 0):
            current_event = events[0]
        else:
            current_event = sense.stick.wait_for_event()
        
        if(current_event.direction == 'right'):
            choice = 'like'
        else:
            choice = 'dislike'

        save(name, choice, data)

    except KeyboardInterrupt:
        sense.clear()
        sys.exit(0)

