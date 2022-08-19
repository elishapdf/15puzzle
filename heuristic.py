from pdb1_5 import db1_5
from pdb2_5 import db2_5
from pdb3_5 import db3_5

def lexicographic_index(p):
    """
    Return the lexicographic index of the permutation `p` among all
    permutations of its elements. `p` must be a sequence and all elements
    of `p` must be distinct.

    >>> lexicographic_index('dacb')
    19
    >>> from itertools import permutations
    >>> all(lexicographic_index(p) == i
    ...     for i, p in enumerate(permutations('abcde')))
    True
    """
    result = 0
    for j in range(len(p)):
        k = sum(1 for i in p[j + 1:] if i < p[j])
        result += k * factorial(len(p) - j - 1)
    return result

def manhattan(node):
    total_distance = 0
    for tile in node.state:
        if (tile != 0):
            tile_goal_column = (tile - 1) % 3
            tile_current_column = node.state.index(tile) % 3
            horizontal_distance = abs(tile_current_column - tile_goal_column)

            tile_goal_row = (tile - 1) // 3
            tile_current_row = node.state.index(tile) // 3
            vertical_distance = abs(tile_current_row - tile_goal_row)

            total_distance += horizontal_distance + vertical_distance
    return total_distance

def pdb_disjoint(node):
    # state_string = [str(int) for int in node.state]
    # key = ','.join(state_string)
    # # print(key)
    # h = db.get(key)
    # if h is not None:
    #     return h
    # else:
    #     raise Exception("Not in PDB")
    p_state1 = []
    p_state2 = []
    p_state3 = []
    # state = [6,5,3,2,1,7,8,11,12,10,9,13,14,15,4,0]
    for k in range(1, 6):
        p_state1.append(node.state.index(k))
    for k in range(6, 11):
        p_state2.append(node.state.index(k))
    for k in range(11, 16):
        p_state3.append(node.state.index(k))

    state_string1 = [str(int) for int in p_state1]
    key1 = ','.join(state_string1)
    state_string2 = [str(int) for int in p_state2]
    key2 = ','.join(state_string2)
    state_string3 = [str(int) for int in p_state3]
    key3 = ','.join(state_string3)


    h1 = db1_5.get(key1)
    h2 = db2_5.get(key2)
    h3 = db3_5.get(key3)

    if h1 is None:
        raise Exception("h1 not found in pdb/db1_5")
    if h2 is None:
        raise Exception("h2 not found in pdb/db2_5")
    if h3 is None:
        raise Exception("h3 not found in pdb/db3_5")
    print("H: ", h1+h2+h3)
    return h1 + h2 + h3


def misplacedTiles(puzzle):
    goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', ' ']]
    
    misplace = 0
    for x in range(3):
        for y in range(3):
            # make sure we don't check blank
            if (puzzle[x][y] != ' '):
                # if it's not at it's proper place, it's misplaced
                if (puzzle[x][y] != goal[x][y]):
                    misplace += 1

    return misplace