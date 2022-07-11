import os
import requests
import json
import pandas as pd

response = pd.read_csv("https://raw.githubusercontent.com/practical-jupyter/sample-data/master/anime/anime.csv")

if not os.path.exists("/home/nacnano/Documents/github/mal-data-warehouse/data"):
    os.makedirs("/home/nacnano/Documents/github/mal-data-warehouse/data")

response.to_csv("/home/nacnano/Documents/github/mal-data-warehouse/data/anime.csv", index=False)