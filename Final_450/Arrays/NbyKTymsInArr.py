"""
Given an array of size n and a number k, find all elements that appear more than n/k times
"""
arr = [3, 1, 2, 2, 1, 2, 3, 3]
n = len(arr)
k = int(input("enter the k value : "))
def count(arr,n,k):
    x = n/k
    freq = {}
  
    for i in range(n) :    
        if arr[i] in freq :
            freq[arr[i]] += 1
        else :
            freq[arr[i]] = 1
        
    for i in freq :
        if (freq[i] > x) :
            print(i)


count(arr, n, k)