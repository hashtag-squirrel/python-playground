from tkinter import *

# GUI constants
LARGE_PAD = 40
SMALL_PAD = 10
LARGE_FONT = ("Arial", 25)
DEFAULT_FONT = ("Arial", 15)

# GUI functions
def start():
    """Returns to start screen/New conversion"""
    clear_frame(frame1)

    lbl = Label(frame1, text="Would you like to convert a single ingredient or convert a recipe file?", font=DEFAULT_FONT)
    lbl.pack(side="top", pady=SMALL_PAD)

    centered_frame = Frame(frame1, width=200, height=200)
    centered_frame.pack(side="top", pady=SMALL_PAD)

    btn = Button(centered_frame, text = "Single ingredient", font=DEFAULT_FONT,  command = single_ingredient)
    btn.pack(side="left", pady=SMALL_PAD, padx=SMALL_PAD)

    btn = Button(centered_frame, text = "Recipe file", font=DEFAULT_FONT, command = recipe_file)
    btn.pack(side="left", pady=SMALL_PAD, padx=SMALL_PAD)


def clear_frame(frame):
    # Iterate through every widget inside the frame
    for widget in frame.winfo_children():
        widget.destroy()  # deleting widget


def submit(opt):  
    centered_frame = Frame(frame1, width=200, height=200)
    centered_frame.pack(side="top", pady=SMALL_PAD)
    lbl = Label(centered_frame, text="", font=LARGE_FONT)
    lbl.pack(side="top", pady=SMALL_PAD)
    lbl.config(text=opt.get())
    

# Converter functions
def single_ingredient():
    clear_frame(frame1)
    lbl = Label(frame1, text="Pick your ingredient", font=LARGE_FONT)
    lbl.pack(side="top", pady=SMALL_PAD)

    centered_frame = Frame(frame1, width=200, height=200)
    centered_frame.pack(side="top", pady=SMALL_PAD)
    
    # Dropdown options 
    ingredients = []
    for ingredient in INGREDIENTS:
        ingredients.append(INGREDIENTS[ingredient][0])

    # Selected option variable  
    opt = StringVar(value="flour")

    # Dropdown menu  
    OptionMenu(centered_frame, opt, *ingredients).pack(side="top", pady=10)

    # Button to update label  
    btn = Button(centered_frame, text="Submit", command=submit(opt))
    btn.pack()


def recipe_file():
    clear_frame(frame1)
    lbl = Label(frame1, text="You chose recipe file", font=LARGE_FONT)
    lbl.pack(side="top", pady=SMALL_PAD)


def convert(ingredient, unit, amount):
    """Returns the converted output in grams"""
    output_amount = amount * ingredient[1][unit]
    print(f"\nYou require {output_amount} grams of {ingredient[0]} for your recipe.")

    return output_amount


root = Tk()

root.title("Baking Converter")

root.geometry('1280x720')

# Creating menu bar
menubar = Menu(root)

# File menu
menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu", menu=menu)
menu.add_command(label="New Conversion", command=start)
menu.add_separator()
menu.add_command(label ='Exit', command = root.destroy)

# Help menu
help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help)
help.add_command(label="Ingredients", command=None)
help.add_command(label="File requirements", command=None)
help.add_separator()
help.add_command(label="About BakingConverter", command=None)

# Start screen
welcome_lbl = Label(root, text="Welcome to the Baking Converter!", font=LARGE_FONT)
welcome_lbl.pack(side="top", pady=LARGE_PAD)

frame1 = Frame(root, width=300, height=300)
frame1.pack(side="top", pady=SMALL_PAD)

btn = Button(root, text="Home", command=start)
btn.pack(side="bottom", pady=LARGE_PAD)


def show():  
    lbl.config(text=opt.get())  

# Dropdown options  
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  

# Selected option variable  
opt = StringVar(value="Monday")  

# Dropdown menu  
OptionMenu(root, opt, *days).pack()  

# Button to update label  
Button(root, text="Click Me", command=show).pack()  

lbl = Label(root, text=" ")  
lbl.pack()

start()
# display_ingredients()

INGREDIENTS = {
        "f": ["flour", {"cups": 125, "tablespoons": 9}],
        "i": ["icing sugar", {"cups": 125}],
        "g": ["granulated sugar", {"cups": 200, "tablespoons": 12.6}],
        "c": ["cream", {"cups": 240, "tablespoons": 15} ],
        "s": ["corn starch", {"cups": 150, "teaspoons": 3.3}],
        "b": ["butter", {"cups": 226, "sticks": 113, "tablespoons": 14}]
    }

# Textbox for entry:
# units = ["cups", "tablespoons"]
# txt = Spinbox(root, justify="center", values=units)
# txt.pack(side="top", pady=10)

# # button:
# btn = Button(root, text = "Is this just fantasy?", fg = "red", command=clicked)
# btn.pack(side="top", pady=10)


root.config(menu = menubar)
root.mainloop()

