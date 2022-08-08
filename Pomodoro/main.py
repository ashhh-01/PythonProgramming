from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
mytimer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
     window.after_cancel(mytimer)
     canvas.itemconfig(timerText,text="00:00")
     timer.config(text="Timer")
     tick.config(text="")
     global reps
     reps=0
     startButton["state"]="active"
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    reps+=1
    worksec=WORK_MIN*60
    longBreak=LONG_BREAK_MIN*60
    shortBreak=SHORT_BREAK_MIN*60
    if reps%8==0:
        countDown(longBreak)
        timer.config(text="Break",fg=RED)
        startButton["state"]="disabled"

    elif reps%2==0:
        countDown(shortBreak)
        timer.config(text="Break",fg=PINK)
        startButton["state"]="disabled"

    else:
        countDown(worksec)
        timer.config(text="Work",fg=GREEN)
        startButton["state"]="disabled"

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math
def countDown(count):
    countmin=math.floor(count/60)
    countsec=count%60
    if countsec<10:
        countsec=f"0{countsec}"
    canvas.itemconfig(timerText,text=f"{countmin}:{countsec}")
    if count>0:
        global mytimer
        mytimer=window.after(1000,countDown,count-1)
    else:
        startTimer()
        mark=""
        worksession=math.floor(reps/2)
        for _ in range(worksession):
            mark+="✔"
        tick.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomatoimage=PhotoImage(file="./pomodoro-start/tomato.png")
canvas.create_image(100,112,image=tomatoimage)
timerText=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

timer=Label(font=(FONT_NAME,34,"bold"),fg=GREEN)
timer.config(text="Timer",background=YELLOW)
timer.grid(column=1,row=0)

startButton=Button(text="Start",highlightthickness=0,command=startTimer)
startButton.grid(column=0,row=2)
resetButton=Button(text="Reset",highlightthickness=0,command=resetTimer)
resetButton.grid(column=2,row=2)

tick=Label(fg=GREEN,bg=YELLOW)
tick.grid(column=1,row=3)

window.mainloop()