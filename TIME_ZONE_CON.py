
# TIME ZONE CONVERTER

import pytz, datetime

year = 2019
month = 3
day = 12
hour = 14
minute = 42

# converting above integer of datetime using datetime library
users_time = datetime.datetime(year,month,day,hour,minute)

# Timezones of different countries.
cairo_timezone = pytz.timezone("Africa/Cairo")
london_timezone = pytz.timezone("UTC")
new_delhi_timezone = pytz.timezone("Asia/Kolkata")
sydney_timezone = pytz.timezone("Australia/Sydney")
tokyo_timezone = pytz.timezone("Asia/Tokyo")
seoul_timezone = pytz.timezone("Asia/Seoul")

# convert user's time into UTC to above timezones
cairo_time = pytz.utc.localize(users_time).astimezone(cairo_timezone)
london_time = pytz.utc.localize(users_time).astimezone(london_timezone)
new_delhi_time = pytz.utc.localize(users_time).astimezone(new_delhi_timezone)
sydney_time = pytz.utc.localize(users_time).astimezone(sydney_timezone)
tokyo_time = pytz.utc.localize(users_time).astimezone(tokyo_timezone)
seoul_time = pytz.utc.localize(users_time).astimezone(seoul_timezone)

# print in ISO format
print("Cairo Time is", cairo_time.isoformat())
print("London Time is", london_time.isoformat())
print("New Delhi Time is", new_delhi_time.isoformat())
print("Sydney Time is", sydney_time.isoformat())
print("Tokyo Time is", tokyo_time.isoformat())
print("Seoul Time is", seoul_time.isoformat())
