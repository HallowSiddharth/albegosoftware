#Albego - Home/Login Page
#Version 1.0
#Build: July 2022
#This file was edited by Vishnu Siddharth
#This file was edited by Vishal Prakash

import login
from pathlib import Path
from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def authenticate():
    username= entry_1.get()
    password= entry_2.get()
    name= login.flogin(username,password)
    with open("restaurantname","w") as newfile:
        newfile.write(str(name))
    print(name)
    if name:
        window.destroy()
        import loginconfirmation
        
    else:   
        canvas.create_text(840.0,485.0,anchor="nw",text="Invalid Login Details! Please try again",fill="#C70000",font=("Arial", 12 * -1))
        
        
def signup():
    window.destroy()
    import signuppage

    


window = Tk()
window.title("AlbeGo")
logo=PhotoImage(file=relative_to_assets("logo.png"))
window.iconphoto(False,logo)
window.geometry("1280x720")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    300.0,
    360.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    924.0,
    382.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    937.0,
    283.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)

entry_1.place(
    x=770.0,
    y=262.0,
    width=334.0,
    height=42.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    937.0,
    379.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    show="•"
)
entry_2.place(
    x=770.0,
    y=358.0,
    width=334.0,
    height=42.0,
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= lambda:authenticate(),
    relief="flat"
)
button_1.place(
    x=880.0,
    y=435.0,
    width=114.0,
    height=41.0
)
'''
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: authenticate(),
    relief="flat"
)
button_2.place(
    x=991.0,
    y=409.0,
    width=124.0,
    height=14.0
)
'''
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: signup(),
    relief="flat"
)

button_3.place(
    x=983.0,
    y=665.0,
    width=55.0,
    height=17.0
)
window.bind('<Return>',lambda event:authenticate())
window.resizable(False, False)
window.mainloop()

