from tkinter import *
from tkinter.font import *

screen = Tk()

screen.title("Task App")

# Font customisation

titleFont = Font(family="JetBrainsMono Nerd Font", size=30)
normalTextFont = Font(family="JetBrainsMono Nerd Font", size=20)

welcomeTextLabel = Label(screen, text="Welcome to the task app! 😁", font=titleFont, bg="#14e81b")
welcomeTextLabel.place(x=150, y=375)

# Details how to enter a task into the app

taskName = Label(screen, text="Task name: ", font=normalTextFont)
taskName.pack(side=LEFT)

taskEntry = Entry(screen,font=normalTextFont)
taskEntry.pack(side=LEFT)

taskSubmit = Button(screen, text="Submit task", width=15, height=2, font=normalTextFont)
taskSubmit.pack(side=LEFT, padx=20)

# Executing entire program
screen.mainloop()
