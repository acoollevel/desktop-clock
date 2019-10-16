from tkinter import *
import time, datetime
from time import gmtime, strftime

root = Tk()

# Window Attributes
root.overrideredirect(1)
root.wm_attributes("-transparentcolor", "gray99")

running = True

# close window
def close(event):
    global running
    running = False

root.bind('<Escape>', close)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

timeframe = Frame(root, width=screen_width, height=screen_height, bg="gray99")
timeframe.grid(row=0,column=0)

tkintertime = StringVar()
timelabel = Label(timeframe, textvariable=tkintertime, fg="white", bg="gray99", font=("NovaMono", 40))
timelabel.place(y=screen_height/2 - 60, x=screen_width/2, anchor="center")

tkinterdate = StringVar()
datelabel = Label(timeframe, textvariable=tkinterdate, fg="white", bg="gray99", font=("Bahnschrift", 15))
datelabel.place(y=screen_height/2 + 60, x=screen_width/2, anchor="center")


while running:
    tkintertime.set(value=strftime("%H:%M:%S"))
    tkinterdate.set(value=strftime("%A, %e %B"))
    root.update_idletasks()
    root.update()
    time.sleep(1)
