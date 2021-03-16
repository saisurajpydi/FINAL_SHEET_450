# Copy set bit in a range 
"""
Given two numbers x and y, and a range [l, r] where 1 <= l, r <= 32. The task is consider set bits of y in range [l, r] and set these bits in x also. Examples :

Input  : x = 10, y = 13, l = 2, r = 3
Output : x = 14
Binary representation of 10 is 1010 and 
that of y is 1101. There is one set bit
in y at 3’rd position (in given range). 
After we copy this bit to x, x becomes 1110
which is binary representation of 14.

Input  : x = 8, y = 7, l = 1, r = 2
Output : x = 11
"""

x = 8 #10
y = 7 #13
l = 1 #2
r = 2 #3 
x = bin(x)
xlen = len(x)
y = bin(y)
val = y[l+1:r+1+1]
for i in range(xlen - r -2):
    val += "0"
result = bin(int(x,2) + int(val,2))
print(int(result,2))

