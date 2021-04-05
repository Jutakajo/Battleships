from battleships import *
import sys

# Visualization as a global variable
viz = '  0 1 2 3 4 5 6 7 8 9\n0 . . . . . . . . . .\n1 . . . . . . . . . .\n2 . . . . . . . . . .\n'\
          '3 . . . . . . . . . .\n4 . . . . . . . . . .\n5 . . . . . . . . . .\n6 . . . . . . . . . .\n'\
          '7 . . . . . . . . . .\n8 . . . . . . . . . .\n9 . . . . . . . . . .\n'

def missed(row, column):
    '''If player's hit misses the ship this function changes visualisation with *'''
    global viz
    index = 21 * (row + 1) + row + 3 + (column * 2)
    viz = viz[:index] + '*' + viz[index + 1:]
    return viz


def shot(row, column):
    '''If player's hit shots the ship but does not sink this function changes visualisation with X'''
    global viz
    index = 21 * (row + 1) + row + 3 + (column * 2)
    viz = viz[:index] + 'X' + viz[index + 1:]
    return viz


def sank(ship_hit, ship_hit_type):
    '''If player's hit sinks the ship this function changes all ship cells with the first capital letter
    of the sunk ship'''
    global viz
    hits = ship_hit[4]
    letter = ship_hit_type[0].upper()
    for val in hits:
        row, column = val
        index = 21 * (row + 1) + row + 3 + (column * 2)
        viz = viz[:index] + letter + viz[index + 1:]
    return viz

def main():

    current_fleet = randomly_place_all_ships()

    all_hits = []

    game_over = False

    print(viz)

    while not game_over:

        try:

            loc_str = input("Enter row and column to shoot (separated by space) or 'q' to quit: ").split()

            # ends the game if user enters q
            if loc_str[0].lower() == 'q':
                print('Good Bye')
                sys.exit()

            # checks that user entered only 2 values separated by a space
            if len(loc_str) != 2:
                print("Woups, wrong input!")
                raise Exception

            # checks that user enters single digits
            if len(loc_str[0]) != 1 or len(loc_str[1]) != 1:
                print("Woups, wrong input!")
                raise Exception

            # checks that user enters positive integer numbers
            if loc_str[0].isnumeric() == False or loc_str[1].isnumeric() == False:
                print("Woups, wrong input!")
                raise Exception

                # checks if the user already hit same spot, adds it to the number of hits eitherway
            if loc_str in all_hits:
                print('You missed!')
                all_hits.append(loc_str)
                raise Exception


        except Exception:
            continue

        all_hits.append(loc_str)
        current_row = int(loc_str[0])
        current_column = int(loc_str[1])

        if check_if_hits(current_row, current_column, current_fleet):
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                ship_hit_type = ship_type(ship_hit)
                print(sank(ship_hit, ship_hit_type))
                print("You sank a " + ship_hit_type + "!")
            else:
                print(shot(current_row, current_column))
                print("You have a hit!")

        else:
            print(missed(current_row, current_column))
            print("You missed!")

        if not are_unsunk_ships_left(current_fleet):
            game_over = True
            print("Game over! You required", len(all_hits), "shots.")

if __name__ == '__main__':
    main()