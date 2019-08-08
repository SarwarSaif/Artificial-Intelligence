# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:17:36 2018

@author: saif
"""

import random
from random import shuffle
import numpy as np

def make_naive_bayes_dataset(datagiven):

    dataset = []
    for data in datagiven:

        label = None
        if data[4] == 1:
            label = 1
        elif data[4] == 0:
            label = 0
        dataset.append(([data[0],data[1],data[2],data[3]],label))    
    return dataset

def splitDataset(dataset, splitRatio):
    data=[]
    #shuffle(dataset)
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]


"""
calculates p(x) for gaussian distribution with mu,sigma
"""
def calculate_gaussian_probability(x,mu,sigma):

    result = np.exp(-((x-mu)**2)/(2.00*(sigma**2)))
    result /= ((2.00*3.1416*(sigma**2))**0.5)
    return result


"""
calculates prior , posterior probabilities and run naive bayes
"""
def run_naive_bayes_gaussian(dataset, num_of_class, num_of_features):

    Prior_probabilities = [0]*num_of_class

    class PosteriorInfo:

        def __init__(self, class_no, feature_no, number_of_class):

            self.class_no = class_no
            self.feature_no = feature_no
            self.number_of_class = number_of_class
            self.values = []
            self.mu = None
            self.sigma = None 

        def calculate_mu_sigma(self):

            self.mu = np.mean(self.values)
            self.sigma = np.std(self.values)

    Posterior_Infos = [].copy()

    for i in range(num_of_class):
        Posterior_Infos.append([])

        for j in range(num_of_features):
            Posterior_Infos[i].append([])
            Posterior_Infos[i][j] = PosteriorInfo(class_no = i, feature_no = j, number_of_class = num_of_class ) 
            
    
    

    for data in dataset:

        label = data[1]
        
        Prior_probabilities[label] += 1
        
        for j in range(num_of_features):

            Posterior_Infos[label][j].values.append(data[0][j])

        
    Prior_probabilities = [ x/len(dataset) for x in Prior_probabilities]
    
    
    for i in range(num_of_class):
        for j in range(num_of_features):
            Posterior_Infos[i][j].calculate_mu_sigma()

    results = []
    for data in dataset:

        result_label = 0
        max_probability = -1.0

        for i in range(num_of_class):
            product = Prior_probabilities[i]
            Posterior_data = Posterior_Infos[i][j]
            for j in range(num_of_features):
                product*= calculate_gaussian_probability(data[0][j],Posterior_data.mu,Posterior_data.sigma)
                
            
            
            if product>max_probability:
                max_probability = product
                result_label = i
                

        results.append(result_label)   

    return results