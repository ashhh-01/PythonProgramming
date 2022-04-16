import os
from art import logo
print(logo)

allBids={}
def biding(name,bid):
  allBids[name]=bid

def highestBider(allBids):
  highestBid=0
  for bids in allBids:
    biddingAmount=allBids[bids]
    if biddingAmount>highestBid:
      highestBid=biddingAmount
  print(f"The highest bider is {bids} with a bid of ${highestBid}")
    
nextbid=True

while nextbid:
  name=input("Enter Your name:\n")
  bid=int(input("Enter the biding amount:\n$"))
  biding(name,bid)
  user=input("Is there another bid?Type 'yes'or 'no.'\n")
  if user=="no":
    os.system("cls")
    nextbid=False
    highestBider(allBids)
  elif user=="yes":
    os.system("cls")    

