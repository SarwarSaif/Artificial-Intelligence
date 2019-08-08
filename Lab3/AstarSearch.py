# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 22:01:37 2018

@author: majaa
"""

import numpy as np
import random
from copy import deepcopy

rmv=[]
q = []
result = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'#']]

def children(parent):
    for i in range(4):
        for j in range(4):
            if parent[i][j] == '#':
                x, y = i, j
                break
    if x - 1 >= 0:
        flag=0
        b = deepcopy(parent)
        b[x][y] = b[x - 1][y]
        b[x - 1][y] = '#'
        b[3][4]= b[3][4]+1
        b[3][5]= b[3][4]+countf(b)
        for p in rmv:
            if wasParent(p,b) == True:
              flag=1
              break
        if flag==0 :
            q.append(b)

    if x + 1 < 4:
        flag2 = 0
        b = deepcopy(parent)
        b[x][y] = b[x + 1][y]
        b[x + 1][y] = '#'
        b[3][4] = b[3][4] + 1
        b[3][5] = b[3][4] + countf(b)
        for p in rmv:
            if wasParent(p,b) == True:
              flag2=1
              break
        if flag2 == 0 :
            q.append(b)
    if y - 1 >= 0:
        flag3 = 0
        b = deepcopy(parent)
        b[x][y] = b[x][y - 1]
        b[x][y - 1] = '#'
        b[3][4] = b[3][4] + 1
        b[3][5] = b[3][4] + countf(b)
        for p in rmv:
            if wasParent(p,b) == True:
              flag3=1
              break
        if flag3==0:
            q.append(b)

    if y + 1 < 4:
        flag4 = 0
        b = deepcopy(parent)
        b[x][y] = b[x][y + 1]
        b[x][y + 1] = '#'
        b[3][4] = b[3][4] + 1
        b[3][5] = b[3][4] + countf(b)
        for p in rmv:
            if wasParent(p,b) == True:
              flag4=1
              break
        if flag4==0 :
            q.append(b)


def countf(A):
    c=0
    for i in range(4):
        for j in range(4):
            if A[i][j] != result[i][j] :
                c=c+1
    if c != 0 :
        c = c - 1
    return c

def goal(A):

    flag=0
    for i in range(4):
        for j in range(4):
            if A[i][j] != result[i][j] :
                flag=1

    if flag== 0:
        return True
    else:
        return False

def lowest(q):
    lowValue=5000
    Low=[]
    for p in q:
        if lowValue > p[3][5]:
            lowValue=p[3][5]
    for p in q:
        if p[3][5] == lowValue:
            Low=p
            break
    q.remove(Low)
    rmv.append(Low)
    return Low

def printf(A):
    mat=[]
    for i in range(4):
      mat.append([])
    for i in range(4):
        for j in range(4):
            mat[i].append(j)
            mat[i][j]=A[i][j]
    print(mat)
def wasParent(parent,child):
    flag = 0
    for i in range(4):
        for j in range(4):
            if parent[i][j] != child[i][j]:
                flag = 1
                break
    if flag == 0:
        return True
    else:
        return False

def Astar(q):
    flag=0
    while 1:
     low = lowest(q)
     if (goal(low)):
        printf(low)
        break
     else:

        children(low)
        printf(low)

if __name__ == '__main__':
    #given=[[1,2,3,4],[5,6,'#',8],[9,10,7,11],[13,14,15,12]]
    given=[[1,2,3,4],[5,6,7,8],[9,'#',10,12],[13,14,11,15]]
    
    given[3].append(4)
    print(given)
    given [3][4] = 0
    given[3].append(5)
    print(given)
    given [3][5]=given[3][4]+countf(given)
    print(given)
    q.append(given)
    Astar(q)
    '''given2=[[1,2,3,4],[5,'#',6,7],[8,9,10,11],[12,13,14,15,5,1]]
    rmv.append(given2)
    given2=[[1,2,3,4],[5,6,'#',7],[8,9,10,11],[12,13,14,15,2,3]]
    children(given2)
    print(q)
    print(rmv)
    '''