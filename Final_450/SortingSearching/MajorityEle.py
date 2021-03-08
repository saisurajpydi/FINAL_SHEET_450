# MAJORITY ELEMENT
"""
Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.
 

Example 1:

Input:
N = 3 
A[] = {1,2,3} 
Output:
-1
Explanation:
Since, each element in 
{1,2,3} appears only once so there 
is no majority element.
"""

def majorityElement( A, N):
        #Your code here
    result = list()
    val = N // 2
    dic = dict()
    for i in A:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for keys,vals in dic.items():
        if vals > val:
            result.append(keys)
    if(result):
        ans = max(result)
        return ans
    return -1