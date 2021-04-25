from tkinter import Tk, IntVar, Radiobutton


app = Tk()
app.title("Window")
app.geometry("600x500")
radioInt = IntVar()

# Gender: Male or Female, Non-binary, 
# Month Joined: Jan - December
# User Type: Member or Guest
# Email settings: Weekly, Daily, Monthly Round-up


radio1 = Radiobutton(app, text="January", variable=radioInt, value=1)
radio2 = Radiobutton(app, text="February", variable=radioInt, value=2)
radio3 = Radiobutton(app, text="March", variable=radioInt, value=3)
radio4 = Radiobutton(app, text="April", variable=radioInt, value=4)
radio1.grid(column=0, row=0)
radio2.grid(column=0, row=1)
radio3.grid(column=0, row=2)
radio4.grid(column=0, row=3)

app.mainloop()
