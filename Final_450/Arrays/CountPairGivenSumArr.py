"""
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
"""
"""
arr = []
k = int(input("enter the sum value : "))
n = int(input("enter the size of the array"))
print("enter the values in the array ")
for i in range(n):
    arr.append(int(input()))
count = 0
for i in range(n):
    for j in range(i+1,n):
        if(arr[i] + arr[j] == k):
            count += 1
print("the count is : ",count)
"""

def getPairsCount(arr,n,sum):
    m = [0] * 1000
    for i in range(n):
        m[arr[i]] += 1
    count = 0
    for i in range(n):
        count += m[sum - arr[i]]
        if(sum - arr[i] == arr[i]):
            count -= 1
    return int(count / 2)
 
 
# Driver function
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is", getPairsCount(arr, n, sum))