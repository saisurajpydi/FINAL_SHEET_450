# Count triplets with sum smaller than X
"""
Given an array arr[] of distinct integers of size N and a sum value X, the task is to find count of triplets with the sum smaller than the given sum value X.

 

Example 1:

Input: N = 6, X = 2
arr[] = {-2, 0, 1, 3}
Output:  2
Explanation: Below are triplets with 
sum less than 2 (-2, 0, 1) and (-2, 0, 3). 

Example 2:

Input: N = 5, X = 12
arr[] = {5, 1, 3, 4, 7}
Output: 4
Explanation: Below are triplets with 
sum less than 12 (1, 3, 4), (1, 3, 5), 
(1, 3, 7) and (1, 4, 5).

"""

def countTriplets(self, arr, n, sum):
        # Your code goes here
    count = 0 
    arr.sort()
    for i in range(0,n-2):
        j = i + 1
        k = n - 1
        while ( j < k):
            if(arr[i] + arr[j] + arr[k] >= sum):
                k -= 1
            else:
                count += (k - j)
                j += 1
    
    return count 