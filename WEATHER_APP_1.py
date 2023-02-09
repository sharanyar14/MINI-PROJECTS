# WEATHER APP

#1 MILESTONE - To print the temperature of the city on particular date, 
# Using OIKOLAB website and generate API key to get data.



import json
import pandas as pd
import requests

city = input("Enter the city: ")
date = input("Enter the date: ")
URL = 'https://api.oikolab.com/weather'
OIKO_KEY = '841bfd264e5344cc95629e796840075b'

resp = requests.get(URL,
                 params={'param': ['temperature'],
                         'start': date,
                         'end': date,
                         'location': city,
                         'api-key': OIKO_KEY,
                         'freq': 'D'
                 }
                    )

#convert to json format as it represent in string format
info = resp.json()
weather_data = info['data']

#convert json to dictonary format
weather_data = json.loads(weather_data)

# df is mentioned in OIKO format for dataframe
df = pd.DataFrame(index=pd.to_datetime(weather_data['index'],unit='s'),
                  data=weather_data['data'],
                  columns=weather_data['columns'])

#iloc stands for locate the index in dataframe
# 0,4 stands for 0 row and 4th columns that represent temperature
temp = int(df.iloc[0,4])

print(f"Temperature for {city} on {date} = {temp}C")