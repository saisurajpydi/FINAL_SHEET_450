"""
Given a binary matrix. Find the maximum area of a rectangle formed only of 1s in the given matrix.
"""
from collections import deque
def maxArea(M, n, m):
    # code here
    result = []
    resultVal = 0
    value = 0
    for i in range(1,n):
        for j in range(m):
            if(M[i][j]):
                M[i][j] += M[i-1][j]
        resultVal = maxHist(M,m)
        value = max(resultVal,value)
    return value

def maxHist(result,m):
    stk = deque()
    index = 0
    top = 0
    area = 0
    maxArea = 0
    while(index < m):
        if( not stk or result[stk[-1]] <= result[index]):
            stk.append(index)
            index += 1
        else:
            top = stk.pop()
            area = (result[top]*((index - stk[-1] - 1) if stack else index))
            maxArea = max(area,maxArea)
    while stk:
        top = stk[-1]
        area = (result[top]*((index - stk[-1] - 1) if stack else index))
        maxArea = max(area,maxArea)    
        
    return maxArea