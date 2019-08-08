# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 18:53:43 2017
@author: Naved
"""
import random
import math

k_value_for_selection = 5
default_gene_size = 8
default_iteration = 1000
default_population_size = 5
default_crossover_rate = 0.5
default_mutation_rate = 0.05
default_bit_generation_probability = [0.5]*default_gene_size

def dummy_fitness_function(gene):
    """
    calculates the fitness of a binary bitstring gene. Fitness function is equal to the standard deviation of the collection of 1s and 0s in the bitstring
    parameters:
    gene- binary bitstring Gene 
    """
    sum = 0

    for i in range(len(gene)):

        sum += int(gene[i])

    mean = sum/len(gene)

    sum_dev = 0.0

    for i in range(len(gene)):

        sum_dev += (float(int(gene[i]))-mean)**2.0
    sum_dev /= len(gene)
    
    sum_dev = sum_dev**0.5
    
    return len(gene)-sum_dev

def another_dummy_fitness_function(gene):
    """
    calculates the fitness of a binary bitstring gene. Fitness function is equal to the proportion of 1sin the bitstring
    parameters:
    gene- binary bitstring Gene
    """

    sum = 0

    for i in range(len(gene)):

        sum += int(gene[i])

    
    return sum/len(gene)

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

    stepSize = 1.0/N
    answer = []
    r = random.random()
    answer.append(binSearch(wheel, r))
    while len(answer) < N:
        r += stepSize
        if r>1:
            r %= 1
        answer.append(binSearch(wheel, r))
    return answer

"""
SELECTION TECHNIQUES
"""

def do_stochastic_universal_sampling(gene_list,fitness_func,selected_no):
    """
    returns a list of selected individuals based on stochstic universal sampling selection technique
    parameters:
    gene_list: candidate individuals
    fitness_func: fitness function used for selection
    selected_no: number of parents to be selected in this process
    """
    wheel = makeWheel(gene_list,fitness_func)
    
    
    return select(wheel,selected_no)

def do_k_tournament_selection(gene_list,fitness_func,selected_no):

    """
    returns a list of selected individuals based on k-tournament selection technique
    value of K has been declared as a global variable k_value_for_selection
    parameters:
    gene_list: candidate individuals
    fitness_func: fitness function used for selection
    selected_no: number of parents to be selected in this process
    """
    
    selected_parents = []

    for i in range(0,selected_no):

      gene_list_temp = gene_list[:]
      random.shuffle(gene_list_temp)
      fitness_list = [fitness_func(x) for x in gene_list_temp[:k_value_for_selection]]
      max_fitness = max(fitness_list)
      best_fit = gene_list_temp[fitness_list.index(max_fitness)] 
      selected_parents.append(best_fit)

    return selected_parents 

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
    
    
def do_uniform_crossover(gene_a_s,gene_b_s,crossover_rate):

    """
    applies uniform crossover between two genes with a probability
    parameters:
    gene_a_s, gene_b_s: two parent gene strings
    crossover_rate: probability of crossover 
    """
    
    gene_a = [c for c in gene_a_s]
    gene_b = [c for c in gene_b_s]
    
    
    for i in range(len(gene_a)):
        
        p = random.random()
        if p <= crossover_rate:
            gene_a[i], gene_b[i] = gene_b[i], gene_a[i] 

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

def do_inversion_mutation(gene_s,mutation_rate):
    

    """
    applies inversion mutation on a gene with a probability
    parameters:
    gene_s: child gene string
    mutation_rate: probability of mutation 
    """
  
    gene = [c for c in gene_s]
    
    p = random.random()
    if p<= mutation_rate:


      start = random.randint(0,len(gene_s)-2)
      end = random.randint(start+1,len(gene_s)-1)

      temp = gene[start:end+1]
      temp.reverse()
      gene[start:end+1] = temp
      
      
    return "".join(gene)

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
                 selection_func = do_stochastic_universal_sampling,
                 crossover_func = do_uniform_crossover,
                 mutation_func = do_bit_flip_mutation
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
            
            gene = ""
            
            for j in range(self.gene_size):
                prob=random.random()
                if prob <= self.bit_generation_probability[j]:
                    gene += "1"
                else:
                    gene += "0"
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
                
                
                selected_parents=self.selection_function(population,
                                                         self.fitness_function,
                                                         2)
                parent_a = selected_parents[0]#population[j*2]
                parent_b = selected_parents[1]#population[j*2+1]
                #print("selected ",parent_a,parent_b)
                new_genes = self.crossover_function(parent_a, parent_b, 
                             
                                                    self.crossover_rate)
                
                new_genes = [self.mutation_function(new_genes[0],
                                                    self.mutation_rate),
                             self.mutation_function(new_genes[1],
                                                    self.mutation_rate)]
                             
                Q += new_genes
            
            #print(Q)
            population = Q
            
        return best
            

        
if __name__=="__main__":
    
                    
    
    GA_instance=GeneticAlgorithm(selection_func=do_k_tournament_selection, 
    fitness_func = another_dummy_fitness_function,
    crossover_func = do_one_point_crossover,
    mutation_func = do_inversion_mutation)
    
    best_solution = GA_instance.run_GA()
    print("Best solution is: ",best_solution)
    
    """
    Testing codes for inversion mutation and one point crossover, You can test other crossover and mutation functions too.
    """
    print(do_inversion_mutation("101110001",0.3))
    print(do_one_point_crossover("10110","01010",0.8))
    