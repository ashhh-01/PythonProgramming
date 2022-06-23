import os
import random
from art import logo

def dealCards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10] #King,Queen,Jack are represented by 10 and Ace by 11
    card=random.choice(cards)
    return card

def scoreCalculation(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0  #Blackjack Ace(11)+10=21 [WIN]
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards) 

def compare(userScore,computerScore):
    """Function to compare User and Computer Scores"""
    if userScore>21 and computerScore>21:
        return "You went Over!You lose ;("
    elif userScore<21 and computerScore>21:
        return "You Win :)"
    elif userScore>21 and computerScore<21:
        return "You Went over!You Lose ;("
    elif userScore==computerScore:
        return "Draw -_-"
    elif userScore==0:
        return "You got Blackjack!You Win :)"
    elif computerScore==0:
        return "Opponent got Blackjack!You lose ;("
    elif userScore>computerScore:
        return "You Win :)"
    else:
        return "You Lose ;("

def playGame():
    print(logo)
    userCards=[]
    computerCards=[]

    for _ in range(2):
        userCards.append(dealCards())
        computerCards.append(dealCards())

    gameisOver=False
    while not gameisOver:   
        userScore=scoreCalculation(userCards)
        computerScore=scoreCalculation(computerCards)
        print(f"Your cards: {userCards} and Score: {userScore}")
        print(f"Oppenent's first card: {computerCards[0]}")
        if userScore==0 or computerScore==0 or userScore>21:
            gameisOver=True #WIN
        else:
            userDeal=input("Type 'y' to deal and 'n' to pass:\n")
            if userDeal=="y":
                userCards.append(dealCards())
            else:
                gameisOver=True
    while computerScore!= 0 and computerScore<17:
        computerCards.append(dealCards())
        computerScore=scoreCalculation(computerCards)
    print(f"Your final cards: {userCards} and Score: {userScore}")
    print(f"Opponents cards: {computerCards} and score: {computerScore}")
    print(compare(userScore,computerScore))

while input("Do you want to play Blackjack 'y' or 'n':\n")=="y":
    os.system("cls")
    playGame()


