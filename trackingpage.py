#Table Tracking Module
#v1.0 - date 08/08/2022 : edited by Vivekananth M , Viswavardini
#v1.1 - date 17/08/2022 : edited by Vivekananth M, Vinay Choudary
#v1.2 - date 18/08/2022 : edited by Vishnu Siddharth V R


import csv
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, Label


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")
window.title("AlbeGo")
logo=PhotoImage(file=relative_to_assets("logo.png"))
window.iconphoto(False,logo)

table_dict={2:[1,2,3,4,5,6,7],4:[8,9,10,11,12,13,14,15,16],6:[17,18],8:[19,20]}
table_list=[2,4,6,8]
#Main Canvas
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
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    154.0,
    370.0,
    image=image_image_1
)
#green tile group
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    434.0,
    333.0,
    image=image_image_2
)
#green tile sample
image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    100.0,
    118.0,
    image=image_image_3
)
#redtile that should be replaced
image_image_redtile = PhotoImage(
    file=relative_to_assets("redtile.png"))

image_image_2 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_2 = canvas.create_image(
    260.0,
    115.5,
    image=image_image_2
)
#green tile group
image_image_31 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_31 = canvas.create_image(
    430.0,
    115.5,
    image=image_image_31
)

image_image_41 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_41 = canvas.create_image(
    598.0,
    115.5,
    image=image_image_41
)

#greentile sample
image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    100.0,
    118.0,
    image=image_image_3
)


#greentile sample
image_image_7 = PhotoImage(
    file=relative_to_assets("image-7.png"))
image_7 = canvas.create_image(
    768.0,
    115.5,
    image=image_image_7
)
#greentile sample
image_image_8 = PhotoImage(
    file=relative_to_assets("image-8.png"))
image_8 = canvas.create_image(
    102.0,
    240.0,
    image=image_image_8
)
#greentile sample
image_image_9 = PhotoImage(
    file=relative_to_assets("image-9.png"))
image_9 = canvas.create_image(
    260.0,
    240.0,
    image=image_image_9
)
#greentile sample
image_image_10 = PhotoImage(
    file=relative_to_assets("image-10.png"))
image_10 = canvas.create_image(
    430.0,
    240.0,
    image=image_image_10
)
#greentile sample
image_image_11 = PhotoImage(
    file=relative_to_assets("image-11.png"))
image_11 = canvas.create_image(
    598.0,
    240.0,
    image=image_image_11
)
#greentile sample
image_image_12 = PhotoImage(
    file=relative_to_assets("image-12.png"))
image_12 = canvas.create_image(
    768.0,
    240.0,
    image=image_image_12
)
#greentile sample
image_image_13 = PhotoImage(
    file=relative_to_assets("image-13.png"))
image_13 = canvas.create_image(
    102.0,
    390.0,
    image=image_image_13
)
#greentile sample
image_image_14 = PhotoImage(
    file=relative_to_assets("image-14.png"))
image_14 = canvas.create_image(
    260.0,
    390.0,
    image=image_image_14
)
#greentile sample
image_image_15 = PhotoImage(
    file=relative_to_assets("image-15.png"))
image_15 = canvas.create_image(
    430.0,
    390.0,
    image=image_image_15
)
#greentile sample
image_image_16 = PhotoImage(
    file=relative_to_assets("image-16.png"))
image_16 = canvas.create_image(
    598.0,
    390.0,
    image=image_image_16
)
#greentile sample
image_image_17 = PhotoImage(
    file=relative_to_assets("image-17.png"))
image_17 = canvas.create_image(
    768.0,
    390.0,
    image=image_image_17
)
#greentile sample
image_image_18 = PhotoImage(
    file=relative_to_assets("image-18.png"))
image_18 = canvas.create_image(
    102.0,
    540.0,
    image=image_image_18
)
#greentile sample
image_image_19 = PhotoImage(
    file=relative_to_assets("image-19.png"))
image_19 = canvas.create_image(
    260.0,
    540.0,
    image=image_image_19
)
"""#greentile sample
image_image_20 = PhotoImage(
    file=relative_to_assets("image-20.png"))
image_20 = canvas.create_image(
    386.0,
    540.0,
    image=image_image_20
)"""
#greentile sample
image_image_20 = PhotoImage(
    file=relative_to_assets("image-20.png"))
image_20 = canvas.create_image(
    430.0,
    540.0,
    image=image_image_20
)
#greentile sample
image_image_21 = PhotoImage(
    file=relative_to_assets("image-21.png"))
image_21 = canvas.create_image(
    598.0,
    540.0,
    image=image_image_21
)
#greentile sample
image_image_22 = PhotoImage(
    file=relative_to_assets("image-22.png"))
image_22 = canvas.create_image(
    768.0,
    540.0,
    image=image_image_22
)
#greentile sample
image_image_4 = PhotoImage(
    file=relative_to_assets("image-4.png"))
image_4 = canvas.create_image(
    260.0,
    118.0,
    image=image_image_4
)
#greentile sample
image_image_5 = PhotoImage(
    file=relative_to_assets("image-5.png"))
image_5 = canvas.create_image(
    430.0,
    115.5,
    image=image_image_5
)


#Change colour function
def onclick(table_no):
    canvas.itemconfig(image_dict[table_no],image=image_image_redtile)

#creating the greentile for conversion
image_greentile=PhotoImage(file=relative_to_assets("greentile.png"))

#Change colour function reverse
def convertgreen(table_no):
    canvas.itemconfig(image_dict[table_no],image=image_greentile)

#writing a method to get the number of seats for a particular table, so that on clearance, the table number can be added to the particular seat size
def getseats(table_no):
    if table_no in [1,2,3,4,5,6,7]:
        return 2
    elif table_no in [8,9,10,11,12,13,14,15,16]:
        return 4
    elif table_no in [17,18]:
        return 6
    elif table_no in [19,20]:
        return 8

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat"
)
button_1.place(
    x=1139.0,
    y=655.0,
    width=114.0,
    height=41.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1071.0,
    171.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=904.0,
    y=150.0,
    width=334.0,
    height=42.0
)
def getin(x):
    a=x.get()
    return a
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1071.0,
    251.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=904.0,
    y=230.0,
    width=334.0,
    height=42.0
)

image_image_413 = PhotoImage(
    file=relative_to_assets("image_413.png"))
image_413 = canvas.create_image(
    1000.0,
    150.0,
    image=image_image_413
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    990.0,
    424.0,
    image=image_image_5
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:crelist(),
    relief="flat"
)
button_2.place(
    x=1014.0,
    y=298.0,
    width=114.0,
    height=41.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:table_clearence(),
    relief="flat"
)
button_3.place(
    x=1019.0,
    y=533.0,
    width=114.0,
    height=41.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1074.0,
    490.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_3.place(
    x=907.0,
    y=469.0,
    width=334.0,
    height=42.0
)

#Table 1 details
canvas.create_text(
    59.0,
    84.0,
    anchor="nw",
    text="Table 1",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)
canvas.create_text(
    65.0,
    115.0,
    anchor="nw",
    text="Seats: 2",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 2 details
canvas.create_text(
    220.0,
    84.0,
    anchor="nw",
    text="Table 2",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)

canvas.create_text(
    227.0,
    115.0,
    anchor="nw",
    text="Seats: 2",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)


#table 3 details
canvas.create_text(
    389.0,
    84.0,
    anchor="nw",
    text="Table 3",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)
canvas.create_text(
    396.0,
    115.0,
    anchor="nw",
    text="Seats: 2",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 4 details
canvas.create_text(
    558.0,
    84.0,
    anchor="nw",
    text="Table 4",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)
canvas.create_text(
    570.0,
    115.0,
    anchor="nw",
    text="Seats: 2",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)


#table 5 details
canvas.create_text(
    727.0,
    84.0,
    anchor="nw",
    text="Table 5",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)

canvas.create_text(
    734.0,
    115.0,
    anchor="nw",
    text="Seats: 2",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 6 details
canvas.create_text(
    59.0,
    210.0,
    anchor="nw",
    text="Table 6",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)
canvas.create_text(
    65.0,
    240.0,
    anchor="nw",
    text="Seats: 2",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 7 details
canvas.create_text(
    220.0,
    210.0,
    anchor="nw",
    text="Table 7",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)
canvas.create_text(
    227.0,
    240.0,
    anchor="nw",
    text="Seats: 2",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 8 details
canvas.create_text(
    389.0,
    210.0,
    anchor="nw",
    text="Table 8",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)
canvas.create_text(
    396.0,
    240.0,
    anchor="nw",
    text="Seats: 4",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 9 details
canvas.create_text(
    557.0,
    210.0,
    anchor="nw",
    text="Table 9",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)

canvas.create_text(
    565.0,
    240.0,
    anchor="nw",
    text="Seats: 4",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 10 details

canvas.create_text(
    719.0,
    210.0,
    anchor="nw",
    text="Table 10",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)

canvas.create_text(
    734.0,
    240.0,
    anchor="nw",
    text="Seats: 4",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 11 details
canvas.create_text(
    51.0,
    360.0,
    anchor="nw",
    text="Table 11",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)

canvas.create_text(
    65.0,
    390.0,
    anchor="nw",
    text="Seats: 4",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)


#table 12 details
canvas.create_text(
    214.0,
    360.0,
    anchor="nw",
    text="Table 12",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)


canvas.create_text(
    227.0,
    390.0,
    anchor="nw",
    text="Seats: 4",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 13 details
canvas.create_text(
    383.0,
    360.0,
    anchor="nw",
    text="Table 13",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)
canvas.create_text(
    396.0,
    390.0,
    anchor="nw",
    text="Seats: 4",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 14 details
canvas.create_text(
    549.0,
    360.0,
    anchor="nw",
    text="Table 14",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)

canvas.create_text(
    565.0,
    390.0,
    anchor="nw",
    text="Seats: 4",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 15 deatails
canvas.create_text(
    719.0,
    360.0,
    anchor="nw",
    text="Table 15",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)

canvas.create_text(
    734.0,
    390.0,
    anchor="nw",
    text="Seats: 4",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 16 details
canvas.create_text(
    51.0,
    510.0,
    anchor="nw",
    text="Table 16",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)


canvas.create_text(
    59.0,
    540.0,
    anchor="nw",
    text="Seats: 4",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 17 details
canvas.create_text(
    214.0,
    510.0,
    anchor="nw",
    text="Table 17",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)

canvas.create_text(
    227.0,
    540.0,
    anchor="nw",
    text="Seats: 6",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 18 details
canvas.create_text(
    386.0,
    510.0,
    anchor="nw",
    text="Table 18",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)

canvas.create_text(
    403.0,
    540.0,
    anchor="nw",
    text="Seats: 6",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 19 details
canvas.create_text(
    549.0,
    510.0,
    anchor="nw",
    text="Table 19",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)
canvas.create_text(
    569.0,
    540.0,
    anchor="nw",
    text="Seats: 8",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)

#table 20
canvas.create_text(
    721.0,
    510.0,
    anchor="nw",
    text="Table 20",
    fill="#FFFFFF",
    font=("Nunito Bold", 24 * -1)
)
canvas.create_text(
    737.0,
    540.0,
    anchor="nw",
    text="Seats: 8",
    fill="#FFFFFF",
    font=("Nunito Bold", 18 * -1)
)
from datetime import date, datetime
today = date.today()
tm = datetime.now()

#time
def updatetime():
    tm = datetime.now()
    timelabel.config(text=tm.strftime("%H:%M:%S"))

def clock():
    tm = datetime.now()
    timelabel.config(text=tm.strftime("%H:%M:%S"))
    timelabel.after(1000,clock)

timelabel=Label(window,text="",font=("Nunito Bold", 15 * -1),bg="white")
timelabel.place(x=1012.0,y=675.0)
clock()

'''canvas.create_text(
    1019.0,
    675.0,
    anchor="nw",
    text= tm.strftime("%H:%M:%S"),
    fill="#000000",
    font=("Nunito Bold", 15 * -1)
)
'''
#date
canvas.create_text(
    1014.0,
    650.0,
    anchor="nw",
    text = today.strftime("%d/%m/%Y"),
    fill="#000000",
    font=("Nunito Bold", 20 * -1)
)

local_table_list=[2,4,6,8]
def table_allocation(party_seats):
    print(party_seats)
    if party_seats in local_table_list:
        """print(local_table_list)
        print(table_dict[party_seats])"""
        if len(table_dict[party_seats])==0:
            if len(local_table_list)==0:
                #print(table_dict)
                messagebox.showwarning("NO AVAILABLE SEATS","NO MORE SEATS AVAILABLE")
            xyz=local_table_list.pop(0)
            if len(local_table_list)==0:
                #print(table_dict)
                messagebox.showwarning("NO AVAILABLE SEATS","NO MORE SEATS AVAILABLE")
                return 
            print(xyz)
            xyz+=2
            return table_allocation(xyz)
        else:
            return table_dict[party_seats].pop(0)
    else:
        if party_seats>max(table_list):
            messagebox.showwarning("Maximum threshold reached","The requested seats is more than the maximum threshold of seats")
        elif party_seats <=0:
            messagebox.showwarning("Invalid input","The entered seats cant be zero or lesser")
        elif len(local_table_list)==0:
            messagebox.showwarning("Tables full","All the tables are currently full")
        else:
            party_seats=party_seats+1
            return table_allocation(party_seats)
def table_clearence(a=entry_3):
    table_no=getin(a)
    count=0
    found=False
    #print(table_booked)
    for a in table_booked:
        count+=1
        if a[2]==int(table_no):
            found=True
            table_booked.pop(count-1)
            seats=getseats(int(table_no))
            if seats not in local_table_list:
                local_table_list.append(seats)
            table_dict[seats].append(int(table_no))
            table_dict[seats].sort()
            convertgreen(int(table_no))
    if found==False:
        messagebox.showwarning("Invalid input","The table requested to clear is invalid or already clear!")

#Button command
image_dict={1:image_3,2:image_4,3:image_31,4:image_41,5:image_7,6:image_8,7:image_9,8:image_10,9:image_11,10:image_12,11:image_13,12:image_14,13:image_15,14:image_16,15:image_17,16:image_18,17:image_19,18:image_20,19:image_21,20:image_22}
table_booked=[]
def crelist(a=entry_1,b=entry_2):
    party_name=getin(a)
    if len(party_name)==0:
        messagebox.showwarning("Invalid input","Give a valid party name")
        return
    party_seats=getin(b)
    party_seats=int(party_seats)
    table_no=table_allocation(party_seats)
    z=[party_name,party_seats,table_no]
    table_booked.append(z)
    onclick(table_no)
    fobj=open("Table_reserved.txt","a")
    fobj.write(str(z))
    fobj.write("\n")
    fobj.close()
       
window.resizable(False, False)
window.mainloop()
""" The format of the given list will be as follows 
[Party Name,Number of people,]"""