from tkinter import Tk, IntVar, Radiobutton


app = Tk()
app.title("Window")
app.geometry("600x500")

# Gender: Male or Female, Non-binary, 
# Month Joined: Jan - December
# User Type: Member or Guest
# Email settings: Weekly, Daily, Monthly Round-up

# GENDER
gender = IntVar()
male = Radiobutton(app, text="Male", variable=gender, value=1)
female = Radiobutton(app, text="Female", variable=gender, value=2)
non = Radiobutton(app, text="Non-binary", variable=gender, value=3)

male.grid(column=0, row=0)
female.grid(column=1, row=0)
non.grid(column=2, row=0)


# MONTH JOINED
month = IntVar()
jan = Radiobutton(app, text="Jan", variable=month, value=4)
feb = Radiobutton(app, text="Feb", variable=month, value=5)
march = Radiobutton(app, text="March", variable=month, value=6)
april = Radiobutton(app, text="April", variable=month, value=7)

jan.grid(column=0, row=1)
feb.grid(column=1, row=1)
march.grid(column=2, row=1)
april.grid(column=3, row=1)


# USER TYPE
membership = IntVar()
member = Radiobutton(app, text="Member", variable=membership, value=8)
guest = Radiobutton(app, text="Guest", variable=membership, value=9)
member.grid(column=0, row=2)
guest.grid(column=1, row=2)


# EMAIL SETTINGS
emailing = IntVar()
daily = Radiobutton(app, text="Daily", variable=emailing, value=10)
weekly = Radiobutton(app, text="Weekly", variable=emailing, value=11)
monthly = Radiobutton(app, text="Monthly Round-up", variable=emailing, value=12)
daily.grid(column=2, row=2)
weekly.grid(column=3, row=2)
monthly.grid(column=4, row=2)


app.mainloop()
