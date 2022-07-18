from mimetypes import guess_all_extensions
from gameData import data
from art import logo,vs
import random,os
# from random import randint



def formatData(account):
    accountName=account["name"]
    accountDesc=account["description"]
    accountCountry=account["country"]
    return f"{accountName},{accountDesc} from {accountCountry}"

def check(guess,follower1,follower2):
    """ compares and returns either True or False"""
    if follower1>follower2:
        return guess=="a"
    else:
        return guess=="b"


score=0
gameContinue=True
account2=random.choice(data)


print(logo)

while gameContinue:

    # rand1=randint(0,len(data)-1)
    # rand2=randint(0,len(data)-1)
    # account1=data[rand1]
    # account2=data[rand2]


    account1=account2
    account2=random.choice(data)
    while account1==account2:
        account2=random.choice(data)

    print(f"Compare A: {formatData(account1)}")
    print(vs)
    print(f"Compare B: {formatData(account2)}")

    guess=input("Which is higher!A or B?").lower()

    follower1=account1["follower_count"]
    follower2=account2["follower_count"]
    
    os.system("cls")
    print(logo)
    iscorrect=check(guess,follower1,follower2)
    if iscorrect:
        score+=1
        print(f"You're right!,current score {score}")
        
    else:
            print(f"Sorry!You're wrong!,Final score {score}")
            gameContinue=False