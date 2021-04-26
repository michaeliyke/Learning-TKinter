from tkinter import Tk, Label, Entry


app = Tk()
app.title("Window")
app.geometry("600x500")

# Gender: Male or Female, Non-binary, 
# Month Joined: Jan - December
# User Type: Member or Guest
# Email settings: Weekly, Daily, Monthly Round-up

Label(app, text="Email Address", font=("jost", 15)).grid(row=0)
Label(app, text="User password", font=("jost", 15)).grid(row=1)

email = Entry(app)
email.grid(row=0, column=1)
password = Entry(app)
password.grid(row=1, column=1)

app.mainloop()
