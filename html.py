from tkinter import *
from PIL import Image  , ImageTk

window=Tk()

window.title("HTML IDE")
window.minsize(600,600)
window.maxsize(600,600)

window.configure(background ="SandyBrown")

run = ImageTk.PhotoImage(Image.open("run.png"))
open = ImageTk.PhotoImage(Image.open("open_file.png"))
save = ImageTk.PhotoImage(Image.open("save_file.png"))


label = Label(window , text = "File Name")
label.place(relx= 0.38 , rely = 0.05 , anchor = CENTER)

input = Entry(window)
input.place(relx = 0.6 , rely=0.05 , anchor = CENTER)

textArea = Text(window , height = 35 , width = 80)
textArea.place(relx=0.5 , rely = 0.5  , anchor = CENTER)







window.mainloop()