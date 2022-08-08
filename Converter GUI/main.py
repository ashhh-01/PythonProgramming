from tkinter import *

from matplotlib.pyplot import text

def converter():
    value1=float(input.get())
    value2=round(value1*1.609,2)
    label.config(text=f"{value2}")

window=Tk()
window.minsize(width=300,height=100)
window.title("Mile to Km converter")
window.config(padx=40,pady=20)

label1=Label(text="Miles")
label2=Label(text="Is equal to")
label3=Label(text="Km")

label1.grid(column=2,row=0)
label2.grid(column=0,row=1)
label3.grid(column=2,row=1)

input=Entry(width=10)
input.focus()
label=Label(width=10)

input.grid(column=1,row=0)
label.grid(column=1,row=1)


button=Button(text="Calculate",command=converter)
button.grid(column=1,row=2)

window.mainloop()