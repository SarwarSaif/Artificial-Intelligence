"""
import header.py and all its functions
"""
import helper
from helper import *

def do_hill_climbing(tweak_function = swap_function):
    """
    Runs hill climmbing algorithm
    Keyword argument:
    tweak_function- the tweaking function you want to use- it can be swap_function(default) or shuffle_function
    returns solution state and its fitnes
    """
    #Initialization step
    current_fitness = None
    current = generate_random_permutation()
    current1 = generate_random_permutation1()
    iteration = 400 #number of iterations, you can change it

    while(iteration>=0):
        iteration -=1
        current_fitness = fitness_function(current,current1) #calculating fitness
        #print('current',current, current_fitness)
        if current_fitness == 28:
            break
        #Modification step
        #generates next step and calculates fitness
        neighbour = generate_next_state(current,tweak_function)
        neighbour1 = generate_next_state(current1,tweak_function)
        neighbour_fitness = fitness_function(neighbour,neighbour1)
        #print('neighbour',neighbour, neighbour_fitness)
        if current_fitness < neighbour_fitness:
            #print("assigning")
            current = neighbour
            current1 = neighbour1

    return current,current1,current_fitness

if __name__ == "__main__":

    random.seed()
    print("Solving 8 queen problem")
    
    #You can use shuffle_function instead of swap_function
    solution,solution1, fitness = (do_hill_climbing(swap_function))
    print("Solution using Hill Climbing")
    printBoard(solution,solution1)
    print("Fitness is ",fitness)
    
