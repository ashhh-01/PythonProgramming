from datetime import datetime, timedelta
from email import message
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

notification=NotificationManager()
dataManager=DataManager()
sheet_data=dataManager.getData()
flightsearch=FlightSearch()
ORIGIN="LON"

if sheet_data[0]["iataCode"]=="":
    for row in sheet_data:
        row["iataCode"]=flightsearch.getdata(row["city"])
    dataManager.destination_data=sheet_data
    dataManager.updateDestinationCode()

for data in sheet_data:
    destinations={
        data["iataCode"]:{
            "id":data["id"],
            "city":data["city"],
            "price":data["lowestPrice"]
        }
    }

for data in sheet_data:
    destinations={
        data["iataCode"]:{
            "id":data["id"],
            "city":data["city"],
            "price":data["lowestPrice"]
        }
    }
tomorrow=datetime.now()+timedelta(days=1)
six_month_from_today=datetime.now()+timedelta(days=(6*30))

# for destination in sheet_data:
#     flight=flightsearch.searchflight(
#         ORIGIN,
#         destination_code=destination["iataCode"],
#         from_time=tomorrow,
#         to_time=six_month_from_today
#     )

for destinationCode in destinations:
    flight=flightsearch(
        ORIGIN,
        destinationCode,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    print(flight.price)
    if flight is None:
        continue
    if flight.price<destinations[destinationCode]["prices"]:
        users=dataManager.getemail()
        email=[row["email"] for row in users]
        name=[row["firstName"] for row in users]

        message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs>0:
            message+=f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

            notification.send_emails(email,message)