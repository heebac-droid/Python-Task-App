from tkinter import *
from tkinter.font import *

print("hello")

screen = Tk()
font = Font(family="Arial", size=30)

screen.title("Frame Organisation")

# Frame Definitions
frame1 = Frame(screen, bg="#000000", width=10, height=5, relief="raised", bd=5, cursor="hand2")
frame1.pack(padx=50, pady=10)

# Label Definitions
label1 = Label(frame1, text="This is a frame! 🤪", font=font)
label1.pack()

screen.mainloop()

