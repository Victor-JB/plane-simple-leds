
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
import traceback
import json

load_dotenv()

PLANE_API_KEY = os.getenv('PLANE_API_KEY')

# consts
format_string = '%Y-%m-%dT%H:%M:%S'
iata_code = "SJC"

# all flights arriving a SJC API endpoint
all_flights_url = f"https://aviation-edge.com/v2/public/timetable?key={PLANE_API_KEY}&iataCode={iata_code}&type=arrival&status=active"

# specific flight info API endpoint; for tracking specific flight as it's on approach
sing_flight_url = f"https://aviation-edge.com/v2/public/flights?key={PLANE_API_KEY}&flightIata="

# ---------------------------------------------------------------------------- #
""" Gets all active flights arriving to SJC on IFR plan; i.e, jets """
def return_flights_queue():
    # A GET request to the API
    arr_dict_list = requests.get(all_flights_url).json()
    print(json.dumps(arr_dict_list, indent=4))

    arrival_queue = []
    for arrival in arr_dict_list:
        print(json.dumps(arrival, indent=4))
        arr_time = arrival['arrival']['estimatedTime'].split(".")[0] # raw string arrival time
        arr_datetime = datetime.strptime(arr_time, format_string) # formatting str into datetime obj

        if datetime.now() < arr_datetime and arrival['flight']['iataNumber']:
            arrival_queue.append({"est_time": arr_datetime, "flight": arrival['flight']})

    arrival_queue.sort(key = lambda x:x['est_time'])

    return arrival_queue

# ---------------------------------------------------------------------------- #
""" Gets specific flight info for a specific flight we want to monitor """
def get_plane_info(iata_number):
    # A GET request to the API
    # print(sing_flight_url + iata_number)
    flight_info = requests.get(sing_flight_url + iata_number)
    try:
        flight_info = flight_info.json()
        return flight_info
    except Exception:
        print(traceback.format_exc())
        return None

# ---------------------------------------------------------------------------- #
flight_queue = return_flights_queue()

print(flight_queue, "\n")

print()

single_flight = get_plane_info(flight_queue[0]['flight']['iataNumber'])
while !single_flight:
    single_flight = get_plane_info(flight_queue[0]['flight']['iataNumber'])
