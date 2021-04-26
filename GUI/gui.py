from tkinter import Tk, Label, X, Y, LEFT, RIDGE, SUNKEN, Entry


app = Tk()
app.title("Window")
app.geometry("600x500")
font=("roboto", 16)

Label(
	app, 
	text="SEVEN COLORS OF THE RAINBOW", 
	bg="#abcabc",
	fg="#fff",
	font=("impact", 20)
	).grid()

rowIndex = 1
for color in ("Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"):
	Label(
		app, 
		text=color , 
		width=20,
		relief=RIDGE, 
		font=font
		).grid(row=rowIndex, column=0)

	Entry(
		app,
		bg=color,
		relief=SUNKEN, 
		width=10,
		).grid(row=rowIndex, column=1)

	rowIndex += 1

app.mainloop()
