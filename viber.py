import requests
import json
from whole_script import get_race_announcement
from dotenv import load_dotenv
import os

load_dotenv()  
api_key = os.getenv('VIBER_API_KEY')
user_id = os.getenv('VIBER_USER_ID')
url = 'https://chatapi.viber.com/pa/post'

message = get_race_announcement()


data = {
    "auth_token":api_key, 
    "from": user_id, 
    "type":"text", 
    "text":message
}

r = requests.post(url=url, data=json.dumps(data))
if r.status_code == 200:
    print(f'Sent: {message}')
else:
    print(f'Error: {r.status_code} - {r.text}')







'''
# Configuration
api_key = '5616cd7c7272cb44-bbef03b9621f875b-40da9d396ef10303'
user_id = '/oUzQ4P9sUoNibNIWlGvnQ=='
url = 'https://chatapi.viber.com/pa/post'

# Get the data from your script
message_text = get_race_announcement()

if message_text:
    payload = {
        "auth_token": api_key,
        "receiver": user_id, # Viber usually uses 'receiver' for outgoing PA messages
        "type": "text",
        "text": message_text 
    }

    r = requests.post(url=url, data=json.dumps(payload))
    
    if r.status_code == 200:
        print(f'Sent: {message_text}')
    else:
        print(f'Error: {r.status_code} - {r.text}')
else:
    print("No race scheduled for tomorrow.")
    '''
