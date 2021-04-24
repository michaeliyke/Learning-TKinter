from tkinter import Tk, Frame, Label, Button, LEFT, RIGHT, IntVar, Checkbutton, W


root = Tk()
root.title("Window")
root.geometry("300x300")
var1 = IntVar()
var2 = IntVar()

Checkbutton(root, text="Male", variable=var1).grid(row=0, sticky=W)
Checkbutton(root, text="Female", variable=var2).grid(row=1, sticky=W)

root.mainloop()
