"""a = list(map(str,input().split()))
print(a)"""
"""b = input("enter ")
for i in b:
    print(i)
print(b)
"""
"""
# oops in python
class Dog:
    def __init__(self,name):
        self.name = name
        print(name)
    def bark(self):
        print("BARK")
    def add(self,x):
        return x + 1
d = Dog("suraj")

#print(d.add(1))
#d.bark()
"""
"""
n = 10
for i in reversed(range(n+1)):
    print(i, end = " ")
print("")
for i in range(n-1,-1,-1):
    print(i, end =" ")
print("")
for i in range(0,5):
    print(i,end = " ")
"""
from collections import deque
stk = deque()
stk.append(2)
stk.append(4)
print(stk)
#stk.pop()
print(stk[-1])
stk.pop()
stk.pop()
#print(stk.peek())
#stk.append(2)
if(not stk):
    print(not stk)
    stk.append(100)
    print(stk)
print(stk)


# max rectangle solution
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
