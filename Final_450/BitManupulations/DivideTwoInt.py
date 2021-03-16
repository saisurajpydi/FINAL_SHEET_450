# Divide two integers without using multiplication, division and mod operator

"""
Given a two integers say a and b. Find the quotient after dividing a by b without using multiplication, division and mod operator.

Example: 

Input : a = 10, b = 3
Output : 3

Input : a = 43, b = -8
Output :  -5 
"""

a = 10 
b = 3
ans = 0
result = 0
for i in range(a):
    ans += 3    
    if(ans > a):
        result = ans - b
        break
print(result)
    