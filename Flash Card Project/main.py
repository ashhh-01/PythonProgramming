import random,pandas

currentcard={}
tolearn={}

try:
    data=pandas.read_csv("./Flash Card Project/data/wordstolearn.csv")
except FileNotFoundError:
    originaldata=pandas.read_csv("./Flash Card Project/data/french_words.csv")
    tolearn=originaldata.to_dict(orient="records")
else:
    tolearn=data.to_dict(orient="records")
# newdata={row.French:row.English for (index,row) in data.iterrows()}


def generator():
    global currentcard,fliptimer
    window.after_cancel(fliptimer)
    currentcard=random.choice(tolearn)
    canvas.itemconfig(cardTitle,text="French",fill="black")
    canvas.itemconfig(cardWord,text=currentcard["French"],fill="black")
    canvas.itemconfig(cardbackground,image=cardfrontimage)
    fliptimer=window.after(3000,func=flipcard)



def flipcard():
    canvas.itemconfig(cardTitle,text="English",fill="White")
    canvas.itemconfig(cardWord,text=currentcard["English"],fill="White")
    canvas.itemconfig(cardbackground,image=cardbackimage)

def is_known():
    tolearn.remove(currentcard)
    data=pandas.DataFrame(tolearn)
    data.to_csv("./Flash Card Project/data/wordstolearn.csv",index=False)    
    generator()
 

#-----------------------------------------------------------------------------------------
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window=Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)
fliptimer=window.after(3000,func=flipcard)


canvas=Canvas(width=800,height=526,highlightthickness=0,background=BACKGROUND_COLOR)
cardbackimage=PhotoImage(file="./Flash Card Project/images/card_back.png")
cardfrontimage=PhotoImage(file="./Flash Card Project/images/card_front.png")
cardbackground=canvas.create_image(400,263,image=cardfrontimage)
cardTitle=canvas.create_text(400,125,text="Title",font=("Ariel",40,"italic"))
cardWord=canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))

canvas.grid(column=0,row=0,columnspan=2)

redImage=PhotoImage(file="./Flash Card Project/images/wrong.png")
redbutton=Button(image=redImage,highlightthickness=0,borderwidth=0,command=generator)
redbutton.grid(column=0,row=1)

greenImage=PhotoImage(file="./Flash Card Project/images/right.png")
greenbutton=Button(image=greenImage,highlightthickness=0,borderwidth=0,command=is_known)
greenbutton.grid(column=1,row=1)

generator()
window.mainloop()

