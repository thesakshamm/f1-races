import pandas as pd
import requests
from datetime import timedelta

def get_race_announcement():
    url = 'https://api.openf1.org/v1/sessions?year=2026'
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data) #loading dataframe

    #conversion of date start to dtype:dataime
    df['date_start'] = pd.to_datetime(df['date_start'])
    df['date_only'] = df['date_start'].dt.date
    df['time_only'] = df['date_start'].dt.time

    # Filter for Races
    race_dates = df[df['session_name'] == 'Race'].copy()

    # Logic for "Tomorrow"
    today = pd.Timestamp.today() # Using your specific test date
    tmrw = today + timedelta(days=1)
    
    # Check if any race date matches tomorrow
    match = race_dates[race_dates['date_only'] == tmrw]

    if not match.empty:
        location = match['circuit_short_name'].iloc[0]
        time = match['time_only'].iloc[0]
        return f"🏎️ RACE DAY TOMORROW at {location} at {time}"
    
    return None # Return None if no race tomorrow
    

get_race_announcement()