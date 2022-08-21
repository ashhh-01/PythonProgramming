import os
from dotenv import load_dotenv

load_dotenv(".\Python Env\env\.env")
APIKEY=os.getenv("OPENWEATHERAPI")
APIENDPOINT="https://api.openweathermap.org/data/2.5/onecall"
debug = bool(os.getenv("DEBUG"))


from msilib.schema import Condition
import requests

parameters={
    "lat":13.360501,
    "lon":74.786369,
    "exclude":"current,minute,daily",
    "appid":APIKEY,
}


response=requests.get(APIENDPOINT,params=parameters)
response.raise_for_status()
hourdata_12=response.json()["hourly"][:12]

willrain=False

for data in hourdata_12:
    condition=data["weather"][0]["id"]
    if condition<800:
        willrain=True

if willrain:
    print("Get an Umbrella.")