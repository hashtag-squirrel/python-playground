from tkinter import *

root = Tk()

root.title("Welcome to my GUI project")

root.geometry('350x200')

menu = Menu(root)
item = Menu(menu)
item.add_command(label="New")
menu.add_cascade(label="File", menu=item)
root.config(menu=menu)

lbl = Label(root, text="Is this the real life?")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column=1, row=0)

def clicked():
    result = "You wrote " + txt.get()
    lbl.configure(text=result)

btn = Button(root, text = "Is this just fantasy?", fg = "red", command=clicked)
btn.grid(column=2, row=1)

root.mainloop()
