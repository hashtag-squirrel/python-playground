import tkinter as tk


# GUI constants
LARGE_PAD = 40
SMALL_PAD = 10
LARGE_FONT = ("Arial", 25)
DEFAULT_FONT = ("Arial", 15)


def start():
    """Returns to start screen/New conversion"""
    clear_frame(main_frame)

    lbl = tk.Label(
        main_frame,
        text="Click the button below to start conversion", # noqa
        font=DEFAULT_FONT)
    lbl.pack(side="top", pady=SMALL_PAD)

    centered_frame = tk.Frame(main_frame, width=200, height=200)
    centered_frame.pack(side="top", pady=SMALL_PAD)

    btn = tk.Button(
        centered_frame,
        text="Single ingredient",
        font=DEFAULT_FONT,
        command=single_ingredient)
    btn.pack(side="left", pady=SMALL_PAD, padx=SMALL_PAD)

    # btn = tk.Button(
    #     centered_frame,
    #     text="Recipe file",
    #     font=DEFAULT_FONT,
    #     command=recipe_file)
    # btn.pack(side="left", pady=SMALL_PAD, padx=SMALL_PAD)


def clear_frame(frame):
    # Iterate through every widget inside the frame
    for widget in frame.winfo_children():
        widget.destroy()  # deleting widget


def submit_ingredient(var, index, mode):
    clear_frame(main_frame)
    ingredient = opt_ingredient.get()

    lbl = tk.Label(
        main_frame,
        text=f"You picked {ingredient}",
        font=DEFAULT_FONT)
    lbl.pack(side="top", pady=SMALL_PAD)

    lbl = tk.Label(main_frame, text="Pick your unit", font=DEFAULT_FONT)
    lbl.pack(side="top", pady=SMALL_PAD)

    units = list(INGREDIENTS[ingredient[0]][1])
    global opt_unit
    opt_unit = tk.StringVar(value=units[0])

    centered_frame = tk.Frame(main_frame, width=200, height=200)
    centered_frame.pack(side="top", pady=SMALL_PAD)

    tk.OptionMenu(centered_frame, opt_unit, *units).pack(side="top", pady=10)

    opt_unit.trace("w", submit_unit)


def submit_unit(var, index, mode):
    clear_frame(main_frame)
    global unit
    unit = opt_unit.get()
    global ingredient
    ingredient = opt_ingredient.get()

    lbl = tk.Label(main_frame, text=f"You picked {unit}", font=DEFAULT_FONT)
    lbl.pack(side="top", pady=SMALL_PAD)

    lbl = tk.Label(
        main_frame,
        text=f"How many {unit} of {ingredient} do you want to convert? ",
        font=DEFAULT_FONT)
    lbl.pack(side="top", pady=SMALL_PAD)

    centered_frame = tk.Frame(main_frame, width=200, height=200)
    centered_frame.pack(side="top", pady=SMALL_PAD)

    global amount
    amount = tk.Entry(centered_frame)
    amount.pack()

    btn = tk.Button(main_frame, text="Submit", command=submit)
    btn.pack(side="bottom", pady=LARGE_PAD)


def submit():
    grams = int(amount.get()) * INGREDIENTS[ingredient[0]][1][unit]
    clear_frame(main_frame)
    lbl = tk.Label(
        main_frame,
        text=f"You need {grams} grams of {ingredient} for your recipe!",
        font=DEFAULT_FONT)
    lbl.pack(side="top", pady=SMALL_PAD)


# Converter functions
def single_ingredient():
    clear_frame(main_frame)
    lbl = tk.Label(main_frame, text="Pick your ingredient", font=LARGE_FONT)
    lbl.pack(side="top", pady=SMALL_PAD)

    centered_frame = tk.Frame(main_frame, width=200, height=200)
    centered_frame.pack(side="top", pady=SMALL_PAD)

    # Dropdown options
    ingredients = []
    for ingredient in INGREDIENTS:
        ingredients.append(INGREDIENTS[ingredient][0])

    # Selected option variable
    global opt_ingredient
    opt_ingredient = tk.StringVar(value="flour")

    # Dropdown menu
    tk.OptionMenu(
        centered_frame,
        opt_ingredient,
        *ingredients).pack(side="top", pady=10)

    opt_ingredient.trace("w", submit_ingredient)


def recipe_file():
    clear_frame(main_frame)
    lbl = tk.Label(main_frame, text="You chose recipe file", font=LARGE_FONT)
    lbl.pack(side="top", pady=SMALL_PAD)


def convert(ingredient, unit, amount):
    """Returns the converted output in grams"""
    output_amount = amount * ingredient[1][unit]
    print(f"\nYou require {output_amount} grams of {ingredient[0]} for your recipe.") # noqa

    return output_amount


window = tk.Tk()

window.title("Baking Converter")

window.geometry('1280x720')

# Creating menu bar
menubar = tk.Menu(window)

# File menu
menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu", menu=menu)
menu.add_command(label="New Conversion", command=start)
menu.add_separator()
menu.add_command(label='Exit', command=window.destroy)

# Help menu
help = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help)
help.add_command(label="Ingredients", command=None)
help.add_command(label="File requirements", command=None)
help.add_separator()
help.add_command(label="About BakingConverter", command=None)

# Start screen
welcome_lbl = tk.Label(
    window,
    text="Welcome to the Baking Converter!",
    font=LARGE_FONT)
welcome_lbl.pack(side="top", pady=LARGE_PAD)

main_frame = tk.Frame(window, width=300, height=300)
main_frame.pack(side="top", pady=SMALL_PAD)

btn = tk.Button(window, text="Home", command=start)
btn.pack(side="bottom", pady=LARGE_PAD)


start()
# display_ingredients()

INGREDIENTS = {
        "f": ["flour", {"cups": 125, "tablespoons": 9}],
        "i": ["icing sugar", {"cups": 125}],
        "g": ["granulated sugar", {"cups": 200, "tablespoons": 12.6}],
        "c": ["cream", {"cups": 240, "tablespoons": 15}],
        "s": ["corn starch", {"cups": 150, "teaspoons": 3.3}],
        "b": ["butter", {"cups": 226, "sticks": 113, "tablespoons": 14}]
    }

window.config(menu=menubar)
window.mainloop()
