from tkinter import Tk, Label, StringVar, RAISED, Button, LEFT

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

btn = Button(
	root, 
	text="Exit", 
	fg="crimson", 
	command=quit,
	font=("jost", 14, "bold")
	)
btn.pack(side=LEFT)
root.mainloop()
