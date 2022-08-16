from tkinter import *
import requests

def get_quote():
    response=requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/random/")
    response.raise_for_status()
    quote=response.json()["message"]
    canvas.itemconfig(quote_text,text=quote)



window = Tk()
window.title("Trump Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="./Quote GUI/Trump/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 18, "bold"), fill="white")
canvas.grid(row=0, column=0)

trumpImage = PhotoImage(file="./Quote GUI/Trump/Donald-Trump-PNG-Photos.png")
trumpImage=trumpImage.subsample(12)
trumpbutton = Button(image=trumpImage, highlightthickness=0, command=get_quote,border=0,width=150,height=150)
trumpbutton.grid(row=1, column=0)

get_quote()


window.mainloop()