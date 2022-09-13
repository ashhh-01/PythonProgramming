import requests
from flight_data import FlightData
from dotenv import load_dotenv
import os

load_dotenv(".\Python Env\env\.env")

KIWIAPI="https://tequila-api.kiwi.com"
KIWIKEY=os.getenv("KIWIKEY")

class FlightSearch:

    def getdata(self,cityname):
        kiwiParameters={
            "term":cityname,
            "location_types":"city" 
        }
        headers={
            "apikey":KIWIKEY
        }
        response=requests.get(url=f"{KIWIAPI}/locations/query",params=kiwiParameters,headers=headers)
        response.raise_for_status()
        result=response.json()["locations"]
        code=result[0]["code"]
        return code
    
    def searchflight(self,origin_city_code,destination_code,from_time,to_time):
        headers={
            "apikey":KIWIKEY
        }
        params={
            "fly_from":origin_city_code,
            "fly_to":destination_code,
            "date_from":from_time.strftime("%d/%m/%Y"),
            "date_to":to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from":7,
            "nights_in_dst_to":28,
            "flight_type":"round",
            "one_for_city":1,
            "max_stopovers": 0,
            "Curr":"GBP"
        }
        response=requests.get(url=f"{KIWIAPI}/v2/search",headers=headers,params=params)
        # print(f"{response.text}")
        try:
            data=response.json()["data"][0]
        except IndexError:
            params["max_stopovers"]=1
            response=requests.get(f"{KIWIAPI}/v2/search",headers=headers,params=params)
            data=response.json()["data"]
            flightdata=FlightData(
                price=data[1]["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_airport=data["route"][1]["flyTo"],
                destination_city=data["route"][1]["cityTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flightdata
        else:
            flightdata=FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flightdata
        
