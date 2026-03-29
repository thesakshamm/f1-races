import requests
import json
import os
from whole_script import get_race_announcement
from dotenv import load_dotenv
load_dotenv()  # Add this before os.getenv() calls

api_key = os.getenv('VIBER_API_KEY')
user_id = os.getenv('VIBER_USER_ID')

url = 'https://chatapi.viber.com/pa/post'
message = get_race_announcement()

data = {
    "auth_token": api_key,
    "from": user_id,
    "type": "text",
    "text": message
}

r = requests.post(url=url, data=json.dumps(data))

if r.status_code == 200:
    print(f'Sent: {message}')
else:
    print(f'Error: {r.status_code} - {r.text}')