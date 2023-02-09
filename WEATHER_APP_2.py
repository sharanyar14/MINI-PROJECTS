# WEATHER APP

#2 MILESTONE - To compare 2 cities and 
# to print the name of the city whose temperature variance will be lesser in the upcoming week from the given date.


OIKO_KEY = '841bfd264e5344cc95629e796840075b'
URL = 'https://api.oikolab.com/weather'

import datetime
import json
import requests
import pandas as pd

city1 = "Delhi"
city2 = "Mumbai"

start_date = int(2019-9-1)
end_date = int(start_date+ 7)


resp1 = requests.get(URL,
        params = {
            'param': ['temperature'],
            'start': start_date,
            'location': city1,
            'end': end_date,
            'api-key': OIKO_KEY,
            'freq': 'D'
            }
    )
resp2 = requests.get(URL,
        params = {
            'param': ['temperature'],
            'start': start_date,
            'location': city2,
            'end': end_date,
            'api-key': OIKO_KEY,
            'freq': 'D'
            }
    )
weather_data1 = json.loads(resp1.json()['data'])
weather_data2 = json.loads(resp2.json()['data'])

df1 = pd.DataFrame(index=pd.to_datetime(weather_data1['index'],unit='s'),
                    data=weather_data1['data'],
                    columns=weather_data1['columns'])
df2 = pd.DataFrame(index=pd.to_datetime(weather_data2['index'],unit='s'),
                    data=weather_data2['data'],
                    columns=weather_data2['columns'])

temp1 = df1.iloc[:,4]
temp2 = df2.iloc[:,4]

city1_temp_variance = temp1.var()
city2_temp_variance = temp2.var()

if city1_temp_variance < city2_temp_variance:
        print(f'We choose {city1} because of less temperature variance')
else:
        print(f'We choose {city2} because of less temperature variance')