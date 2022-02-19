import random
import string


def check_input(any_input):
    not_digit = False
    for char in any_input:
        if char not in string.digits:
            not_digit = True
    return not_digit

def give_default_values(k_loop):
    flip = False
    j = 0
    for i in range(0, k_loop):
        if flip == False:
            y.append(8 - i + j)
            x.append(8 - i + j)
            flip = True
        else:
            y.append(8 - i + 1 + j)
            x.append(8 - i + j)
            flip = False
            j += 1


letter = ["A", "B", "C", "D", "E", "F", "G", "H"]

def_input_k = 3             #<-- You may change this one to any positive integer value (please keep it low).
def_replays = 100               #<-- You may change this one to any positive integer value or zero.
enable_user_input = False        #<-- Change this to True to enable user inputs.
set_defaults = False
x = []
y = []
if enable_user_input == True:
    print("--------------------------")
    input_k = input("Give Number Of Configurations: ")
    no_int = check_input(input_k)
    if no_int == False:
        k = int(input_k)
        for i in range(0, k):
            if no_int == False:
                print("For Configuration:   #", i+1)
                input_x = input("Give X Coordinate (2-8): ")
                input_y = input("Give Y Coordinate (2-8): ")
                no_int = check_input(input_x)
                if no_int == False:
                    no_int = check_input(input_y)
                if no_int == False:
                    x.append(int(input_x))
                    y.append(int(input_y))
                    if (x[i] < 2) or (x[i] > 8) or (y[i] < 2) or (y[i] > 8):
                        no_int = True
    if no_int == True:
        print("User Input Error.")
        set_defaults = True

if (enable_user_input == False) or (set_defaults == True):
    x = []
    y = []
    k = def_input_k
    give_default_values(k)

set_defaults = False
if enable_user_input == True:
    input_replays = input("Give Number Of Replays: ")
    no_int = check_input(input_replays)
    if no_int == False:
        replays = int(input_replays)
    else:
        print("User Input Error.")
        set_defaults = True
if (enable_user_input == False) or (set_defaults == True):
    replays = def_replays



for k_configuration in range(0, k):

    player1_wincount = 0
    player2_wincount = 0

    chessboard = []
    tile_letter = []
    for i in range(0, x[k_configuration]):
        tile_letter.append(letter[i])
    tile_number = [j for j in range(1, 1 + y[k_configuration])]
    for i in tile_letter:
        for j in tile_number:
            chessboard.append([i,j])

    for k_chess_games in range(0, replays):

        pawn_bishop = random.choice(chessboard)
        pawn_rook = random.choice(chessboard)
        while pawn_bishop == pawn_rook:
            pawn_bishop = random.choice(chessboard)
            pawn_rook = random.choice(chessboard)


        if (pawn_rook[0] == pawn_bishop[0]) or (pawn_rook[1] == pawn_bishop[1]):
            player1_wincount += 1
        else:
            number_distance = abs(pawn_rook[1] - pawn_bishop[1])
            letter_counter = 0
            letter_rook = 0
            letter_bishop = 0
            for i in letter:
                letter_counter += 1
                if i == pawn_rook[0]:
                    letter_rook = letter_counter
                if i == pawn_bishop[0]:
                    letter_bishop = letter_counter
            if number_distance == abs(letter_rook - letter_bishop):
                player2_wincount += 1

    print("----------------------------------------")
    print(x[k_configuration], "x", y[k_configuration], " Chessboard - results from ", replays, " games:")
    print("The Rook Won:", player1_wincount, "times")
    print("The Bishop Won:", player2_wincount, "times")
    print("----------------------------------------")