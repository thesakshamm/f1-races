import pandas as pd
import requests

url = 'https://api.openf1.org/v1/sessions?year=2026'
response = requests.get(url)
data = response.json()



