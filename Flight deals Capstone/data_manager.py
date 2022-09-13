from urllib import response
import requests
from dotenv import load_dotenv
import os

load_dotenv(".\Python Env\env\.env")

SHEETYAPI=os.getenv("SHEETYAPI")
SHEETYCUSTOMERAPI=os.getenv("SHEETYCUSTOMERAPI")

class DataManager():
    def __init__(self):
        self.destinationData={}

    def getData(self):
        response=requests.get(url=SHEETYAPI)
        data=response.json()["prices"]
        self.destinationData=data
        return self.destinationData
    
    def updateDestinationCode(self):
        for city in self.destinationData:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response=requests.put(url=f"{SHEETYAPI}/{city['id']}",json=new_data)
            # print(response.text)
    def getemail(self):
        response=requests.get(url=SHEETYCUSTOMERAPI)
        data=response.json()
        self.customerdata=data["users"]
        return self.customerdata



