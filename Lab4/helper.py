"""
Header files for random number generation, math operations and permutation generation
"""
import random
import math
from itertools import permutations




def generate_random_permutation(combination = '12345678'):
    """Generates a random permutation of given combination string.
    Keyword arguments:
    combination -- the input string to be permuted(default "12345678")
    returns a random permutation
    """
      
    # Get all permutations of string combination
    perms = permutations(combination)
    # Making the list of all permutations
    permList = list(perms)
    #print(permList)
    # generating a random index in [0,len(list)-1]
    idx = random.randint(0,len(permList))
    #concataneting all the characters of new permutation     
    random_combination = ''.join(permList[idx])
    #print(random_combination)
     
    return random_combination

    
def printBoard(combination):
    """Prints the chessboard.

    Keyword arguments:
    combination -- a string denoting which row contains queens in which column
    
    """
    #board to be print, dimension 8X8
    board_array = []
    #Filling the board with *
    for i in range(0,8):
        board_array.append([])
        for j in range(0,8):
            board_array[i].append("*")
    #Placing queens in the board based on input combination
    for i in range(len(combination)):
        board_array[i][int(combination[i])-1] = "Q" 
    for i in range(0,8):
        print(board_array[i])

def shuffle_function(combination_main):
    """Shuffle a combination string.

    Keyword arguments:
    combination_main -- input combination string
    
    """
    #Making temporary string
    combination = combination_main [:]
    #Generating random start and endpoints for shuffling
    i = random.randint(0,len(combination)-2)
    j = random.randint(i+1,len(combination)-1)
    #print(i)
    #print(j)
    list_combination = list(combination)
    #print(list_combination)
    #Shuffling in [i,j] interval
    shuffle_list = list_combination[i:j+1]
    #print(shuffle_list)
    random.shuffle(shuffle_list)
    list_combination[i:j+1] = shuffle_list
    #print(list_combination)
    combination = ''.join(list_combination)
    return combination

def swap_function(combination_main):
    """Shuffle a combination string.

    Keyword arguments:
    combination_main -- input combination string
    
    """

    combination = combination_main [:]
    #Generating random start and endpoints for shuffling
    i = random.randint(0,len(combination)-2)
    j = random.randint(i,len(combination)-1)
    #Swapping in [i,j] interval
    list_combination = list(combination)
    list_combination[i],list_combination[j] = list_combination[j],list_combination[i]
    combination = ''.join(list_combination)
    return combination

def generate_next_state(combination, tweak_function = swap_function):
    """generates next random state of a given state
    Keyword arguments:
    combination- input state
    tweak_function- the tweaking function you want to use- it can be swap_function(default) or shuffle_function
    returns a new generated state 
    """
    return tweak_function(combination)

def fitness_function(combination):
    """calculates the fitness of a given state, i.e.- number of non-attacking queen pairs
    Keyword arguments:
    combination- input state
    
    returns the fitness/ number of non-attacking pairs in this case 
    """
    fitness = 28 #non-attacking pairs

    for i in range(0,7):
        for j in range(i+1,8):

            if abs(i-j) == abs( int(combination[i])- int(combination[j])):
                fitness -= 1 #one attacking pair found
                """ print(fitness)
                print(abs(i-j))
                print(int(combination[i]))
                print(int(combination[j]))
                print(abs( int(combination[i])- int(combination[j])))
                """
    
    for i in range(0,7):
        for j in range(i+2,8):

            if abs(i-j-1) == abs( int(combination[i])- int(combination[j])):
                fitness -= 1 #one attacking pair found
            elif abs(i-j+1) == abs( int(combination[i])- int(combination[j])):
                fitness -= 1 #one attacking pair found
    
    return fitness

