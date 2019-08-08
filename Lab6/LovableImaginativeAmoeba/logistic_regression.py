import random as rd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

"""
draws a line of equation y=coefflist[0]+coefflist[1]*x1+coefflist[2]*x2
parameters:
coefflist- a list of coefficients of a linear equation
"""
def drawLine(coefflist):

    a = -(coefflist[0]/coefflist[1])
    b = -(coefflist[0]/coefflist[2])
    plt.plot([a,0],[0,b],'k-')

"""
converts each data [x1,x2,y] (example- [10,2, 'red']) from datagiven to [(1,x1,x2), 1/0 ] form [(1,10,2),1]
parameters:
datagiven: dataset list
"""
def make_logistic_regression_dataset(datagiven):

    dataset = []
    for data in datagiven:

        label = None
        if data[2] == 'red':
            label = 1
        elif data[2] == 'blue':
            label = 0
        dataset.append(([1,data[0],data[1]],label))    
    return dataset

"""
implements sigmoid function
parameters: theta- coefficient list
x- feature vector
returns a value in [0,1]
"""
def sigmoid(theta,x):

    z = sum([ theta[i]*x[i] for i in range(3)])
    return 1.00/(1.00+np.exp(-z))

"""
runs batch gradient descent with alpha = learning rate on given dataset
returns 'theta' as stated in andrew ng note
"""
def run_logistic_regression(dataset, learning_rate=0.01, iteration=64):

    rd.seed()
    theta =[ rd.random() for i in range(3)]
    for i in range(iteration):
      
        for j in range(3):
            error_sum = 0.0
            for data in dataset:
                error_sum += (data[1]-sigmoid(theta,data[0]))*data[0][j]
    
            theta[j] += learning_rate*error_sum

        plt.subplot(8,8,(i+1))	
        for data in dataset:
            if data[1] == 1:
                plt.plot(data[0][1],data[0][2],'ro')
            elif data[1] == 0:
                plt.plot(data[0][1],data[0][2],'bo')
        
        drawLine(theta)
        
    plt.savefig("logregview.eps")
    plt.close()           
    return theta 
