# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 18:53:43 2017

@author: Naved


"""

import random
import math
#import DocumentProcessing
#from DocumentProcessing import *

default_gene_size = 5
default_iteration = 3
default_population_size = 5
default_crossover_rate = 0.5
default_mutation_rate = 0.05
default_bit_generation_probability = [0.5]*default_gene_size


def dummy_fitness_function(gene):

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


def makeWheel(population,fitness):
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

def do_stochastic_universal_sampling(gene_list,fitness_func,child_no):
    
    wheel = makeWheel(gene_list,fitness_func)
    
    
    return select(wheel,child_no)
 
def do_majority_voting(votes):
        
        bits = [ int(vote) for vote in votes ]
        result = (bits[0] & bits[1]) | (bits[1] & bits[2]) | (bits[2] & bits[0])
        return str(result)
    
def apply_TMR_in_Gene(Gene_list):
        
        result = ""
        
        gene_length = len(Gene_list[0][0])
        
        for i in range(gene_length):
            
            result += do_majority_voting( [gene[0][i] for gene in Gene_list ] )
        
        result_fitness = 0.16*Gene_list[0][1]+0.68*Gene_list[1][1]+0.16*Gene_list[2][1]
        return (result,result_fitness)
    
def do_uniform_crossover(gene_a_s,gene_b_s,crossover_rate):

    
    gene_a = [c for c in gene_a_s]
    gene_b = [c for c in gene_b_s]
    
    
    for i in range(len(gene_a)):
        
        p = random.random()
        if p <= crossover_rate:
            gene_a[i], gene_b[i] = gene_b[i], gene_a[i] 

    return ["".join(gene_a),"".join(gene_b)]


def do_bit_flip_mutation(gene_s,mutation_rate):
    
    gene = [c for c in gene_s]
    
    for i in range(len(gene)):
        
        p = random.random()
        
        #print(" at ",i)
        if p <= mutation_rate:
            
            #print("yes at ",i)
            gene[i] = str( 1- int(gene[i]))
            
    return "".join(gene)

                                     
class GeneticAlgorithm:

    """
    Class for genetic algorithm
    """    
    def __init__(self,
                 fitness_func = dummy_fitness_function,
                 selection_func = do_stochastic_universal_sampling,
                 crossover_func = do_uniform_crossover,
                 mutation_func = do_bit_flip_mutation
                 ):
        
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
        
        population=[]
        
        for i in range(self.population_size):
            
            gene=""
            
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
    
    
    def generate_population_FT(self):
        
        """
        returns an initial population for GA
        """
        
        populations=[[],[],[]]
        
        for i in range(self.population_size):
            
            gene=["","",""]
            probs = [0,0,0]
            for j in range(self.gene_size):
                for k in range(3):
                    probs[k] = random.random()
                if probs[0] <= self.bit_generation_probability[j]:
                    gene[0] += "1"
                else:
                    gene[0] += "0"
                if probs[1] <= self.bit_generation_probability[j]:
                    gene[1] += "0"
                else:
                    gene[1] += "1"
                if probs[2] <= 0.5:
                    gene[2] += "1"
                else:
                    gene[2] += "0"
                        
            #print(gene)
            for k in range(3):
                populations[k].append(gene[k])
        #print(population)    
        return populations
    
    def run_GA_FT(self):
        
        populations = self.generate_population_FT()
        bests = [(None,None),(None,None),(None,None)]
        
        for i in range(self.iteration):
            
            for k in range(3):
                for gene in populations[k]:
                    fitness = self.fitness_function(gene)
                #print(gene,fitness)
                    if bests[k][0] == None or bests[k][1] < fitness:
                        bests[k] = (gene,fitness)
                        Q = []
            
                for j in range(self.population_size//2):
                
                
                    selected_parents=self.selection_function(populations[k],
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
                    populations[k] = Q
            
        best = apply_TMR_in_Gene(bests)
        return best
        
    def run_GA(self):
        
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
    
                    
    
    GA_instance=GeneticAlgorithm()
    
    best_solution = GA_instance.run_GA()
    print(best_solution)
    print(do_bit_flip_mutation("10111",0.3))
    print(do_uniform_crossover("10110","01010",0.8))
    