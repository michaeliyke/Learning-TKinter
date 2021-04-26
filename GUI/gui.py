from tkinter import Tk, Label, StringVar, OptionMenu


app = Tk()
app.title("Window")
app.geometry("600x500")
variable = StringVar(app)
variable.set("May be")

options = OptionMenu(app, variable, "Yes", "No", "Not sure", "May be")
options.pack()

app.mainloop()
