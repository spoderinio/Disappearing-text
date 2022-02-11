from re import A
from time import time
from tkinter import Tk, Entry, Text, END


root = Tk()
root.title("The Brave Editor")

time_left = 5
timer = None


def click(key):
    global time_left, timer
    root.after_cancel(timer)
    count_down(time_left)
    print(key.char)

    return time_left


def count_down(count):
    if count > 0:
        global time_left, timer
        timer = root.after(1000, count_down, count - 1)
        print(count)
    else:
        entry.delete("1.0", END)
        root.after_cancel(timer)


entry = Text()
entry.grid()
entry.focus()
# Bind entry to any keypress
entry.bind("<Key>", click)

count_down(time_left)


root.mainloop()
