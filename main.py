from os import stat
import time
from heuristic import manhattan, pdb_disjoint
from tools import puzzleTools, FifteenPuzzle, Records
from search import astar_search
# from pdb663 import generatePDB, convert_to_py, lexicographic_followers
# from math import factorial

def check_solvability(state):
        """ Checks if the given state is solvable """

        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1

        return inversion % 2 == 0

# def lexicographic_index(p):
#     """
#     Return the lexicographic index of the permutation `p` among all
#     permutations of its elements. `p` must be a sequence and all elements
#     of `p` must be distinct.

#     >>> lexicographic_index('dacb')
#     19
#     >>> from itertools import permutations
#     >>> all(lexicographic_index(p) == i
#     ...     for i, p in enumerate(permutations('abcde')))
#     True
#     """
#     result = 0
#     for j in range(len(p)):
#         k = sum(1 for i in p[j + 1:] if i < p[j])
#         result += k * factorial(len(p) - j - 1)
#     return result

# def lexicographic_followers(p):
#     """
#     Return the number of permutations of `p` that are greater than `p`
#     in lexicographic order. `p` must be a sequence and all elements
#     of `p` must be distinct.
#     """
#     return factorial(len(p)) - lexicographic_index(p) - 1

if __name__ == "__main__": 
    # generatePDB()
    # convert_to_py("15_5_puzzleDatabase.txt", "pdb1_5.py")

    # p = [0,1,2,3,4,5,6,7,8]
    # p.reverse()
    # print(p)
    # print(lexicographic_index(p))
    # print(lexicographic_followers(p))

    set1 = set(line.strip() for line in open('15pdb_test.txt'))
    set2 = set(line.strip() for line in open('15pdb.txt'))
    # print(len(set1))
    # print(len(set2))

    intersec = set1.intersection(set2)
    sym_diff = set1.symmetric_difference(set2)    
    print("# of entries in intersection of sets: ", len(intersec))
    print("# of entries in symmetric_difference of sets: ", len(sym_diff))

    # print("first 25 in sym_diff: ")
    # for k in range(25):
    #     x = next(iter(sym_diff))
    #     print(x)
    #     sym_diff.remove(x)


    # pdb_test = []
    # manhattan_test = []
    
    # # Starting a timer for the whole run
    # # total_start = time.time()
    
    # # Collecting the test cases from the test folder and checcking for solveability. 
    # # The puzzle object contains a list of solveable states
    # # states = puzzleTools(open('tests/8_puzzle_tests.txt').readlines(), importFromFile=True).clean_test_cases()
    
    # state = (3,6,5,2,1,7,8,11,12,10,9,13,14,15,4,0)
    # # state = (1, 2, 4, 8, 6, 7, 3, 0, 5, 10, 11, 12, 9, 13, 14, 15)
    # if not check_solvability(state):
    #     raise Exception('stupid - not solvable')
    # else:
    #     print('solvable')
        
    # # Testing every state in the list
    # # for state in states:
    # puzzle = FifteenPuzzle(state)

    # # PDB TEST        
    # start_time = time.time()
    # sol = astar_search(puzzle, pdb_disjoint, True).solution()
    # elapsed_time = time.time() - start_time
    # pdb_test.append([state, sol, len(sol), elapsed_time])
        
        # MANHATTAN TEST
        # start_time = time.time()
        # sol = astar_search(puzzle, manhattan, True).solution()
        # elapsed_time = time.time() - start_time
        # manhattan_test.append([state, sol, len(sol), elapsed_time])

    # Save results to csv file
    # Records('PDB_test_results', pdb_test).save()
    # Records('manhattan_test_results', manhattan_test).save()