from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip,json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generator():
    passwordentry.delete(0,END)
    number=["1","2","3","4","5","6","7","8","9","0"]
    letters=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    symbols=["?","!","@","#","$","%","&"]

    passwordletter=[choice(letters) for _ in range(randint(8,10))]
    passwordnumber=[choice(number) for _ in range(randint(2,4))]
    passwordsymbol=[choice(symbols) for _ in range(randint(2,4))]
    passwordlist=passwordletter+passwordnumber+passwordsymbol
    shuffle(passwordlist)
    password="".join(passwordlist)
    passwordentry.insert(0,string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    saveweb=webentry.get()
    saveuser=emailentry.get()
    savepassword=passwordentry.get()
    newData={
        saveweb:{
            "email":saveuser,
            "password":savepassword
        }
    }
    if saveweb=="" or len(saveuser)<=10 or savepassword=="":
        messagebox.showinfo(title="oopss",message="Please enter all the info!")
    else:     
        isOk=messagebox.askokcancel(title=website,message=f"These are the details that've been entered\nEmail: {saveuser}\nPassword: {savepassword}\nDo you want to save it?")
        if isOk:
            with open("./password-manager-start/data.json","w") as datafile:
                json.dump(newData,datafile,indent=4)
            try:
                with open("./password-manager-start/data.json",mode="r") as datafile:
                    data=json.load(datafile) #Reading Old Data
                    data.update(newData)
                
                with open("./password-manager-start/data.json","w") as datafile:
                    json.dump(data,datafile,indent=4)
            except:
                with open("./password-manager-start/data.json","w") as datafile:
                    json.dump(newData,datafile,indent=4)
                
            # with open("./password-manager-start/data.json","w") as datafile:
            #     json.dump(data,datafile,indent=4)
            finally:   
                webentry.delete(0,END)
                passwordentry.delete(0,END)
                emailentry.delete(0,len(saveuser)-10) # or END

#----------------------------Search function ------------------------------#

def search():
    web=webentry.get()
    try:
        with open("./password-manager-start/data.json") as datafile:
            data=json.load(datafile)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data File found")

    else:
        if web in data:
            email=data[web]["email"]
            password=data[web]["password"]
            messagebox.showinfo(title=web,message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error",message="No details found!")
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(width=240,height=240,padx=20,pady=20,background="#495C83")

photo=PhotoImage(file="./password-manager-start/logo.png")
canvas=Canvas(width=200,height=200,background="#495C83",highlightthickness=0)
canvas.create_image(100,100,image=photo)
canvas.grid(column=1,row=0)

website=Label(text="Website:",background="#495C83",fg="#C4DDFF",font= ('Helvetica 10 bold'))
website.grid(column=0,row=1)

email=Label(text="Email/Username:",background="#495C83",fg="#C4DDFF",font= ('Helvetica 10 bold'))
email.grid(column=0,row=2)

password=Label(text="Password:",background="#495C83",fg="#C4DDFF",font= ('Helvetica 10 bold'))
password.grid(column=0,row=3)


webentry=Entry(width=22,background="#C4DDFF")
webentry.focus()
webentry.grid(column=1,row=1)

emailentry=Entry(width=42,background="#C4DDFF")
emailentry.insert(0,string="@gmail.com")
emailentry.grid(column=1,row=2,columnspan=2)

passwordentry=Entry(width=22,background="#C4DDFF")
passwordentry.grid(column=1,row=3)

genpassword=Button(text="Generate Password",command=generator,background="#0AA1DD",fg="#C4DDFF",font= ('Helvetica 8 bold'))
genpassword.grid(column=2,row=3)

search=Button(text="Search",command=search,background="#0AA1DD",width=13,fg="#C4DDFF",font= ('Helvetica 8 bold'))
search.grid(column=2,row=1)
add=Button(text="Add",width=34,command=save,background="#36AE7C",fg="#C4DDFF",font= ('Helvetica 8 bold'))
add.grid(column=1,row=4,columnspan=2)
window.mainloop()
