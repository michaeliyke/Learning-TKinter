from tkinter import Tk, Label, StringVar, RAISED, Button, LEFT


def count1():
	global counter
	counter += 1
	label.config(text=str(counter))
	label.after(1000, count1)

def count(label):
	counter = 0
	count1()


root = Tk()
root.title("Counting seconds")
label = Label(
	root, 
	fg="blue",
	font=("jost", 25)
)
label.pack()

counter = 0

count(label)
btn = Button(
	root, 
	text="stop", 
	width=25, 
	command=root.destroy, 
	font=("jost", 14, "bold")
	)
btn.pack()


root.mainloop()
