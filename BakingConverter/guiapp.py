from tkinter import *
import tkinter.font as tkFont

root = Tk()

my_font = tkFont.Font(family="Arial", size=20, weight=tkFont.NORMAL)

root.title("Baking Converter")

root.geometry('1280x720')

# Creating menu bar
menubar = Menu(root)

# File menu
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="New Conversion", command=None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Help menu
help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help)
help.add_command(label="Ingredients", command=None)
help.add_command(label="File requirements", command=None)
help.add_separator()
help.add_command(label="About BakingConverter", command=None)



lbl = Label(root, text="Welcome to the Baking Converter!", font=my_font)
lbl.pack(side="top", pady=10)



def clicked():
    result = "You wrote " + txt.get()
    lbl.configure(text=result)



# Textbox for entry:
units = ["cups", "tablespoons"]
txt = Spinbox(root, justify="center", values=units)
txt.pack(side="top", pady=10)

# button:
btn = Button(root, text = "Is this just fantasy?", fg = "red", command=clicked)
btn.pack(side="top", pady=10)


root.config(menu = menubar)
root.mainloop()

