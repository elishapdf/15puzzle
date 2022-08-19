import time as timer
from collections import deque
from math import factorial
from copy import deepcopy
import json
from heuristic import lexicographic_index

goal_state_1 = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]
goal_state_2 = [-1, -1, -1, -1, -1, 6, 7, 8, 9, 10, -1, -1, -1, -1, -1, 0]
goal_state_3 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 11, 12, 13, 14, 15, 0]

# possible moves of blank tile for 8-puzzle
# input: current state
# output: possible moves of blank tile from current state
def getPossible8Moves(state):
    pos = puzzle.index(0)

    if pos == 0:
        moves = [1, 3]
    elif pos == 1:
        moves = [1, 3, -1]
    elif pos == 2:
        moves = [3, -1]
    elif pos == 3:
        moves = [-3, 1, 3]
    elif pos == 4:
        moves = [-3, 1, 3, -1]
    elif pos == 5:
        moves = [-3, 3, -1]
    elif pos == 6:
        moves = [-3, 1]
    elif pos == 7:
        moves = [-3, 1, -1]
    else:
        moves = [-3, -1]

# possible moves of blank tile for 15-puzzle
# input: current state
# output: possible moves of blank tile from current state
def getMoves15(state):
    pos = state.index(0)

    if pos == 0:
        moves = [1, 4]
    elif pos == 1:
        moves = [1, 4, -1]
    elif pos == 2:
        moves = [4, -1,1]
    elif pos == 3:
        moves = [-1, 4]
    elif pos == 4:
        moves=[-4,4,1]
    elif pos == 7:
        moves = [-4, 4, -1]
    elif pos == 8:
        moves = [1,-4,4]
    elif pos ==11:
        moves = [-1,4,-4]
    elif pos ==12:
        moves = [-4,1]
    elif pos ==13:
        moves=[1,-1,-4]
    elif pos == 14:
        moves = [1,-1,-4]
    elif pos == 15: 
        moves = [-4,-1]
    else:
        moves = [-4, 1, 4, -1]

    return moves

# moves blank tile in N-puzzle
# input: current state, direction (R, L, U, D) of movement for blank tile
# output: blank tile swapped with tile occupying indicated location
def move(state, direction):
    new_state = deepcopy(state)
    pos = state.index(0)
    next_pos = pos + direction

    # swap blank position
    new_state[pos], new_state[next_pos] = new_state[next_pos], new_state[pos]

    return new_state

# convert text --> python file for PDB
def convert_to_py(filename, py_filename, db_name):
    data_set = []
    with open(filename, 'r') as file:
        for i in file:
            data_set.append(eval(i))
    
    with open(py_filename, 'w') as file:
        file.write(db_name + ' = {\n')
        for data in data_set:
            file.write('"' + str(data[0]) + '"' + ':' + str(data[1]) + ',\n')
        file.write('}')


# make another for 8 puzzle or edit this for any n-puzzle
def generatePDB(goal_state, filename):
    start_time = timer.time()
    start = goal_state
    queue = deque([[start, 0]])
    entries = {}
    visited = set()

    tile_set = []
    for t in range(len(goal_state)):
        if goal_state[t] > 0:
            tile_set.append(goal_state[t])

    print("Database generation started.....")
    # BFS from goal state to generate statespace from moving blank space/tile
    while queue:
        state_cost = queue.popleft()  # .popleft faster than .pop
        curr_state = state_cost[0]
        cost = state_cost[1]

        for direction in getMoves15(curr_state):
            # move blank tile
            next_state = move(curr_state, direction)
            pos = curr_state.index(0)

            # update cost if blank within tile set
            if next_state[pos] != -1:
                cost = cost + 1

            # find location of tiles in set
            tile_indices = []
            for k in tile_set:
                tile_indices.append(next_state.index(k))
            next_state_cost = [next_state, cost]

            # Create key
            entry = ",".join(str(t) for t in tile_indices)
            state_entry = ",".join(str(t) for t in next_state)
            print(state_entry)            

            if not state_entry in visited:
                queue.append(next_state_cost)
                visited.add(state_entry)
            if entry not in entries:
                entries[entry] = cost
            elif entries.get(entry) > cost: # update previous entry w/ lower cost
                new_entry = {entry:cost}
                entries.update(new_entry)

        if len(entries) % 1000 == 0: 
            print(len(entries))

        # Check if all entries are in the PDB
        if len(entries) >= factorial(len(goal_state))/factorial(len(goal_state) - len(tile_set)):
            print("All entries for PDB collected.....")
            break

    time_entry_collection = timer.time() - start_time
    with open(filename, "w") as f:
        for key, value in entries.items():
            json.dump((key, value), f)
            f.write("\n")    

    total_time = timer.time() - start_time
    print("Entries for PDB written to {}....".format(filename))
    print("Time to gather entries: {}".format(time_entry_collection))
    print("Total time: {}".format(total_time))


generatePDB(goal_state_1, "15pdb.txt")
convert_to_py("15pdb.txt", "15pdb.py", "15pdb_db")