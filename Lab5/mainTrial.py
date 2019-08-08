# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 00:01:46 2018

@author: majaa
"""

import random
import math
from itertools import permutations



k_value_for_selection = 5
default_gene_size = 8
default_iteration = 100
default_population_size = 5
default_crossover_rate = 0.5
default_mutation_rate = 0.05
default_bit_generation_probability = [0.5]*default_gene_size


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

def dummy_fitness_function(gene):
    """
    calculates the fitness of a binary bitstring gene. Fitness function is equal to the standard deviation of the collection of 1s and 0s in the bitstring
    parameters:
    gene- binary bitstring Gene 
    
    
    """

    fitness = 28 #non-attacking pairs
    
    for i in range(0,7):
        for j in range(i+1,8):
            
                if abs(i-j) == abs( int(gene[i])- int(gene[j])):
                    fitness -= 1 #one attacking pair found
	 
    
    
    
        
    """		
    for i in range(0,7):
        for j in range(i+1,8):
            
            if ( combination1[i] == 'q' and combination1[i] == 'q') :
                if abs(i-j) == abs( int(combination[i])- int(combination[j])):
                    fitness -= 1 #one attacking pair found	
           
                    
            elif ( combination1[i] == 'r' and combination1[i] == 'q') :
                if abs(i-j) == abs( int(combination[i])- int(combination[j])):
                    fitness -= 1 #one attacking pair found	
            
                
            elif ( combination1[i] == 'r' and combination1[i] == 'r') :
                if abs(i-j) == abs( int(combination[i])- int(combination[j])):
                    fitness += 1 #one attacking pair found	
    """       
            
    return fitness



"""
Next three functions are helper functions for selection function do_stochastic_universal_sampling
"""

def makeWheel(population,fitness):
    """
    returns a list which will work as the "roulette wheel" in stochastic universal sampling. Each element contains the start and end of the fitness-probability interval and the individual associated with it  
    parameters: 
    population- list of binary bitstrings 
    fitness- fitness function passed as parameters (you can use dummy_fitness_function or another_dummy_fitness_function as arguments)

    after calculating fitness of each individuals, we have used exponentials to normalize them, so that the derived quantities sum to 1.0, and represent a probability distribution.
    """
    #print("Yeah! im in")
    wheel = []
    exp_population = [ (p, math.exp(fitness(p))) for p in population ]
    total = sum(exp_p for (p,exp_p) in exp_population)
    top = 0
    for (p,exp_p) in exp_population:
        
        f = exp_p/total
        wheel.append((top, top+f, p))
        top += f
    #print(wheel)
    return wheel

def binSearch(wheel, num):
    """
    returns the desired gene with maximum probabilty not exceeding num from "roulette wheel" using binary search
    parameters:
    wheel- wheel built in makeWheel function
    num-  random probability point to be found in the wheel
    """
    #print("calling",wheel,num)
    mid = (len(wheel))//2
    #print(mid)
    low, high, answer = wheel[mid]
    if mid == 0:
        return answer
    if low<=num and num<=high:
        return answer
    elif low > num:
        return binSearch(wheel[:mid], num)
    else:
        return binSearch(wheel[mid:], num)

def select(wheel, N):
    """
    returns a list of N selected genes from a "roulette wheel"
    parameters: 
    wheel - same as stated in previous functions
    N - number of genes to be selected 
    """

    stepSize = 1.0
    answer = []
    r = random.random()
    answer.append(binSearch(wheel, r))
    while len(answer) < 1:
        r += stepSize
        if r>1:
            r %= 1
        answer.append(binSearch(wheel, r))
        
    #print(answer)
    return answer

"""
SELECTION TECHNIQUES
"""

def do_roulette_wheel_sampling(gene_list,fitness_func,selected_no):
    """
    returns a list of selected individuals based on stochstic universal sampling selection technique
    parameters:
    gene_list: candidate individuals
    fitness_func: fitness function used for selection
    selected_no: number of parents to be selected in this process
    """
    for i in range(len(gene_list)):
        gene_list[i]=generate_random_permutation()
    wheel = makeWheel(gene_list,fitness_func)
    #print(wheel)
    
    return select(wheel,selected_no)



"""
CROSSOVER TECHNIQUES
"""

def do_one_point_crossover(gene_a_s,gene_b_s,crossover_rate):

    """
    applies one point crossover between two genes with a  probability
    parameters:
    gene_a_s, gene_b_s: two parent gene strings
    crossover_rate: probability of crossover 
    """
    gene_a = [c for c in gene_a_s]
    gene_b = [c for c in gene_b_s]
    
    p = random.random()
    if p <= crossover_rate:

      point_index = random.randint(0,len(gene_a)-2)

      gene_a[point_index:-1],gene_b[point_index:-1] = gene_b[point_index:-1],gene_a[point_index:-1]       
    
    
  
    return ["".join(gene_a),"".join(gene_b)]
    
    
def do_partially_matched_crossover(gene_a_s,gene_b_s,crossover_rate):

    """
    applies uniform crossover between two genes with a probability
    parameters:
    gene_a_s, gene_b_s: two parent gene strings
    crossover_rate: probability of crossover 
    """
    
    gene_a = [c for c in gene_a_s]
    gene_b = [c for c in gene_b_s]
    
    #print(gene_a)
    #print(gene_b)
    for i in range(len(gene_a)):
        
        p = random.random()
        if p <= crossover_rate:
            gene_a[i], gene_b[i] = gene_b[i], gene_a[i] 

    #print(gene_a)
    #print(gene_b)
    return ["".join(gene_a),"".join(gene_b)]

"""
MUTATION TECHNIQUES
"""

def do_bit_flip_mutation(gene_s,mutation_rate):
    
    """
    applies bit flip mutation on a gene with a probability
    parameters:
    gene_s: child gene string
    mutation_rate: probability of mutation 
    """
  
    gene = [c for c in gene_s]
    
    for i in range(len(gene)):
        
        p = random.random()
        
        #print(" at ",i)
        if p <= mutation_rate:
            
            #print("yes at ",i)
            gene[i] = str( 1- int(gene[i]))
            
    return "".join(gene)

def do_swap_mutation(gene_s,mutation_rate):
    

    """
    applies inversion mutation on a gene with a probability
    parameters:
    gene_s: child gene string
    mutation_rate: probability of mutation 
    """
    
    gene = [c for c in gene_s]
    """
    p = random.random()
    if p<= mutation_rate:


      start = random.randint(0,len(gene_s)-2)
      end = random.randint(start+1,len(gene_s)-1)

      temp = gene[start:end+1]
      temp.reverse()
      gene[start:end+1] = temp
      
      
    return "".join(gene)
    """
    combination = gene [:]
    #Generating random start and endpoints for shuffling
    i = random.randint(0,len(combination)-2)
    j = random.randint(i,len(combination)-1)
    #Swapping in [i,j] interval
    list_combination = list(combination)
    list_combination[i],list_combination[j] = list_combination[j],list_combination[i]
    combination = ''.join(list_combination)
    return combination

def do_scramble_mutation(gene_s,mutation_rate):
    

    
    
    gene = [c for c in gene_s]
    
    random.shuffle(gene)
    return gene


"""
Object oriented implementation of Genetic Algorithm
"""                                
class GeneticAlgorithm:

    """
    Class for genetic algorithm
    fitness, selection, crossover and mutation functions can be passed as constructor arguments.
    If any of them is not passed, default value is passed.
    """    
    
    def __init__(self,
                 fitness_func = dummy_fitness_function,
                 selection_func = do_roulette_wheel_sampling,
                 crossover_func = do_partially_matched_crossover,
                 mutation_func = do_swap_mutation
                 ):
        
        """
        size of genes, number of iterations, size of populations, crossover and mutation rate, probability 
        of generating 1 in an index of bit string are set to default values stated in the beginning of the code.
        You can tweak them.
        """
        self.gene_size = default_gene_size
        self.iteration = default_iteration
        self.population_size = default_population_size
        self.crossover_rate = default_crossover_rate
        self.mutation_rate = default_mutation_rate
        self.bit_generation_probability = default_bit_generation_probability
        self.fitness_function = fitness_func
        self.selection_function = selection_func
        self.crossover_function = crossover_func
        self.mutation_function = mutation_func
        
    def generate_population(self):
        
        """
        returns an initial population for GA
        """
        
        population = []
        
        for i in range(self.population_size):
            
            gene = generate_random_permutation()
            """f=0
            for j in range(self.gene_size):
                prob=random.random()
                
                if prob <= self.bit_generation_probability[j]:
                    gene += "1"
                else:
                    gene += "0"
            """
            #print(gene)
            population.append(gene)
        #print(population)    
        return population
    
    
    def run_GA(self):
        
        """
        Basic Genetic Algorithm implementation based on pseudocode
        """
        
        population = self.generate_population()
        best = (None,None)
        
        for i in range(self.iteration):
            
            for gene in population:
                fitness = self.fitness_function(gene)
                #print(gene,fitness)
                if best[0] == None or best[1] < fitness:
                    best = (gene,fitness)
            Q = []
            
            for j in range(self.population_size//2):
                
                
                selected_parents=do_roulette_wheel_sampling(population,
                                                         dummy_fitness_function,
                                                         1)
                parent_a = selected_parents[0]#population[j*2]
                
                
                
                selected_parents=do_roulette_wheel_sampling(population,
                                                         dummy_fitness_function,
                                                         1)
                parent_b = selected_parents[0]#population[j*2+1]
                #print("selected ",parent_a,parent_b)
                #print(parent_a)
                #print(parent_b)
                new_genes = do_partially_matched_crossover(parent_a, parent_b, 
                             
                                                    self.crossover_rate)
                
                #print(new_genes)
                new_genes = [self.mutation_function(new_genes[0],
                                                    self.mutation_rate),
                             self.mutation_function(new_genes[1],
                                                    self.mutation_rate)]
                             
                Q += new_genes
            
            #print(Q)
            population = Q
            for gene in population:
                fitness = self.fitness_function(gene)
                #print(gene,fitness)
                if best[0] == None or best[1] < fitness:
                    best = (gene,fitness)
            
        return best
            

        
if __name__=="__main__":
    
                    
    
    GA_instance=GeneticAlgorithm(selection_func=do_roulette_wheel_sampling, 
    fitness_func = dummy_fitness_function,
    crossover_func = do_partially_matched_crossover,
    mutation_func = do_swap_mutation)
    
    best_solution = GA_instance.run_GA()
    best_solution[1]=dummy_fitness_function(best_solution[1].tolist)
    #solution1=helper.generate_random_permutation1()
    print("Best solution is: ",best_solution)
    #helper.printBoard1(best_solution)
    """
    board_array = []
    
    #Filling the board with *
    for i in range(0,8):
        board_array.append([])
        for j in range(0,8):
            board_array[i].append("*")
    #Placing queens in the board based on input combination
    for i in range(len(best_solution)):
        board_array[i][int(best_solution[i])] = "Q" 
    for i in range(0,8):
        print(board_array[i])
    """
    """
    Testing codes for inversion mutation and one point crossover, You can test other crossover and mutation functions too.
    """
    #print(do_swap_mutation("101110001",0.3))
    #print(do_one_point_crossover("10110","01010",0.8))
    