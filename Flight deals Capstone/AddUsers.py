import os
from dotenv import load_dotenv

load_dotenv("./Python Env/env/.env")

SHEETYCUSTOMERAPI=os.getenv("SHEETYCUSTOMERAPI")

import requests

print("Welcome to the Flight Club\nHere we find the you the cheapest flights")
firstName=input("What is your First Name?\n")
lastName=input("What is your Last Name?\n")
email=input("What is your email?\n")
verify=input("Please re-type your email.\n")

if email==verify:
  print("Welcome to the flight club")
  data={
    "user":{
      "firstName":firstName,
      "lastName":lastName,
      "email":verify
    }
  }
  response=requests.post(url=SHEETYCUSTOMERAPI,json=data)
else:
  while verify!=email:
    verify=input("Please re-type your email.\n")

