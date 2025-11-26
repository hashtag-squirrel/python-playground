def convert_flour(input_amount):
    output_amount = input_amount * 125
    return output_amount


def convert_icing_sugar(input_amount):
    output_amount = input_amount * 125
    return output_amount


def convert_granulated_sugar(input_amount):
    output_amount = input_amount * 200
    return output_amount


def convert_cream(input_amount):
    output_amount = input_amount * 240
    return output_amount


def convert_corn_starch(input_amount):
    output_amount = input_amount * 150
    return output_amount


def convert_butter(input_amount):
    output_amount = input_amount * 226
    return output_amount


print("Welcome to the Baking Converter!")

print('''
The following ingredients can be converted:
      
(F)lour - (I)cing Sugar - (G)ranulated Sugar
(C)ream - Corn (S)tarch - (B)utter
      ''')

ingredient = input("Which ingredient would you like to convert? Enter the letter in parentheses. ").lower()
input_amount = int(input("How much does the recipe require in cups? "))


match ingredient:
    case "f":
        output_amount = convert_flour(input_amount)
    case "i":
        output_amount = convert_icing_sugar(input_amount)
    case "g":
        output_amount = convert_granulated_sugar(input_amount)
    case "c":
        output_amount = convert_cream(input_amount)
    case "s":
        output_amount = convert_corn_starch(input_amount)
    case "b":
        output_amount = convert_butter(input_amount)
    case _:
        print("Sorry, I can't find that ingredient.")

print(f"You require {output_amount} grams for your recipe.")