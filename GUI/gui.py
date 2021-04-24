from tkinter import Tk, Frame, Label, Button, LEFT, RIGHT


root = Tk()
root.title("Window")
root.geometry("300x300")
frame = Frame(root)
frame.pack()

left = Frame(root)
left.pack(side=LEFT)
right = Frame(root)
right.pack(side=RIGHT)

btnA = Button(
	frame, 
	fg="red",
	activebackground="crimson",
	text="Submit", 
	font=("jost", 14, "bold")
	)
btnA.pack(side=LEFT)

btnB = Button(
	frame, 
	fg="green",
	activebackground="green",
	text="Remove", 
	font=("jost", 14, "bold")
	)
btnB.pack(side=RIGHT)

btnC = Button(
	frame, 
	fg="black",
	activebackground="#ABCABC",
	text="Add", 
	font=("jost", 14, "bold")
	)
btnC.pack(side=LEFT)


root.mainloop()
