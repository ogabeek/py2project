import os

import requests
from dotenv import load_dotenv

load_dotenv()



response = requests.get(
    "https://science.nasa.gov/wp-json/wp/v2/apod-basic",
    params={
        "api_key": os.getenv("my_NASA_API", "DEMO_KEY"),
        "feedtype": "json",
        "ver": "1.0",
    },
    timeout=15,
)
response.raise_for_status()
