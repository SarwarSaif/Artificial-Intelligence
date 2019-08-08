# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 02:05:04 2018

@author: saif
"""
from copy import deepcopy
openList=[]
closedList=[]
goalState= [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','#']]



def printSteps(state):
    
    step=[]
    step= deepcopy(state)
    del step[3][5]
    del step[3][4]
    print(step)
    
    
def isSame(parent,child):
    flag = 0
    for i in range(m):
        for j in range(n):
            if parent[i][j] != child[i][j]:
                flag = 1
                break
    if flag == 0:
        return True
    else:
        return False
def leftSuccessor(currentState,x,y):
    
    if x-1 >= 0:
        state = deepcopy(currentState)
        state[x][y] = state[x - 1][y]
        state[x - 1][y] = '#'
        state[3][4]= state[3][4]+1
        state[3][5]= state[3][4]+heuristic(state)
        check=0
        for p in closedList:
            if isSame(p,state) == True:
              check=1
              break
        if check==0 :
            openList.append(state)

def rightSuccessor(currentState,x,y):
    
    if x + 1 < 4:
        state = deepcopy(currentState)
        state[x][y] = state[x + 1][y]
        state[x + 1][y] = '#'
        state[3][4]= state[3][4]+1
        state[3][5]= state[3][4]+heuristic(state)
        check=0
        for p in closedList:
            if isSame(p,state) == True:
              check=1
              break
        if check==0 :
            openList.append(state)

def upSuccessor(currentState,x,y):
    if y - 1 >= 0:
        state = deepcopy(currentState)
        state[x][y] = state[x][y - 1]
        state[x][y - 1] = '#'
        state[3][4]= state[3][4]+1
        state[3][5]= state[3][4]+heuristic(state)
        check=0
        for p in closedList:
            if isSame(p,state) == True:
              check=1
              break
        if check==0 :
            openList.append(state)
            
def downSuccessor(currentState,x,y):
    if y + 1 < 4:
        state = deepcopy(currentState)
        state[x][y] = state[x][y + 1]
        state[x][y + 1]= '#'
        state[3][4]= state[3][4]+1
        state[3][5]= state[3][4]+heuristic(state)
        check=0
        for p in closedList:
            if isSame(p,state) == True:
              check=1
              break
        if check==0 :
            openList.append(state)
def findSuccessor(currentState):
    
    for i in range(m):
        for j in range(n):
            if currentState[i][j] == '#':
                x, y = i, j
                break
    
    leftSuccessor(currentState,x,y)
    rightSuccessor(currentState,x,y)
    upSuccessor(currentState,x,y)
    downSuccessor(currentState,x,y)
    
            
def heuristic(A):
    c=0
    for i in range(m):
        for j in range(n):
            if A[i][j] != goalState[i][j] :
                c=c+1
    if c != 0 :
        c = c - 1
    return c

def isGoal(A):

    flag=0
    for i in range(4):
        for j in range(4):
            if A[i][j] != goalState[i][j] :
                flag=1

    if flag== 0:
        return True
    else:
        return False

def optimalState(openList):
    minValue=99
    optimal=[]
    for array in openList:
        if minValue > array[3][5]:
            minValue=array[3][5]
    for array in openList:
        if array[3][5] == minValue:
            optimal=array
            break
    openList.remove(optimal)
    closedList.append(optimal)
    return optimal
            
def AstarSearch(openList):
    while 1:
        currentState= optimalState(openList)
        if (isGoal(currentState)):
            printSteps(currentState)
            break
        else:
    
            findSuccessor(currentState)
            printSteps(currentState)
    
            
if __name__ == '__main__':
    global m,n
    n = int(input().strip())
    m = int(input().strip())
    initialState = [[0]*n for _ in range(m)]
    for i in range(n):
        initialState[i] = list(input().strip().split(" "))
    print(initialState)
    initialState[m-1].append(0)
    initialState[m-1].append( (initialState[3][4])+heuristic(initialState) )
    print(initialState)
    openList.append(initialState)
    AstarSearch(openList)
    
    
    