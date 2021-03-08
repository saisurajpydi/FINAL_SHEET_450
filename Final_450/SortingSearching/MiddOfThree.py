# find the middle of given three numbers
"""
Given three distinct numbers A, B and C. Find the number with value in middle (Try to do it with minimum comparisons).


Example 1:

Input:
A = 978, B = 518, C = 300
Output:
518
Explanation:
Since 518>300 and 518<978, so 
518 is the middle element.
"""
def middle(self,a,b,c):
   #code here
    if( a > b ):
        if(b > c):
            return b
        elif(a > c):
            return c
        else:
            return a
    else:
        if(a > c):
            return a
        elif(c > b):
            return b
        else:
            return c