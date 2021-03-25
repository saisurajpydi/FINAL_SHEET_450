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
"""
"""
def swap_string(s):
    swapped_string=""
    swapped_string += s.swapcase()
    return swapped_string
#print("enter ")
s = input()
print(swap_string(s))
"""
"""
import math
def gp(a,r,n):
    return (a * (int(math.pow(r,n-1))))
print("enter ")
a = list(map(int,input().split()))
print(gp(a[0],a[1],a[2]))
"""
"""
index = 10
print(index / 2)
print(index // 2)
"""
"""
a = ["1","2","3"]
s = ""
for i in a:
    s += i
print(s)
print(type(s))
s = int(s)
print(s)
print(type(s))
"""
import random
from tkinter import *
root=Tk()
root.geometry("700x400")
l1=Label(root,text='',font=("times",200))
def roll():
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()
b1=Button(root,text="lets roll",command=roll)
b1.place(x = 330, y = 0)
root.mainloop()