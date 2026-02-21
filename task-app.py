from tkinter import *
from tkinter.font import *

def taskConfirmation():
    taskLst.append(taskEntry.get())
    taskConfirmText = f"Task added: {taskEntry.get()}"
    taskConfirmLabel = Label(text=taskConfirmText, font=normalTextFont)
    taskConfirmLabel.place(x=75, y=500)

def errorEraseCommand():
    noAvaliableTasks.place_forget()

def listTasks():
    n = 600
    for t in taskLst:
        taskListText = f"Avaliable tasks: {t}"
        listTasksLabel = Label(screen, text=taskListText, font=normalTextFont)
        listTasksLabel.place(x=75, y=n)
        n += 50
    if len(taskLst) == 0:
        noAvaliableTasks.place(x=75, y=150)

screen = Tk()

screen.title("Task App")

# Font customisation

titleFont = Font(family="JetBrainsMono Nerd Font", size=30)
normalTextFont = Font(family="JetBrainsMono Nerd Font", size=20)

welcomeTextLabel = Label(screen, text="Welcome to the task app! 😁", font=titleFont, bg="#14e81b")
welcomeTextLabel.place(x=150, y=50)

taskLst = []

noAvaliableTasks = Label(screen, text="There are no avaliable tasks at the moment", font=normalTextFont)

# Creating a menu hub that stores the rest of the menus

menuBar = Menu(screen) 
TaskMenu = Menu(menuBar)
ErrorMenu = Menu(menuBar)
menuBar.add_cascade(label="Tasks", menu = TaskMenu)
menuBar.add_cascade(label="Errors", menu = ErrorMenu)
TaskMenu.add_command(label="List all avaliable tasks", command=listTasks)
ErrorMenu.add_command(label="Remove no avaliable tasks error message", command=errorEraseCommand)
screen.config(menu = menuBar)

enterTaskFrame = Frame(screen, relief="raised", bd=7, height=175, width=100)
enterTaskFrame.place(x=75, y=275)

taskName = Label(enterTaskFrame, text="Task name: ", font=normalTextFont)
taskName.pack(side=LEFT)

taskEntry = Entry(enterTaskFrame,font=normalTextFont)
taskEntry.pack(side=LEFT)

taskSubmit = Button(enterTaskFrame, text="Submit task", width=15, height=3, font=normalTextFont, command=taskConfirmation)
taskSubmit.pack(side=LEFT, padx=20)

# Executes the entire program
screen.mainloop()
