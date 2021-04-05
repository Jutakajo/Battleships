import pytest
from battleships import *

def test_is_sunk1():
    s = (2, 3, False, 3, {(2, 3), (3, 3), (4, 3)})
    assert is_sunk(s) == True

def test_is_sunk2():
    s = (9, 0, False or True, 1, {(9, 0)})
    assert is_sunk(s)==True

def test_is_sunk3():
    s = (5, 2, True, 4, {(5,2), (5,4), (5,5)})
    assert is_sunk(s) == False

def test_is_sunk4():
    s = (1, 8, True, 2, {(1, 8),(1, 9)})
    assert is_sunk(s) == True

def test_is_sunk5():
    s = (6, 5, True, 1, set())
    assert is_sunk(s) == False


def test_ship_type1():
    #test if cruiser
    s = (2, 3, False, 3, set())
    assert ship_type(s) == 'cruiser'

def test_ship_type2():
    #test if submarine hotizontal
    s = (9, 0, True, 1, {(9, 0)})
    assert ship_type(s) == 'submarine'

def test_ship_type3():
    #test if battleship
    s = (5, 2, True, 4, set())
    assert ship_type(s) == 'battleship'

def test_ship_type4():
    s = (1, 8, True, 2, set())
    #test if destroyer
    assert ship_type(s) == 'destroyer'

def test_ship_type5():
    s = (9, 0, False, 1, set())
    #test if submarine vertical
    assert ship_type(s) == 'submarine'

#adding global variables to run tests on

ship1 = (5, 2, True, 4, set())
ship2 = (1, 6, True, 2, set())
ship3 = (9, 9, True,1, set())
fleet = [ship1, ship2, ship3]

def test_is_open_sea1():
    #adjacent diagonally, first ship in fleet
    assert is_open_sea(6, 6, fleet) == False


def test_is_open_sea2():
    #adjacent diagonally, last ship in fleet
    assert is_open_sea(8, 8, fleet) == False


def test_is_open_sea3():
    #adjacent horizontally, middle ship in fleet
    assert is_open_sea(2, 6, fleet) == False

def test_is_open_sea4():
    #on a cell already occupied by a ship
    assert is_open_sea(5, 2, fleet) == False

def test_is_open_sea5():
    #valid to place cell
    assert is_open_sea(9, 7, fleet) == True

ship4 = (7, 4, False, 3, set())
ship5 = (9, 6, True, 2, set())
ship6 = (0, 0, False, 2, set())
ship7 = (0, 2, False, 4, set())
fleet1 = [ship4, ship5, ship6, ship7]


def test_ok_to_place_ship_at1():
    #horizontally adjacent to ship 5
    assert ok_to_place_ship_at(7, 8, False, 2, fleet1) == False

def test_ok_to_place_ship_at2():
    #horizontally adjacent to last ship in fleet
    assert ok_to_place_ship_at(4, 0, True, 2, fleet1) == False

def test_ok_to_place_ship_at3():
    #same place as ship6 in fleet
    assert ok_to_place_ship_at(0, 0, True, 2, fleet1) == False

def test_ok_to_place_ship_at4():
    #vertically adjacent to the first ship in fleet
    assert ok_to_place_ship_at(7, 2, True, 2, fleet1) == False

def test_ok_to_place_ship_at5():
    #legal to place ship
    assert ok_to_place_ship_at(3, 0, True, 1, fleet1) == True


def test_place_ship_at1():
    actual = place_ship_at(2, 5, True, 3, fleet1)
    actual.sort()
    expected = [ship4, ship5, ship6, ship7, (2, 5, True, 3, set())]
    expected.sort()
    assert expected == actual

def test_place_ship_at2():
    #checks that not adding ship to the fleet is not legal
    actual = place_ship_at(2, 5, True, 3, fleet1)
    actual.sort()
    expected = [ship4, ship5, ship6, ship7]
    expected.sort()
    assert expected != actual

def test_place_ship_at3():
    actual = place_ship_at(9, 9, True, 1, fleet1)
    actual.sort()
    expected = [ship4, ship5, ship6, ship7, (9, 9, True, 1, set()), (2, 5, True, 3, set()), (2, 5, True, 3, set())]
    expected.sort()
    assert expected == actual

def test_place_ship_at4():
    actual = place_ship_at(2, 7, True, 2, fleet1)
    actual.sort()
    expected = [ship4, ship5, ship6, ship7, (2, 5, True, 3, set()),(2, 5, True, 3, set()), (9, 9, True, 1, set()),
                (2, 7, True, 2, set())]
    expected.sort()
    assert expected == actual

def test_place_ship_at5():
    actual = place_ship_at(7, 6, True, 4, fleet1)
    actual.sort()
    expected = [ship4, ship5, ship6, ship7, (2, 5, True, 3, set()),(2, 5, True, 3, set()), (9, 9, True, 1, set()),
                (2, 7, True, 2, set()), (7, 6, True, 4, set())]
    expected.sort()
    assert expected == actual


fleet2 = [(7, 4, False, 3, {(7, 4), (9, 4)}), (9, 6, True, 2, set()), (0, 0, False, 2, {(0, 0)}), (0, 2, False, 4, set()),
(5, 2, True, 3, set()), (5, 0, False, 2, {(6, 0)}), (3, 6, True, 1, set()), (8, 9, True, 1, set()),
(1, 6, False, 1, set()), (9, 0, True, 1, set())]

def test_check_if_hits1():
    #hits already hit cell for 1st ship in the fleet
    assert check_if_hits(9, 4, fleet2) == True

def test_check_if_hits2():
    #hits last ship in the fleet
    assert check_if_hits(9, 0, fleet2) == True

def test_check_if_hits3():
    #hits the last cell of the ship in fleet
    assert check_if_hits(3, 2, fleet2) == True

def test_check_if_hits4():
    #hits diagonally adjacent cell for a ship in fleet
    assert check_if_hits(4, 7, fleet2) == False

def test_check_if_hits5():
    #hits vertically adjacent cell for a ship in fleet
    assert check_if_hits(0, 6, fleet2) == False



def test_hit1():
    #first cell of the ship
    (actual, s) = hit(5, 0, fleet2)
    actual.sort()
    expected = [(7, 4, False, 3, {(7, 4), (9, 4)}), (9, 6, True, 2, set()), (0, 0, False, 2, {(0, 0)}),
                (0, 2, False, 4, set()), (5, 2, True, 3, set()), (5, 0, False, 2, {(5, 0), (6, 0)}),
                (3, 6, True, 1, set()), (8, 9, True, 1, set()),
                (1, 6, False, 1, set()), (9, 0, True, 1, set())]
    expected.sort()
    assert (actual, s) == (expected, (5, 0, False, 2, {(5, 0), (6, 0)}))


def test_hit2():
    #last ship in fleet
    (actual, s) = hit(9, 0, fleet2)
    actual.sort()
    expected = [(7, 4, False, 3, {(7, 4), (9, 4)}), (9, 6, True, 2, set()), (0, 0, False, 2, {(0, 0)}),
                (0, 2, False, 4, set()),
                (5, 2, True, 3, set()), (5, 0, False, 2, {(6, 0), (5, 0)}), (3, 6, True, 1, set()),
                (8, 9, True, 1, set()),
                (1, 6, False, 1, set()), (9, 0, True, 1, {(9, 0)})]
    expected.sort()
    assert (actual, s) == (expected, (9, 0, True, 1, {(9, 0)}))

def test_hit3():
    #last cell of the ship
    (actual, s) = hit(3, 2, fleet2)
    actual.sort()
    expected = [(7, 4, False, 3, {(7, 4), (9, 4)}), (9, 6, True, 2, set()), (0, 0, False, 2, {(0, 0)}),
                (0, 2, False, 4, {(3, 2)}),
                (5, 2, True, 3, set()), (5, 0, False, 2, {(6, 0), (5, 0)}), (3, 6, True, 1, set()),
                (8, 9, True, 1, set()),
                (1, 6, False, 1, set()), (9, 0, True, 1, {(9, 0)})]
    expected.sort()
    assert (actual, s) == (expected, (0, 2, False, 4, {(3, 2)}))

def test_hit4():
    #hits the same cell twice
    (actual, s) = hit(3, 2, fleet2)
    actual.sort()
    expected = [(7, 4, False, 3, {(7, 4), (9, 4)}), (9, 6, True, 2, set()), (0, 0, False, 2, {(0, 0)}),
                (0, 2, False, 4, {(3, 2)}),
                (5, 2, True, 3, set()), (5, 0, False, 2, {(6, 0), (5, 0)}), (3, 6, True, 1, set()),
                (8, 9, True, 1, set()),
                (1, 6, False, 1, set()), (9, 0, True, 1, {(9, 0)})]
    expected.sort()
    assert (actual, s) == (expected, (0, 2, False, 4, {(3, 2)}))

def test_hit5():
    #middle cell of the ship
    (actual, s) = hit(5, 3, fleet2)
    actual.sort()
    expected = [(7, 4, False, 3, {(7, 4), (9, 4)}), (9, 6, True, 2, set()), (0, 0, False, 2, {(0, 0)}),
                (0, 2, False, 4, {(3, 2)}),
                (5, 2, True, 3, {(5, 3)}), (5, 0, False, 2, {(6, 0), (5, 0)}), (3, 6, True, 1, set()),
                (8, 9, True, 1, set()),
                (1, 6, False, 1, set()), (9, 0, True, 1, {(9, 0)})]
    expected.sort()
    assert (actual, s) == (expected, (5, 2, True, 3, {(5, 3)}))



def test_are_unsunk_ships_left1():
    #ships left, none hit
    assert are_unsunk_ships_left (fleet) == True

def test_are_unsunk_ships_left2():
    # ships left
    assert are_unsunk_ships_left (fleet1) == True

def test_are_unsunk_ships_left3():
    # ships left, some ships hit
    assert are_unsunk_ships_left (fleet2) == True

def test_are_unsunk_ships_left4():
    #all ships sank
    fleet3 = [(7, 4, False, 3, {(7, 4), (8, 4), (9, 4)}), (9, 6, True, 2, {(9, 6), (9, 7)}),
              (0, 0, False, 2, {(0, 0), (1, 0)}),
              (0, 2, False, 4, {(3, 2), (0, 2), (1, 2), (2, 2)}),
              (5, 2, True, 3, {(5, 3), (5, 2), (5, 4)}), (5, 0, False, 2, {(6, 0), (5, 0)}), (3, 6, True, 1, {(3, 6)}),
              (8, 9, True, 1, {(8, 9)}),
              (1, 6, False, 1, {(1, 6)}), (9, 0, True, 1, {(9, 0)})]
    assert are_unsunk_ships_left (fleet3) == False

def test_are_unsunk_ships_left5():
    #one ship left
    fleet4 = [(7, 4, False, 3, {(7, 4), (8, 4), (9, 4)}), (9, 6, True, 2, {(9, 6), (9, 7)}),
              (0, 0, False, 2, {(0, 0), (1, 0)}),
              (0, 2, False, 4, {(3, 2), (0, 2), (1, 2), (2, 2)}),
              (5, 2, True, 3, {(5, 3), (5, 2), (5, 4)}), (5, 0, False, 2, {(6, 0), (5, 0)}), (3, 6, True, 1, {(3, 6)}),
              (8, 9, True, 1, {(8, 9)}),
              (1, 6, False, 1, {(1, 6)}), (9, 0, True, 1, {})]
    assert are_unsunk_ships_left (fleet4) == True


#testing my own written function ship_hit()

ship8 = (6, 1, False, 3, set())
ship9 = (9, 6, True, 2, set())
ship10 = (7, 4, False, 3, set())
fleet5 = [ship8, ship9, ship10]
def test_ship_hit1():
    #hitting last ship in the fleet
    assert ship_hit(8, 4, fleet5) == 2

def test_ship_hit2():
    #hitting first ship in fleet
    assert ship_hit(7, 1, fleet5) == 0

def test_ship_hit3():
    #none of ships hit by the shot
    assert ship_hit(1, 2, fleet5) == False

