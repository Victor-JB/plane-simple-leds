
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

import time
from rpi_ws281x import *




