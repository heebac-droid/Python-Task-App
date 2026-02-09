from tkinter import *
from tkinter.font import *

screen = Tk()
font = Font(family="Arial", size=30)

screen.title("Frame Organisation")

# Frame Definitions
frame1 = Frame(screen, bg="#000000", width=10, height=5, relief="groove", bd=5)
frame1.grid(column=10,row=10)

# Label Definitions
label1 = Label(frame1, text="This is a frame! 🤪", font=font)
label1.grid(column=5, row=5)

screen.mainloop()

