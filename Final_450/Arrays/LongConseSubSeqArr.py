"""
Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
"""
arr = [1,9,3,10,4,20,2]
n = len(arr)
def longSubSeq(arr, n): 
    s = {}
    s = set()
    ans = 0
    for ele in arr: 
        s.add(ele) 
  
    for i in range(n): 
        if (arr[i]-1) not in s: 
  
            j = arr[i] 
            while(j in s): 
                j += 1
  
            ans = max(ans, j-arr[i]) 
    return ans 
print("the longest sub sequence is :",longSubSeq(arr,n))
