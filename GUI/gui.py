from tkinter import Tk, Label, StringVar, RAISED

root = Tk()
root.title("First GUI application")
txtVar = StringVar()
x = Label(
	root, 
	textvariable=txtVar,
	relief=RAISED,
	fg="indigo" ,
	bg="silver",
	font=("jost", 30, "bold")
	)

txtVar.set("Welcome to TKinter Framework!")
# x.grid()
x.pack()

root.mainloop()
