"""
Header files for random number generation, math operations and permutation generation
"""
import random
from itertools import permutations
import numpy
import matplotlib.pylab as plt


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
    # generating a random index in [0,len(list)-1]
    idx = random.randint(0,len(permList))
    #concataneting all the characters of new permutation     
    random_combination = ''.join(permList[idx])
     
    return random_combination
	
def generate_random_permutation1(combination1 = 'qqrqrqqr'):
    """Generates a random permutation of given combination string.
    Keyword arguments:
    combination -- the input string to be permuted(default "12345678")
    returns a random permutation
    """
      
    # Get all permutations of string combination
    perms1 = permutations(combination1)
    # Making the list of all permutations
    permList1 = list(perms1)
    # generating a random index in [0,len(list)-1]
    idx1 = random.randint(0,len(permList1))
    #concataneting all the characters of new permutation     
    random_combination1 = ''.join(permList1[idx1])
	#ran = list(random_combination1)
     
    return random_combination1

string = generate_random_permutation1()
def printBoard1(combination):
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
    
def printBoard(combination,combination1):
    """Prints the chessboard.

    Keyword arguments:
    combination -- a string denoting which row contains queens in which column
    
    """
    #board to be print, dimension 8X8
    board_array = []
    graph_board_array = []
    c_i=3
    #Filling the board with *
    for i in range(0,8):
        board_array.append([])
        graph_board_array.append([])
        for j in range(0,8):
            board_array[i].append("*")
            c_i= c_i+.1
            graph_board_array[i].append(c_i)
    #Placing queens in the board based on input combination
	
    for i in range(len(combination)):
        board_array[i][int(combination[i])-1] = combination1[i]
        if (combination1[i]=='q') :
            graph_board_array[i][int(combination[i])-1] = float (0)
        elif (combination1[i]=='r') :
            graph_board_array[i][int(combination[i])-1] = float (2)
        
            
    for i in range(0,8):
        print(board_array[i])

    
          
    matrix = numpy.matrix(graph_board_array)
    #print(matrix)
    #m = [[0.0, 1.47, 2.43, 3.44, 1.08, 2.83, 1.08, 2.13, 2.11, 3.7], [1.47, 0.0, 1.5,     2.39, 2.11, 2.4, 2.11, 1.1, 1.1, 3.21], [2.43, 1.5, 0.0, 1.22, 2.69, 1.33, 3.39, 2.15, 2.12, 1.87], [3.44, 2.39, 1.22, 0.0, 3.45, 2.22, 4.34, 2.54, 3.04, 2.28], [1.08, 2.11, 2.69, 3.45, 0.0, 3.13, 1.76, 2.46, 3.02, 3.85], [2.83, 2.4, 1.33, 2.22, 3.13, 0.0, 3.83, 3.32, 2.73, 0.95], [1.08, 2.11, 3.39, 4.34, 1.76, 3.83, 0.0, 2.47, 2.44, 4.74], [2.13, 1.1, 2.15, 2.54, 2.46, 3.32, 2.47, 0.0, 1.78, 4.01], [2.11, 1.1, 2.12, 3.04, 3.02, 2.73, 2.44, 1.78, 0.0, 3.57], [3.7, 3.21, 1.87, 2.28, 3.85, 0.95, 4.74, 4.01, 3.57, 0.0]]
    #matrix = numpy.matrix(m)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_aspect('equal')
    plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.ocean)
    #plt.colorbar()
    plt.show() 

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

    list_combination = list(combination)
    #Shuffling in [i,j] interval
    shuffle_list = list_combination[i:j+1]
    random.shuffle(shuffle_list)
    list_combination[i:j+1] = shuffle_list
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

def generate_next_state1(combination1, tweak_function = swap_function):
    """generates next random state of a given state
    Keyword arguments:
    combination- input state
    tweak_function- the tweaking function you want to use- it can be swap_function(default) or shuffle_function
    returns a new generated state 
    """
    return tweak_function(combination1)

def fitness_function(combination,combination1):
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
	 
        
        
    		
    for i in range(0,7):
        for j in range(i+1,8):
            
            if ( combination1[i] == 'q' and combination1[i] == 'q') :
                if abs(i-j) == abs( int(combination[i])- int(combination[j])):
                    fitness -= 1 #one attacking pair found	
           
                    
            elif ( combination1[i] == 'r' and combination1[i] == 'q') :
                if abs(i-j) == abs( int(combination[i])- int(combination[j])):
                    fitness -= 1 #one attacking pair found	
            
    """             
            elif ( combination1[i] == 'r' and combination1[i] == 'r') :
                if abs(i-j) == abs( int(combination[i])- int(combination[j])):
                    fitness += 1 #one attacking pair found	
    """       
            
    return fitness

