import turtle,pandas

screen=turtle.Screen()
screen.title("U.S States Game")

image="./us-states-game-start/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("./us-states-game-start/50_states.csv")
allstate=data.state.to_list()
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

guessedState=[]
while len(guessedState)<50:
    useranswer=screen.textinput(title=f"{len(guessedState)}/50 Guess the State",prompt="Whats the name of the state?").title()
    if useranswer in allstate:
        guessedState.append(useranswer)
        tom=turtle.Turtle()
        tom.hideturtle() 
        tom.pu()
        stateData=data[data.state==useranswer]
        tom.goto(int(stateData.x),int(stateData.y))
        tom.write(stateData.state.item()) #or useranswer
        print()
    elif useranswer=="Exit":
        # missingStates=[]
        missingStates=[state for state in allstate if state not in guessedState]
        # for state in allstate:
        #     if state not in guessedState:
                # missingStates.append(state)
        newData=pandas.DataFrame(missingStates)
        newData.to_csv("./us-states-game-start/StatestoLearn.csv")
        break

screen.exitonclick()

