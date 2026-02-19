from tkinter import *
from tkinter.font import *

screen = Tk()

screen.title("Task App")

# Font customisation

titleFont = Font(family="JetBrainsMono Nerd Font", size=30)
normalTextFont = Font(family="JetBrainsMono Nerd Font", size=20)

welcomeTextLabel = Label(screen, text="Welcome to the task app! 😁", font=titleFont, bg="#14e81b")
welcomeTextLabel.place(x=150, y=50)

taskLst = []

def listTasks():
    n = 600
    print(taskLst)
    for t in taskLst:
        taskListText = f"Avaliable tasks: {t}"
        print(taskListText)
        listTasksLabel = Label(screen, text=taskListText, font=normalTextFont)
        listTasksLabel.place(x=75, y=n)
        n += 50

menuBar = Menu(screen) # Creating a menu hub that stores the rest of the menus
TaskMenu = Menu(menuBar)
menuBar.add_cascade(label="Tasks", menu = TaskMenu)
TaskMenu.add_command(label="List all avaliable tasks", command=listTasks)
screen.config(menu = menuBar)




# Task confirmation

def taskConfirmation():
    taskLst.append(taskEntry.get())
    taskConfirmText = f"Task added:{taskEntry.get()}"
    taskConfirmLabel = Label(text=taskConfirmText, font=normalTextFont)
    taskConfirmLabel.place(x=75, y=500)


# Details how to enter a task into the app

# Frame for enterring a task

enterTaskFrame = Frame(screen, relief="raised", bd=7, height=175, width=100)
enterTaskFrame.place(x=75, y=275)


taskName = Label(enterTaskFrame, text="Task name: ", font=normalTextFont)
taskName.pack(side=LEFT)

taskEntry = Entry(enterTaskFrame,font=normalTextFont)
taskEntry.pack(side=LEFT)

taskSubmit = Button(enterTaskFrame, text="Submit task", width=15, height=3, font=normalTextFont, command=taskConfirmation)
taskSubmit.pack(side=LEFT, padx=20)

# Executing entire program
screen.mainloop()
