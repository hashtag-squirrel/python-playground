def convert_flour(input_amount):
    output_amount = input_amount * 125
    return output_amount


def convert_icing_sugar(input_amount):
    output_amount = input_amount * 125
    return output_amount


print("Welcome to the Baking Converter!")

print('''
The following ingredients can be converted:
      
(F)lour - (I)cing Sugar - (G)ranulated Sugar
(C)ocoa Powder - Corn (S)tarch - (B)utter
      ''')

ingredient = input("Which ingredient would you like to convert? Enter the letter in parentheses. ").lower()
input_amount = int(input("How much does the recipe require in cups? "))


match ingredient:
    case "f":
        output_amount = convert_flour(input_amount)
    case _:
        print("Sorry, I can't find that ingredient.")

print(f"You require {output_amount} grams for your recipe.")