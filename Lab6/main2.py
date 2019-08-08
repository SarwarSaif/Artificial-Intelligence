# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:17:36 2018

@author: saif
"""

import csv #for csv files
import pandas as pd #for reading data from csv file and operating on them
import random as rd 
import matplotlib #plotting
from matplotlib import pyplot as plt

import numpy as np #Faster matrix and array operations
#from naive_bayes import *
import naiveBayes as nb
data_file = "banknote.csv"



if __name__ == "__main__":

    """
    Reading data from file and plotting them. 'ro' means red circle. 'bo' = blue circle
    """  
    df = pd.read_csv(data_file)
    datalist= df.values.tolist()
    #print(datalist)
    for data in datalist:

        if data[4] == 0:
            plt.plot(data[0],data[1],'ro')
        elif data[4] == 1:
            
            plt.plot(data[0],data[1],'bo')
    plt.savefig('data.pdf')
    plt.close()
    
    """
    Split the dataset in 80%-20% proportion randomly
    """
    splitRatio = 0.80
    train, test = nb.splitDataset(datalist, splitRatio)
    print(len(train))
    print(len(test))
    
    nbds = nb.make_naive_bayes_dataset(train)
    nbds2 = nb.make_naive_bayes_dataset(test)

    results = nb.run_naive_bayes_gaussian(nbds,2,4)
    
    for i in range(len(nbds)):

        data = train[i]
        true_label = data[4]
        predicted_label = results[i]

        if true_label == 1 and predicted_label == 1 :
            plt.plot(data[0],data[1],'ro')
        elif true_label == 0 and predicted_label == 0:
            plt.plot(data[0],data[1],'bo')
        elif true_label == 1 and predicted_label == 0 :
            plt.plot(data[0],data[1],'rx')
        elif true_label == 0 and predicted_label == 1:
            plt.plot(data[0],data[1],'bx')
        
    plt.close()
    results2 = []
    m0=0 
    m1=0
    mean=0.0
    for i in range(len(nbds)):
        e=abs(nbds[i][1]-results[i])
        #print(e)
        if e>0:
            predVal=1
            m1+=1
        else:
            predVal=0
            m0+=1
        results2.append(predVal)
    
    mean=(m0/(m0+m1)) * 100    
    
    print("Accuracy ")
    print(mean) #55.05925% accuracy
    
    for i in range(len(nbds2)):

        data = test[i]
        true_label = data[4]
        predicted_label = results2[i]

        if true_label == 1 and predicted_label == 1 :
            plt.plot(data[0],data[1],'ro')
        elif true_label == 0 and predicted_label == 0:
            plt.plot(data[0],data[1],'bo')
        elif true_label == 1 and predicted_label == 0 :
            plt.plot(data[0],data[1],'rx')
        elif true_label == 0 and predicted_label == 1:
            plt.plot(data[0],data[1],'bx')
        
    plt.savefig('nbayes2.pdf')
    plt.close()
    
       