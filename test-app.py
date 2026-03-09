#from tkinter import *
#from tkinter.font import *

#screen = Tk()

# This is a prototype for what is supposed to come for the task-app project in tkinter

class task:
    def __init__(self,name,dateCreated,date,duration,dateComplete):
        self.name = name
        self.dateCreated = dateCreated
        self.date = date
        self.duration = duration
        self.dateComplete = dateComplete
    def printTaskName(self):
        return f"task name: {self.name}"

task1 = task("Clean house",2,5,60,4)
task2 = task("Compelte homework",2,5,60,4)

print(task1.printTaskName())
print(task2.printTaskName())

#screen.mainloop()
