from tkinter import *

# GUI functions
def start():
    """Returns to start screen/New conversion"""
    clear_frame(frame1)

    lbl = Label(frame1, text="Would you like to convert a single ingredient or convert a recipe file?", font=("Arial", 25))
    lbl.pack(side="top", pady=10)

    centered_frame = Frame(frame1, width=200, height=200)
    centered_frame.pack(side="top", pady=10)

    btn = Button(centered_frame, text = "Single ingredient", command = single_ingredient)
    btn.pack(side="left", pady=10, padx=5)

    btn = Button(centered_frame, text = "Recipe file", command = recipe_file)
    btn.pack(side="left", pady=10, padx=5)


def display_ingredients():
    """Displays buttons for all available ingredients for conversion"""
    btn = Button(frame1, text = "Single ingredient", command = single_ingredient)
    btn.pack()


def clear_frame(frame):
    # Iterate through every widget inside the frame
    for widget in frame.winfo_children():
        widget.destroy()  # deleting widget


# Converter functions
def single_ingredient():
    clear_frame(frame1)
    lbl = Label(frame1, text="You chose single ingredient", font=("Arial", 25))
    lbl.pack(side="top", pady=10)


def recipe_file():
    clear_frame(frame1)
    lbl = Label(frame1, text="You chose recipe file", font=("Arial", 25))
    lbl.pack(side="top", pady=10)


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
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="New Conversion", command=start)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Help menu
help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help)
help.add_command(label="Ingredients", command=None)
help.add_command(label="File requirements", command=None)
help.add_separator()
help.add_command(label="About BakingConverter", command=None)

# Start screen
lbl = Label(root, text="Welcome to the Baking Converter!", font=("Arial", 25))
lbl.pack(side="top", pady=10)

frame1 = Frame(root, width=300, height=300)
frame1.pack(side="top", pady=10)

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

