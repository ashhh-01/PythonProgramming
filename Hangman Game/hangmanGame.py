import random
from hangmanArt import stages, logo
from hangmanWords import wordList

print(logo)
chosenWord=random.choice(wordList)
display=[]
userList=[]
gameOver=False
lives=6
for x in range(len(chosenWord)):
    display+="_"
print(display)
while not gameOver:
  userInput=input("Guess a Letter:\n").lower()
  if userInput!="":  #Doesnt allow empty Entry
    guess=userInput[0] #Takes Only first the character if multiple characters have been entered
    if guess.isalpha(): #Checks if its actually a letter
      if guess not in userList:
        if guess in display:
          userList.append(guess)
          print("You have already enter this letter")
        for position in range(len(chosenWord)):
          if guess==chosenWord[position]:
            userList.append(guess)
            display[position]=guess
        print(display)
        if guess not in chosenWord:
          userList.append(guess)
          lives-=1
          print(f"The letter {guess} doesn't exist in the word.You lose a Life!")
          print(stages[lives])
        if lives==0:
          gameOver=True
          print(f"Game Over!You lose.\nThe word was {chosenWord}")
        if "_" not in display:
          gameOver=True 
          print("Congratulations!You win!")
      else:
        print(f"You have already used this Letter!\n{userList}\n^These are the Letters which have already been used.")
    else:
      print("Invalid!Please Enter a letter!")
  else:
    print("You haven't Entered anything!Please Enter a letter!")