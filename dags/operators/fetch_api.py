import pandas as pd
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()


response = requests.get(f'''
                        POST /v2/auth/token HTTP/1.1
                        Host: api.myanimelist.net
                        Accept: application/json
                        User-Agent: NineAnimator/2 CFNetwork/976 Darwin/18.2.0
                        X-MAL-Client-ID: 6114d00ca681b7701d1e15fe11a4987e
                        Content-Type: application/x-www-form-urlencoded
                        Content-Length: 112

                        client_id=6114d00ca681b7701d1e15fe11a4987e&grant_type=password&password={os.getenv('MAL_PASSWORD')}&username={os.getenv('MAL_USERNAME')}
                        ''')