from tkinter import Tk, Label, X, Y, LEFT


app = Tk()
app.title("Window")
app.geometry("600x500")
font=("roboto", 16)

Label(
	app, 
	text="Favourite Languages", 
	bg="#abcabc",
	fg="#fff",
	font=("impact", 20)
	).pack(fill=X)
i = 0
for lang in ("C", "C++", "Java", "Python", "JavaScript", "PHP"):
	Label(
		app, 
		text=lang , 
		bg="#000", 
		fg="#ebebeb", 
		font=font
		).pack(fill=X, pady=5, padx=12)

for lang in ("Ruby", "Perl", "Cobol", "Lisp", "Assembly"):
	Label(
		app, 
		text=lang,
		bg="#777",
		fg="orange",
		font=("cursive", 12)
		).pack(padx=4, side=LEFT)

app.mainloop()
