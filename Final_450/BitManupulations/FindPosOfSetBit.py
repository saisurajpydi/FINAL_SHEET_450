# Find position of set bit
"""
Given a number N having only one ‘1’ and all other ’0’s in its binary representation, find position of the only set bit. If there are 0 or more than 1 set bit the answer should be -1. Position of  set bit '1' should be counted starting with 1 from LSB side in binary representation of the number.

Example 1:

Input:
N = 2
Output:
2
Explanation:
2 is represented as "10" in Binary.
As we see there's only one set bit
and it's in Position 2 and thus the
Output 2.
Example 2:

Input:
N = 5
Output:
-1
Explanation:
5 is represented as "101" in Binary.
As we see there's two set bits
and thus the Output -1.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findPosition() which takes an integer N as input and returns the answer.

Expected Time Complexity: O(log(N))
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 108
"""

def findPosition( N):
        # code here 
    x = str(bin(N).replace("0b",""))
    x = x[::-1]
    count = 0
    result = 0
    for i in range(len(x)):
        if( x[i] == "1"):
            result = i+1
            count += 1 
    if(count == 1):
        return result
    else:
        return -1

print(findPosition(2))