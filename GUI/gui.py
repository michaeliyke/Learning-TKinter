from tkinter import Tk, Label, X, Y, LEFT, RIDGE, SUNKEN, Entry, Button


app = Tk()
app.title("Window")
app.geometry("450x400")
font=("Tahoma", 16)

Label(app, text="Maths").place(x=100, y=20)
Entry(app, bd=5).place(x=160, y=20)

Label(app, text="Bio").place(x=100, y=55)
Entry(app, bd=4).place(x=160, y=50)

Label(app, text="Total").place(x=100, y=160)
Entry(app, bd=5).place(x=160, y=160)

Button(app, text="Add").place(x=200, y=100)
app.mainloop()
