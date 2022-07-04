import os
import requests
import json
import pandas as pd

response = pd.read_csv("https://raw.githubusercontent.com/practical-jupyter/sample-data/master/anime/anime.csv")

if not os.path.exists("data"):
    os.makedirs("data")

response.to_csv("data/anime.csv", index=False)