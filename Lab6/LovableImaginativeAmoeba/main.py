import csv #for csv files
import pandas as pd #for reading data from csv file and operating on them
import random as rd 
import matplotlib #plotting
from matplotlib import pyplot as plt

import numpy as np #Faster matrix and array operations
from logistic_regression import * 
from naive_bayes import *
import naive_bayes as nb
data_file = "dummy_data.csv"



if __name__ == "__main__":

    """
    Reading data from file and plotting them. 'ro' means red circle. 'bo' = blue circle
    """  
    df = pd.read_csv(data_file)
    datalist= df.values.tolist()
    
    for data in datalist:

        if data[2] == 'red':
            plt.plot(data[0],data[1],'ro')
        elif data[2] == 'blue':
            
            plt.plot(data[0],data[1],'bo')
    plt.savefig('data.pdf')
    plt.close()
    

    """
    Converting datasets suitable for logistic regression
    """
    nbds = nb.make_naive_bayes_dataset(datalist)
    #print(nbds)

    """
    Running Naive Bayes and plotting the data points according to true and predicted classes
    """
    
    results = nb.run_naive_bayes_gaussian(nbds,2,2)
    print(results)
    for i in range(len(nbds)):

        data = datalist[i]
        true_label = data[2]
        predicted_label = results[i]

        if true_label == 'red' and predicted_label == 1 :
            plt.plot(data[0],data[1],'ro')
        elif true_label == 'blue' and predicted_label == 0:
            plt.plot(data[0],data[1],'bo')
        elif true_label == 'red' and predicted_label == 0 :
            plt.plot(data[0],data[1],'rx')
        elif true_label == 'blue' and predicted_label == 1:
            plt.plot(data[0],data[1],'bx')
        
    plt.savefig('nbayes.pdf')
    plt.close()
    
