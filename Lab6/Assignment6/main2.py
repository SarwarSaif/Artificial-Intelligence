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
    #dataset = datalist
    splitRatio = 0.80
    train, test = nb.splitDataset(datalist, splitRatio)
    #print(train[1:10])
    
    """
    Converting datasets suitable for Naive Bayes
    """
    nbds = nb.make_naive_bayes_dataset(train)
    nbds2 = nb.make_naive_bayes_dataset(test)
    #print(nbds[1:10])

    
    """
    Running Naive Bayes and plotting the data points according to true and predicted classes
    """
    
    results = nb.run_naive_bayes_gaussian(nbds,2,4)
    #print(results)
    
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
        
    #plt.savefig('nbayes.pdf')
    plt.close()
    results2 = []
    #print(nbds[0][0][0])
    
    for i in range(len(nbds2)):
        predVal=0
        a=b=c=d=a2=b2=c2=d2=0
        
        for j in range(len(nbds)):
            a=abs(nbds[j][0][0]-nbds2[i][0][0])
            b=abs(nbds[j][0][1]-nbds2[i][0][1])
            c=abs(nbds[j][0][2]-nbds2[i][0][2])
            d=abs(nbds[j][0][3]-nbds2[i][0][3])
            if a<=a2 and b<=b2 and c<=c2 and d<=d2:
                
                predVal=results[j]
            a2=abs(nbds[j][0][0]-nbds2[i][0][0])          
            b2=abs(nbds[j][0][1]-nbds2[i][0][1])                         
            c2=abs(nbds[j][0][2]-nbds2[i][0][2])
            d2=abs(nbds[j][0][3]-nbds2[i][0][3])
        results2.append(predVal)

    print(results2)
    
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
    
       