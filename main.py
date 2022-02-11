from re import A
from time import time
from tkinter import *


time_left = 5
timer = None
time_to_save = None


def click(key):
    global time_left, timer
    root.after_cancel(timer)
    count_down(time_left)
    # print(key.char)

    return time_left


def count_down(count):
    if count > 0:
        global time_left, timer
        timer = root.after(1000, count_down, count - 1)

    else:
        entry.delete("1.0", END)
        root.after_cancel(timer)


def choose_difficulty():
    global time_to_save, time_left
    if clicked.get() == "Easy(15 sec)":
        time_to_save = 15
    elif clicked.get() == "Medium(30 sec)":
        time_to_save = 30
    else:
        time_to_save = 60
    entry.focus()
    save_timer(time_to_save)
    count_down(time_left)


def save_timer(counter):
    global time_to_save, usr_input
    root.after(1000, save_timer, counter - 1)
    usr_input = entry.get("1.0", END)

    if counter == 0:
        save_button = Button(root, text="Save",
                             command=save_to_file)
        save_button.grid(row=1, column=1)


def save_to_file():
    with open("Brave.txt", "w") as file:
        file.write(usr_input)


############################ USER INTERFACE ##################
root = Tk()
root.title("The Brave Editor")


difficulty_label = Label(text="Difficulty")
difficulty_label.grid(row=1, column=0)


############################ DROPDOWN MENU ##################

options = ["Easy(15 sec)", "Medium(30 sec)", "Hard(60 sec)"]

clicked = StringVar()
clicked.set(options[0])

option = OptionMenu(root, clicked, *options)
# option.config(bg="#E6EFBF")
option["highlightthickness"] = 0
option.grid(row=2, column=0)

############################ BUTTONS ##################

select_button = Button(root, text="Select",
                       command=choose_difficulty).grid(row=2, column=1)


############################ ENTRY ##################
entry = Text()
entry.grid(row=3, columnspan=2, column=0)

# Bind entry to any keypress
entry.bind("<Key>", click)


root.mainloop()
