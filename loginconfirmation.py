#Albego: A Table Reservation System
#Login confirmation
#This file was edited and organized by Vishnu Siddharth V R
#this file was modified by Vishal Prakash


from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets3")


def relative_to_assets3(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#creating the window
window = Tk()

#writing the method that takes us to the next page
def go():
    window.destroy()
    import trackingpage

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")
window.title("AlbeGo")
logo=PhotoImage(file=relative_to_assets3("logo.png"))
window.iconphoto(False,logo)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
#albego logo
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets3("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    133.0,
    image=image_image_1
)
#login successful text
image_image_2 = PhotoImage(
    file=relative_to_assets3("image_2.png"))
image_2 = canvas.create_image(
    650.0,
    255.0,
    image=image_image_2
)
#burger photo
image_image_3 = PhotoImage(
    file=relative_to_assets3("image_3.png"))
image_3 = canvas.create_image(
    656.0,
    407.0,
    image=image_image_3
)
#shapes in the background
image_image_4 = PhotoImage(
    file=relative_to_assets3("image_4.png"))
image_4 = canvas.create_image(
    725,
    390,
    image=image_image_4
)
with open("restaurantname","r") as file:
    name=file.read()
canvas.create_text(
    532.0,
    373.0,
    anchor="nw",
    text=name,
    fill="#FFFFFF",
    font=("Nunito Bold", 32 * -1)
)
#go button
button_image_1 = PhotoImage(
    file=relative_to_assets3("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: go(),
    relief="flat"
)
button_1.place(
    x=600.0,
    y=525.0,
    width=114.0,
    height=41.0
)
window.bind("<Return>",lambda event:go())
window.resizable(False, False)
window.mainloop()
