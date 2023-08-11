#version 2.0
#Edited by : Vishnu Siddharth V R
#Edited by : Vishal Prakash

# from os import uname
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def signup():
    import login #module to create an account
    email= entry_4.get()
    usname= entry_5.get()
    pwd=entry_1.get()
    cnfrmpwd=entry_2.get()
    hotel=entry_3.get()
    error=''
    '''if email and usname and pwd and cnfrmpwd and hotel:
        conf=login.fsignup(email,usname,pwd,cnfrmpwd,hotel)
    else:
        conf=False
        canvas.create_text(860.0,650.0,anchor="nw",text="Please enter all the details",fill="#C70000",font=("Arial", 12 * -1))'''
    
    if email and usname and pwd and cnfrmpwd and hotel:
    

        conf=login.fsignup(email,usname,pwd,cnfrmpwd,hotel)
        if conf:
            window.destroy()
            file=open('restaurant.txt','w')
            file.write(hotel)
            import loginconfirmation
        else:
            canvas.create_text(860.0,650.0,anchor="nw",text=error,fill="#C70000",font=("Arial", 12 * -1))

    else:
        error='Please enter all the details'
        canvas.create_text(860.0,650.0,anchor="nw",text=error,fill="#C70000",font=("Arial", 12 * -1))
        
        






OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets2")


def relative_to_assets2(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("AlbeGo")
logo=PhotoImage(file=relative_to_assets2("logo.png"))
window.iconphoto(False,logo)
window.geometry("1280x720")
window.configure(bg = "#FFFFFF") #Background white


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
) 
#Canvas is created

canvas.place(x = 0, y = 0)
#Canvas is placed

image_image_1 = PhotoImage(
    file=relative_to_assets2("image_1.png"))
image_1 = canvas.create_image(
    322.0,
    360.0,
    image=image_image_1
)



image_image_2 = PhotoImage(
    file=relative_to_assets2("image_2.png"))
image_2 = canvas.create_image(
    930.0,
    310.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets2("entry_1.png"))
entry_bg_1 = canvas.create_image(
    939.0,
    419.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    show='•'
)
entry_1.place(
    x=772.0,
    y=398.0,
    width=334.0,
    height=42.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets2("entry_2.png"))
entry_bg_2 = canvas.create_image(
    939.0,
    489.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    show='•'
)
entry_2.place(
    x=772.0,
    y=468.0,
    width=334.0,
    height=42.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets2("entry_3.png"))
entry_bg_3 = canvas.create_image(
    939.0,
    559.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_3.place(
    x=772.0,
    y=538.0,
    width=334.0,
    height=42.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets2("entry_4.png"))
entry_bg_4 = canvas.create_image(
    939.0,
    279.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_4.place(
    x=772.0,
    y=258.0,
    width=334.0,
    height=42.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets2("entry_5.png"))
entry_bg_5 = canvas.create_image(
    939.0,
    349.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_5.place(
    x=772.0,
    y=328.0,
    width=334.0,
    height=42.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets2("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:signup(),
    relief="flat"
)

button_1.place(
    x=886.0,
    y=605.0,
    width=114.0,
    height=41.0
)

window.bind('<Return>', lambda event:signup())  #pressing enter key will trigger 
window.resizable(False, False)
window.mainloop()
