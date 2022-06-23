from art import logo
import random
print(logo)
gameOver=False

def dealCards():
    """Returns a random card from the Deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10] #King,Queen,Jack all count as 10 and ace as 11 or 1
    card=random.choice(cards)
    return card

#Blackjack(0)-->11 + 10 [WIN]
def calculateScore(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(userScore,computerScore):
    if userScore>21 and computerScore>21:
        return "You went Over you lose ;("
    elif userScore<21 and computerScore>21:
        return "You Win :)"
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
userCard=[]
computerCard=[]

for _ in range(2):
    userCard.append(dealCards())
    computerCard.append(dealCards())

while not gameOver:
    userScore=calculateScore(userCard)
    computerScore=calculateScore(computerCard)
    print(f"Your Cards: {userCard} and Your Score: {userScore}")
    print(f"Opponent's first Card {computerCard[0]}")

    if userScore==0 or computerScore==0 or userScore>21:
        gameOver=True
    else:
        userDeal=input("Type 'y' to deal or 'n' to pass.")
        if userDeal=="y":
            userCard.append(dealCards())
        else:
            gameOver=True

while computerScore!=0 and computerScore<17:
    computerCard.append(dealCards())
    computerScore=calculateScore(computerCard)
print(f"Your final cards: {userCard} and Score: {userScore}")
print(f"Opponent's cards: {computerCard} and Opponent's Score: {computerScore}")
print(compare(userScore,computerScore))
