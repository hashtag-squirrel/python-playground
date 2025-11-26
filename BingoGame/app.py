import random

def generate_col_numbers(col):
    """Generates the randomized column numbers
    Returns a list of numbers representing a column"""

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
    if col == 2:
        numbers[2] = "O"
    return numbers


def generate_card():
    """Generates the randomized card numbers
    Returns the nested card list"""

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
        print(f'''
 {card[0][row]}  {card[1][row]}  {card[2][row]}  {card[3][row]}  {card[4][row]}''')
            

def update_card(card, number):
    """checks the card for drawn number and updates the card values
    Returns the updated card list"""

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
    Will generate numbers until one wasn't drawn yet.
    Returns the new number"""

    while True:
        drawn_number = random.randint(1,76)
        if drawn_number not in numbers_drawn:
            numbers_drawn.append(drawn_number)
            return drawn_number


def check_columns(card):
    """checks if there is a sequence of 5 Xs or 4 Xs and O in a column
    Returns a boolean"""

    i = 0
    for col in card:
        if i == 2:
            if col.count("X") >=4:
                return True
        else:
            if col.count("X") >= 5:
                return True
        i += 1
    return False


def check_rows(card):
    """checks if there is a sequence of 5 Xs or 4 Xs and O in a row
    Returns a boolean"""

    i = 0
    for i in range(5):
        row = []
        for column in range(5):
            row.append(card[column][i])
        if i == 2:
            if row.count("X") == 4:
                return True
        else: 
            if row.count("X") == 5:
                return True
    return False


def check_diagonals(card):
    """checks if there is a sequence of 4 Xs in a diagonal
    Returns a boolean"""

    if card[0][0] == "X" and card[1,1] == "X" and card[3,3] == "X" and card [4,4] == "X":
        return True
    elif card[0][4] == "X" and card[1,3] == "X" and card[3,1] == "X" and card [4,0] == "X":
        return True
    else: 
        return False


def check_card(card):
    """checks if there is a sequence of 5 Xs or 4 Xs and O in a row, column or diagonally
    Returns a boolean"""

    if check_columns(card) or check_rows(card) or check_diagonals(card):
        return True
        

# Game start - initializing the drawn numbers pool and generating the game card
print("Let's play Bingo!")
numbers_drawn = []
card = generate_card()
print_card(card)
input("Press 'Enter' to start the game.")

# Main game loop
while True:
    # drawing a number (and printing it)
    new_number = draw_number()
    print(f'{new_number}')

    update_card(card, new_number)
    print_card(card)
    if check_card(card):
        print("You won!")
        break
    input("Press 'Enter' to proceed to next turn.")