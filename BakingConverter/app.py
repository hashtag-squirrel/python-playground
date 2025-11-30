def convert(ingredient):
    """Asks for input of unit and amount and returns the converted output in grams"""

    current_ingredient = INGREDIENTS[ingredient]
    
    available_units = list(current_ingredient[1])
    print("Which unit would you like to convert? ")
    for unit in available_units:
        print(unit)
    input_unit = input("\nEnter unit (full word): \n").lower()
    input_amount = int(input(f"\nHow much does the recipe require in {input_unit}? \n"))
    output_amount = input_amount * current_ingredient[1][input_unit]

    print(f"\nYou require {output_amount} grams of {current_ingredient[0]} for your recipe.")

    return output_amount


def parse_file():
    f = open("BakingConverter/recipe.txt", "r")
    lines = f.readlines()
    
    new_file = open("BakingConverter/recipe-metric.txt", "a")

    for line in lines:
        line_elements = line.split(" ")
        input_amount = int(line_elements[0])
        input_unit = line_elements[1]
        ingredient = line_elements[2][0]

        current_ingredient = INGREDIENTS[ingredient]
        output_amount = input_amount * current_ingredient[1][input_unit]
        new_file.write(f'{output_amount} g {current_ingredient[0]}\n')
    
    print("\nYour converted recipe can now be found in the same folder as your original recipe.")
    print("\nThank you for using Baking Converter!\n")


INGREDIENTS = {
        "f": ["flour", {"cups": 125, "tablespoons": 9}],
        "i": ["icing sugar", {"cups": 125}],
        "g": ["granulated sugar", {"cups": 200, "tablespoons": 12.6}],
        "c": ["cream", {"cups": 240, "tablespoons": 15} ],
        "s": ["corn starch", {"cups": 150, "teaspoons": 3.3}],
        "b": ["butter", {"cups": 226, "sticks": 113, "tablespoons": 14}]
    }

print("Welcome to the Baking Converter!")

convert_file = input('Do you want to convert a recipe in a file? (y/n): ').lower().startswith('y')

if convert_file:
    parse_file()

else:
    print('''
    The following ingredients can be converted:
        
    (F)lour - (I)cing Sugar - (G)ranulated Sugar
    (C)ream - Corn (S)tarch - (B)utter
        ''')

    ingredient = input("Which ingredient would you like to convert? Enter the letter in parentheses. ").lower()

    output_amount = convert(ingredient)
