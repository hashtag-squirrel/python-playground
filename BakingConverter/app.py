def convert(ingredient):
    ingredients = {
        "f": ["flour", {"cups": 125, "tablespoons": 9}],
        "i": ["icing sugar", {"cups": 125}],
        "g": ["granulated sugar", {"cups": 200, "tablespoons": 12.6}],
        "c": ["cream", {"cups": 240, "tablespoons": 15} ],
        "s": ["corn starch", {"cups": 150, "teaspoons": 3.3}],
        "b": ["butter", {"cups": 226, "sticks": 113, "tablespoons": 14}]
    }

    current_ingredient = ingredients[ingredient]
    available_units = list(current_ingredient[1])
    print("Which unit would you like to convert? ")
    for unit in available_units:
        print(unit)
    input_unit = input("\nEnter unit (full word): \n").lower()
    input_amount = int(input(f"\nHow much does the recipe require in {input_unit}? \n"))
    output_amount = input_amount * current_ingredient[1][input_unit]

    print(f"\nYou require {output_amount} grams of {current_ingredient[0]} for your recipe.")

    return output_amount


print("Welcome to the Baking Converter!")

print('''
The following ingredients can be converted:
      
(F)lour - (I)cing Sugar - (G)ranulated Sugar
(C)ream - Corn (S)tarch - (B)utter
      ''')

ingredient = input("Which ingredient would you like to convert? Enter the letter in parentheses. ").lower()
output_amount = convert(ingredient)
