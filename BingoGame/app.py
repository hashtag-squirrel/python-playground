import random

def generate_col_numbers(col):
    """Generates the randomized column numbers"""
    numbers = []

    while len(numbers) < 5:
        match col:
            case 0:
                new_number = random.randint(1,16)
            case 1:
                new_number = random.randint(16,31)
            case 2:
                new_number = random.randint(31, 46)
            case 3:
                new_number = random.randint(46, 61)
            case 4:
                new_number = random.randint(61, 75)
        if new_number not in numbers:
            numbers.append(new_number)
    return numbers


def generate_card():
    """Generates the randomized card numbers"""
    card = []
    for col in range(5):
        col_numbers = generate_col_numbers(col)
        card.append(col_numbers)
    return card


def print_card(card):
    """prints out the card in a formatted way""" 
    print('''
  B   I   N   G   O ''')
    for row in range(5):
        if row == 2:
                print(f'''
 {card[0][row]}  {card[1][row]}   O  {card[3][row]}  {card[4][row]}''')
        else: print(f'''
 {card[0][row]}  {card[1][row]}  {card[2][row]}  {card[3][row]}  {card[4][row]}''')
            

def update_card(card, number):
    """checks the card for drawn number and updates the card values"""
    i = 0
    coordinates = []
    for list in card:
        if number in list:
            coordinates = [i, list.index(number)]
        i += 1
    if len(coordinates) > 0:
        card[coordinates[0]][coordinates[1]] = "X"
    return card


def draw_number():
    """generates a random number and checks if it was already drawn. 
    Will generate numbers until one wasn't drawn yet."""
    while True:
        drawn_number = random.randint(1,76)
        if drawn_number not in numbers_drawn:
            numbers_drawn.append(drawn_number)
            return drawn_number


def check_card():
    """checks if there is a sequence of 5 Xs or 4 Xs and O in a row, column or diagonally"""
    


numbers_drawn = []
card = generate_card()
print_card(card)
input("Press 'Enter' to start the game.")
while True:
    new_number = draw_number()
    update_card(card, new_number)
    print(new_number)
    print_card(card)
    input("Press 'Enter' to proceed to next turn.")