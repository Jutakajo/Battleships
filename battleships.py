#see the readme.md file for description and data 
import sys
import random
from extension import *

def is_sunk(ship):
    '''Checks if ship has been sunk already'''
    return len(ship[4]) == ship[3]



def ship_type(ship):
    '''Checks what type is the ship by its length'''
    if ship[3] ==1:
        return "submarine"
    elif ship[3] ==2:
        return "destroyer"
    elif ship[3] == 3:
        return "cruiser"
    elif ship[3] == 4:
        return "battleship"


def is_open_sea(row, column, fleet):
    '''Checks if the cell given is in a legal place to put a ship at in relationship to the existing fleet'''
    for ship in fleet:
        if ship[2] == True:  #if ship is horizontal
            # checks if a given cell occupies an illegal area
            if 0 <= abs(ship[0] - row) <= 1 and 0 <= abs(ship[1] - column) <= ship[3]:
                return False
        else:                 # if ship is vertical
            if 0 <= abs(ship[0] - row) <= ship[3] and 0 <= abs(ship[1] - column) <= 1:
                return False
    return True



def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    '''Checks if the new ship can be placed in the sea within an appropriate distance from the rest of the fleet'''
    if horizontal:
        for i in range(0,length):
            #checks each cell of a given horizontal ship
            column += i
            if not is_open_sea(row, column, fleet):
                return False
    else:  #same for vertical ships
        for j in range(0,length):
            row += j
            if not is_open_sea(row, column, fleet):
                return False
    return True


def place_ship_at(row, column, horizontal, length, fleet):
    '''Places a ship in an existing fleet'''
    fleet.append((row, column, horizontal, length, set()))
    return fleet



def randomly_place_all_ships():
    '''Randomly places 10 ships in the sea'''
    fleet = []
    index = 0
    all_ships = [4,3,3,2,2,2,1,1,1,1]
    # runs until all ships are placed
    while index < len(all_ships):
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        horizontal = bool(random.getrandbits(1))
        length = all_ships[index]
        # checks that generated ship does not go outside the borders
        if row + (length - 1) < 10 and column + (length - 1) < 10:
            # checks that generated ship is not adjacent to existing ships in fleet
            if ok_to_place_ship_at(row, column, horizontal, length, fleet):
                place_ship_at(row, column, horizontal, length, fleet)
                index += 1
    return fleet




def ship_hit(row, column, fleet):
    '''My function. Checks if ship is hit and returns its index if it is or False if not'''
    for i in range(len(fleet)):
        ship = fleet[i]
        if ship[2]: # for horizontal ships
            # checks if the cell provided hits any of the ship in fleet
            if ship[0] == row and ship[1] <= column < ship[1] + ship[3]:
                return i
        else:       # same for vertical ships
            if ship[1] == column and ship[0] <= row < ship[0] + ship[3]:
                return i
    return False

def check_if_hits(row, column, fleet):
    '''Tells if any of the ships in the fleet have been hit by the shot'''
    if ship_hit(row, column, fleet) is False:
        return False
    else:
        return True


def hit(row, column, fleet):
    '''Adds a successful shot to the set of tuples and returns resulting fleet and hit ship '''
    hit_ship_index = ship_hit(row, column, fleet)
    fleet[hit_ship_index][4].add((row, column))
    hit_ship = fleet[hit_ship_index]
    return fleet, hit_ship


def are_unsunk_ships_left(fleet):
    '''Checks if there are any more unsunk ships left in the fleet'''
    for ship in fleet:
        if not is_sunk(ship):
            return True
    return False



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
