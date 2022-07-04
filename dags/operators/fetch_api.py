import pandas as pd
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

account_headers = {
    "Accept": "application/json", 
    "X-MAL-Client-ID": "6114d00ca681b7701d1e15fe11a4987e", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Content-Length": "112", 
    "client_id": "6114d00ca681b7701d1e15fe11a4987e",
    "grant_type": "password",
    "password": f"{os.getenv('MAL_PASSWORD')}",
    "username": f"{os.getenv('MAL_USERNAME')}", 
}

response = requests.get("https://api.myanimelist.net/v2/auth/token", headers = account_headers)

print(response.text)