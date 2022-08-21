import smtplib
import requests,time
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv(".\Python Env\env\.env")

MYLAT=os.getenv("LATITUDE")
MYLONG=os.getenv("LONGITUDE")
parameter={
    "lat":MYLAT,
    "long":MYLONG,
    "formatted":0
}
EMAIL=os.getenv("EMAIL1")
PASSWORD=os.getenv("PASSWORD")



#ISS
def isOverhead():
    response=requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    longitude=float(response.json()["iss_position"]["longitude"])
    latitude=float(response.json()["iss_position"]["latitude"])

    if float(MYLAT)-5 <=latitude <=float(MYLAT)+5 and float(MYLONG)-5<=longitude<=float(MYLONG)+5:
        return True


#Sunrise&Sunset
def isNight():
    response=requests.get("https://api.sunrise-sunset.org/json",params=parameter,verify=False)
    response.raise_for_status()
    data=response.json()
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
    hour=int(datetime.now().hour)
    if hour >=sunset or hour<=sunrise:
        return True
        

if isOverhead() and isNight():
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(EMAIL,PASSWORD)
    connection.sendmail(from_addr=EMAIL,
        to_addrs=os.getenv("EMAIL2"),
        msg="Subject:Time to look at the sky/nThe ISS is above Your head in the Sky"
    )