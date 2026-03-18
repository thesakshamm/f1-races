import pandas as pd 
from datetime import date, timedelta
import requests

url = 'https://api.openf1.org/v1/sessions?year=2026'
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data) #loading dataframe

#conversion of date start to dtype:dataime
df['date_start'] = pd.to_datetime(df['date_start']) 

#making new column named 'date_only and converting it to datetime dtype
df['date_only'] = df['date_start'].dt.date
df['date_only'] = pd.to_datetime(df['date_only'])
df['time_only'] = df['date_start'].dt.time

#filterin out for race only excluding practise, session and everything
race_filter = (df['session_name'] == 'Race')
race_dates = df[race_filter]
today = pd.Timestamp('2026-07-04')#date.today()
tmrw = today + timedelta(1) 
race_is_tmrw = (tmrw == race_dates['date_only'])

#gets race details like date, time and cicuit name
race_details = race_dates[['date_only','time_only','circuit_short_name']]
race_location = (race_details.loc[race_is_tmrw,'circuit_short_name'].item())
race_time = (race_details.loc[race_is_tmrw,'time_only'].item())
print(f'RACE DAY TOMMORROW at {race_location} at {race_time}')








