from tkinter import Tk, Label

root = Tk()
root.title("First GUI application")
	
x = Label(root, text="Hello World!", font=("jost", 30))
# x.grid()
x.pack()

root.mainloop()
