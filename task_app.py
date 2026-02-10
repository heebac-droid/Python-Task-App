from tkinter import *
from tkinter.font import *

screen = Tk()

# Different function definitions for processes
def clicking():
    user_result = f"Your task name is: {user_input.get()}"
    hidden_label.configure(text = user_result)


screen.title("Task app")
text = "Enter task here please"
font = Font(family="Arial", size=30)
button_font = Font(family="Arial", size=20)

hello = "hello mate"

# Label definitions
text_label = Label(screen, text=text, font=font)
text_label.grid(column=1, row=2)
hidden_label = Label(screen, text="", font=font)
hidden_label.grid(column=3, row=6)
# Creating the menu 

# Viewbar settings
view_bar = Menu(screen)

# File sub-menu
file_sys = Menu(view_bar)
file_sys.add_command(label="List Tasks")
view_bar.add_cascade(label='Tasks', menu=file_sys)

# Leave application sub-menu
leaving_now = Menu(view_bar)
leaving_now.add_command(label='Are you sure? 🤔',command = screen.destroy)
view_bar.add_cascade(label='Leave application',menu=leaving_now)

# Displaying the main menu bar
screen.config(menu=view_bar)

# Creating Entry field
user_input = Entry(screen, width=10, cursor="xterm")
user_input.grid(column=2,row=2)

# Button Definitions
button1 = Button(screen, text="Click me please 🤓", fg="blue",command=clicking, width=15, height=6, font=button_font)

# Outputting labels onto screen
button1.grid(column=3, row=2)


# Executing entire program
screen.mainloop()
