
"""
    Description: Query Aviation Edge API endpoint and return LED status for incoming
    plane
    Author: Victor Joulin-Batejat
    Date: Fall 2024
"""
import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta

load_dotenv()

PLANE_API_KEY = os.getenv('PLANE_API_KEY')

format_string = '%Y-%m-%dT%H:%M:%S'

# The API endpoint
url = f"https://aviation-edge.com/v2/public/timetable?key={PLANE_API_KEY}&iataCode=SJC&type=arrival&status=active"

# A GET request to the API
arr_dict_list = requests.get(url).json()

arriving_soon = []
for arrival in arr_dict_list:
    arr_time = arrival['arrival']['estimatedTime'].split(".")[0] # raw string arrival time
    print(arr_time)
    arr_datetime = datetime.strptime(arr_time, format_string)
    print(arr_datetime)

    if datetime.now() < arr_datetime:
        arriving_soon.append(arrival)

print(arriving_soon)
