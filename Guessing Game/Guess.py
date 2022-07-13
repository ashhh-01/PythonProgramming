def game():

    # import random
    # Numbers=[*range(1,101,1)]
    # answer=random.choice(Numbers)

    from random import randint
    answer=randint(1,100)

    # print(answer)

    # gameOver=False

    EASYLEVEL=10
    HARDLEVEL=5

    # def check(guess,answer,life):
    #     if guess>answer:
    #         print("Too high")
    #         print(f"Number of life's remaining : {life}")

    #     elif guess<answer:
    #         print("Too low")
    #         print(f"Number of life's remaining : {life}")

    #     else:
    #         print("congragulation!You guessed it Right!")

    def check(guess,answer,life):
        if guess<answer:
            print("Too low")
            return life-1
        elif guess>answer:
            print("Too high")
            return life-1
        else:
            print("congratulations!!You guessed it right")

    def difficulty():
        set=input("choose difficulty!Type 'easy' or 'hard': ")
        if set=="easy":
            return EASYLEVEL
        else:
            return HARDLEVEL


    print("Welcome to the Number Guessing Game!\n I am thinking of a number between 1 and 100")
    life=difficulty()   

    # while not gameOver:
    #     guess=int(input("Guess the number:"))
    #     life-=1
    #     check(guess,answer,life)
    #     if guess==answer or life==0 :
    #         gameOver=True
    
    guess=0
    while guess!=answer:
        guess=int(input("Guess the number: "))
        print(f"You got {life} life remaining")        
        life=check(guess,answer,life)
        if life==0:
            print("You have 0 life's!You lose:( ")
            return 

game()


